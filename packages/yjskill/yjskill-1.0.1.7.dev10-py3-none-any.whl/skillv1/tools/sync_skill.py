# !/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
实现技能下发
1. 技能下发到盒子

技能下发进度说明：
1. 核心是两个task，先执行sync_model，再执行sync_skill
2. sync_model: 上报下述指标(数字为示例)
    2.1 job_total=100
    2.2 model_successd=90
    2.3 model_failed=10
3. sync_skill: 上报下述指标(数字为示例)
    3.1 skill_total=90 (=model_successd)
    3.2 skill_successed=70
    3.3 skill_failed=20
    3.4 job_failed=10+20=30 (=model_failed+skill_failed)
    3.5 job_successed=70 (=skill_successed)

"""

import traceback
from argparse import ArgumentParser
import os
import json
from dataclasses import dataclass
from typing import List, Dict, Any, Optional, Tuple
from pydantic import BaseModel
import bcelogger as logger


from jobv1.client import job_client
from jobv1.client import job_api_job as job_api
from jobv1.client import job_api_event as event_api
from jobv1.client import job_api_metric as metric_api
from jobv1.client import job_api_task as task_api
from jobv1.tracker import tracker

from devicev1.client import device_client, device_api

from windmillartifactv1.client import artifact_api_artifact as artifact_api

from skillv1.client import skill_api_skill as skill_api
from skillv1.client import skill_client
from skillv1.client import skill_api_datasource as datasource_api


@dataclass
class Config:
    """
    技能同步器配置

    Attributes:
        sync_kind: str, 技能下发类型，Edge:下发到盒子,SubCloud:下发到子平台
        skill_name: str, 技能名称,对应SkillVersionName, e.g. "workspaces/:ws/skills/:localName/versions/:version"
        skill_create_kind: str, 技能创建类型, e.g. "Sync"
        skill_from_kind: str, 技能来源类型, e.g. "Edge"
        vistudio_endpoint: str, 技能服务后端, e.g. "http://ip:port"
        windmill_endpoint: str, windmill服务后端, e.g. "http://ip:port"
        device_names: list[str], 目标设备名称列表,对应DeviceName, e.g. ["workspaces/:ws/devices/:deviceName"]
        org_id: str
        user_id: str
        job_name: str, 技能下发任务名称
        skill_task_name: str, 技能下发子任务名称
        sync_model_succeed_resul: list[str], 模型下发成功结果列表,若模型下发失败则技能下发也失败
    """

    vistudio_endpoint: str
    windmill_endpoint: str
    device_names: list[str]

    org_id: str
    user_id: str
    workspace_id: str

    job_name: str
    job_local_name: str
    skill_task_name: str
    skill_task_display_name: str

    model_result_path: str
    sync_model_result: dict

    sync_kind: datasource_api.EdgeKind
    skill_name: str
    skill_local_name: str
    skill_version: str
    skill_create_kind: str
    skill_from_kind: str

    device_hub_name: str

    @classmethod
    def init_from_env(cls) -> "Config":
        """Create configuration from environment variables."""
        return cls(
            org_id=os.getenv("ORG_ID"),
            user_id=os.getenv("USER_ID"),
            job_name=os.getenv("JOB_NAME"),
            skill_task_name=os.getenv("PF_STEP_NAME", ""),
            windmill_endpoint=os.getenv("WINDMILL_ENDPOINT"),
            vistudio_endpoint=os.getenv("VISTUDIO_ENDPOINT", ""),
            model_result_path=os.getenv(
                "PF_INPUT_ARTIFACT_MODEL_URI", ""),
            skill_task_display_name="技能模板下发",
            device_names=[],
            workspace_id="",
            job_local_name="",
            sync_model_result={},
            sync_kind=datasource_api.EdgeKind.Edge,
            skill_name="",
            skill_local_name="",
            skill_version="",
            skill_create_kind="Sync",
            skill_from_kind="Edge",
            device_hub_name="default",
        )


class SkillSynchronizer:
    """
    技能同步器
    """

    config: Config
    skill: skill_api.Skill
    targets: list[dict]  # 下发到的目的地

    __skill_cli: skill_client.SkillClient
    __job_cli: job_client.JobClient
    __device_cli: device_client.DeviceClient

    __total = 0  # 技能下发总数
    __skill_succeed_count = 0
    __skill_failed_count = 0
    __job_succeed_count = 0
    __job_failed_count = 0
    __event_reason_format = "{}（{}）{}"  # 中文名（id）成功/失败原因

    def __init__(self,
                 config: Config,
                 skill_cli: skill_client.SkillClient,
                 device_cli: device_client.DeviceClient,
                 job_cli: job_client.JobClient):
        """
        initialize the class.
        """

        self.config = config

        self.__total = len(self.config.sync_model_result)
        self.__job_failed_count = len(self.config.device_names) - self.__total

        artifact_name = artifact_api.parse_artifact_name(
            self.config.skill_name)
        if not artifact_name or not (
            artifact_name.object_name and artifact_name.version
        ):
            raise ValueError(
                f"Invalid artifact name: {self.config.skill_name}")
        self.config.skill_version = artifact_name.version

        skill_name = skill_api.parse_skill_name(artifact_name.object_name)
        if not skill_name or not (
            skill_name.workspace_id and skill_name.local_name
        ):
            raise ValueError(f"Invalid skill name: {self.config.skill_name}")
        self.config.skill_local_name = skill_name.local_name

        parsed_job_name = job_api.parse_job_name(self.config.job_name)
        if not parsed_job_name or not (
            parsed_job_name.local_name and parsed_job_name.workspace_id
        ):
            raise ValueError(f"Invalid job name: {self.config.job_name}")
        self.config.workspace_id = parsed_job_name.workspace_id
        self.config.job_local_name = parsed_job_name.local_name

        self.__skill_cli = skill_cli
        self.__device_cli = device_cli
        self.__job_cli = job_cli

    def __get_skill(self) -> None:
        """
        获取技能信息

        Returns:
            boolean: 是否成功
            dict: 错误信息, 例如：{"error": "Internal Server Error xxxx", "reason": "技能上线失败"}
        """

        req = skill_api.GetSkillRequest(
            workspaceID=self.config.workspace_id,
            localName=self.config.skill_local_name,
            version=self.config.skill_version)
        skill = self.__skill_cli.get_skill(req=req)
        if skill.graph is not None and 'draft' in skill.graph:
            skill.graph['draft'] = {}
        self.skill = skill

    def __sync_skill(self, device_accelerator_config: dict, device: dict) -> Optional[dict]:
        """
        下发技能
        1. 对接任务中心, 更新技能下发子任务的成功失败数量

        Args:
            req: SyncSkillRequest, 技能下发请求参数
        Returns:
            dict: 错误信息, 例如：{"error": "Internal Server Error xxxx", "reason": "技能上线失败"}
        """

        # 下发校验
        err_msg = self.__check_device(
            device=device, device_accelerator_config=device_accelerator_config)
        if err_msg is not None:
            logger.error("CheckDeviceFailed: %s", err_msg)
            return {"error": err_msg, "reason": err_msg}

        # 更新graph
        skill = self.skill
        device_workspace = device.get("workspaceID", None)
        model_result = self.config.sync_model_result.get(device["name"])
        target_model_name = model_result.get("artifactName")
        old_model_name = get_model_name(self.skill.graph)
        logger.debug(
            "SyncSkill old_model_name: %s, target_model_name: %s",
            old_model_name, target_model_name)
        target_skill_workspace = skill.workspaceID
        # 修改graph中的workspace,model_name
        replace = {}
        if skill.workspaceID != "public":
            target_skill_workspace = device_workspace
            replace[skill.workspaceID] = device_workspace
        if old_model_name is not None and old_model_name != target_model_name:
            replace[old_model_name] = target_model_name
        graph = build_skill_graph(
            origin_graph=skill.graph,
            replace=replace)
        logger.debug("SyncSkill build_skill_graph: %s",
                     json.dumps(graph, ensure_ascii=False))

        # 创建技能
        create_skill_req = skill_api.CreateSkillRequest(
            workspaceID=target_skill_workspace,
            localName=skill.localName,
            displayName=skill.displayName,
            description=skill.description,
            kind=skill.kind,
            fromKind=self.config.skill_from_kind,
            createKind=self.config.skill_create_kind,
            tags=skill.tags,
            graph=graph,
            artifact=skill.graph.get('artifact'),
            imageURI=skill.imageURI,
            defaultLevel=skill.defaultLevel,
            alarmConfigs=skill.alarmConfigs)
        ok, created_result = self.__create_skill(req=create_skill_req,
                                                 device=device)
        if not ok:
            return created_result

        # 技能上线
        return self.__release_skill(skill=created_result, device=device)

    def __get_device_configuration(self) -> dict:
        """
        获取设备配置

        Returns:
            dict: 设备硬件-显卡对应关系
        """

        workspace_id = self.config.workspace_id
        # 注意，应该用device的workspace_id，而不是skill的workspace_id
        if self.__total > 0:
            device_name = next(iter(self.config.sync_model_result))
            device_name = device_api.parse_device_name(device_name)
            workspace_id = device_name.workspace_id

        req = device_client.GetConfigurationRequest(
            workspace_id=workspace_id,
            device_hub_name=self.config.device_hub_name,
            local_name="default")
        resp = {}
        resp = self.device_cli.get_configuration(req=req)
        deviceAcceleratorConfig = {}
        if resp is not None and resp.device_configs is not None:
            for item in resp.device_configs:
                deviceAcceleratorConfig[item.kind] = item.gpu
        return deviceAcceleratorConfig

    def __check_device(self,
                       device_accelerator_config: dict,
                       device: dict) -> Optional[str]:
        """
        检查技能是否能下发

        Args:
            dest (dict): 下发的目的地，例如：盒子信息
        Returns:
            bool: 是否匹配
            str: 错误信息
        """

        if device["status"] == "Disconnected":
            return "设备已断开连接"

        if device["kind"] not in device_accelerator_config:
            return "未找到设备的硬件信息"

        if self.skill.graph is None:
            return "未找到技能的硬件信息"

        artifact = self.skill.graph.get('artifact', None)
        if artifact is None:
            return "未找到技能的硬件信息"

        skill_tag = self.skill.graph['artifact'].get('tags', {})

        return check_accelerators(
            skill_accelerator=skill_tag.get("accelerator", ""),
            target_accelelator=device_accelerator_config[device["kind"]])

    def __list_devices(self,
                       workspace_id: str,
                       device_local_names: list[str]) -> list[Any]:

        list_device_req = device_api.ListDeviceRequest(
            workspaceID=workspace_id,
            deviceHubName=self.config.device_hub_name,
            pageSize=200,
            pageNo=1,
            selects=device_local_names)
        devices = []
        resp = self.__device_cli.list_device(req=list_device_req)
        if resp is not None and resp.result is not None:
            devices.extend(resp.result)
        return devices

    def __create_skill(self,
                       req: skill_api.CreateSkillRequest,
                       device: dict) -> Tuple[bool, dict]:
        """
        创建技能

        Args:
            req: skill_api.CreateSkillRequest, 技能创建请求参数
            target: dict, 下发目标
        Returns:
            skill: 创建的技能的信息
        """

        try:
            device_name = device.get("localName")
            target_workspace = device.get("workspaceID")
            device_url = f'v1/workspaces/{req.workspace_id}/skills'
            invoke_method_req = device_api.InvokeMethodHTTPRequest(
                workspaceID=target_workspace,
                deviceHubName=self.device_hub_name,
                deviceName=device_name,
                uri=device_url,
                body=req.model_dump(by_alias=True),
            )
            skill_resp = self.__device_cli.invoke_method_http(
                request=invoke_method_req)
            logger.debug('CreateSkill req=%s, resp=%s',
                         invoke_method_req, skill_resp)
            return True, skill_resp
        except Exception as e:
            logger.error("SyncSkillCreateSkill device=%s Failed: %s",
                         device_name, traceback.format_exc())
            return False, {"error": str(e), "reason": "创建技能失败"}

    def __release_skill(self,
                        skill: skill_api.Skill,
                        device: dict) -> Optional[dict]:
        """
        技能上线

        Args:
            released_version: int, 要上线的技能版本号
            extra_data: dict,额外参数
        Returns:
            dict: 错误信息, 例如：{"error": "Internal Server Error xxxx", "reason": "技能上线失败"}
        """

        # 技能下发成功后，技能热更新
        artifact = None
        if skill.graph is not None:
            artifact = skill.graph.get('artifact')
        artifact_version = None
        if artifact is not None:
            artifact_version = artifact.get('version')
        if artifact_version is None:
            logger.error("ReleaseSkillFailed artifact_version is none")
            return {"error": "技能版本号为空", "reason": "技能上线失败"}

        released_version = artifact_version

        device_hub_name = device.get("deviceHubName")
        device_name = device.get("localName")
        target_workspace = device.get("workspaceID")

        workspace_id = skill.workspaceID
        local_name = skill.localName
        update_skill_request = skill_api.UpdateSkillRequest(
            workspaceID=workspace_id,
            localName=local_name,
            releasedVersion=released_version)
        try:
            skill_url = f'api/vistudio/v1/workspaces/{workspace_id}/skills/{local_name}/put'
            invoke_method_req = device_api.InvokeMethodHTTPRequest(
                workspaceID=target_workspace,
                deviceHubName=device_hub_name,
                deviceName=device_name,
                uri=skill_url,
                body=update_skill_request.model_dump(by_alias=True),
            )
            skill_resp = self.device_cli.invoke_method_http(
                request=invoke_method_req)
            logger.info('ReleaseSkill req=%s, resp=%s',
                        invoke_method_req, skill_resp)
            if hasattr(skill_resp, 'success') and skill_resp.success == False:
                raise Exception(skill_resp.message)
            return None
        except Exception as e:
            logger.error("ReleaseSkillFailed device=%s Failed: %s",
                         device_name, traceback.format_exc())
            return {"error": str(e), "reason": "技能上线失败"}

    def run(self) -> None:
        """
        执行技能下发逻辑
        """

        logger.info("SyncSkillRun Start")

        # 初始化基础配置
        device_accelerator_config = {}
        device_local_names = []
        device_map = {}  # key: device_local_name, value: device_info
        try:
            # 更新task的display_name，因为pf的task无法在创建时设置display_name
            update_task_req = task_api.UpdateTaskRequest(
                workspace_id=self.config.workspace_id,
                job_name=self.config.job_local_name,
                local_name=self.config.skill_task_name,
                display_name=self.config.skill_task_display_name)
            self.__job_cli.update_task(request=update_task_req)

            self.tracker = tracker.Tracker(
                client=self.__job_cli,
                workspace_id=self.config.workspace_id,
                job_name=self.config.job_name,
                task_name=self.config.skill_task_name,
            )

            # symc_skill task total
            self.tracker.log_metric(
                local_name=metric_api.MetricLocalName.Total,
                task_name=self.config.skill_task_name,
                kind=metric_api.MetricKind.Counter,
                counter_kind=metric_api.CounterKind.Cumulative,
                data_type=metric_api.DataType.Int,
                value=[str(self.__total)]
            )

            self.__get_skill()
            # 设备-显卡关系
            device_accelerator_config = self.__get_device_configuration()

            # 要使用device_name中的workspace，而不是技能的workspace，因为有公共技能
            # 此处仅考虑了多个device都是同一个workspace的情况
            device_workspace_id = ""
            for name in self.config.sync_model_result:
                device_name = device_api.parse_device_name(name)
                device_local_names.append(device_name.local_name)
                device_workspace_id = device_name.workspace_id
            devices = self.__list_devices(workspace_id=device_workspace_id,
                                          device_local_names=device_local_names)
            for device in devices:
                device_local_name = device.get("localName", "")
                device_map[device_local_name] = device
        except Exception as e:
            logger.error("SyncSkillFailed %s", traceback.format_exc())
            self.__skill_failed_count += self.__total
            self.__job_failed_count += self.__total
            reason = self.__event_reason_format.format(
                "", "", "技能模板下发系统内部错误")
            # sync_skill failed count
            self.tracker.log_metric(
                local_name=metric_api.MetricLocalName.Failed,
                kind=metric_api.MetricKind.Counter,
                counter_kind=metric_api.CounterKind.Cumulative,
                data_type=metric_api.DataType.Int,
                value=[str(self.__skill_failed_count)]
            )
            # job failed event
            # job failed count
            self.tracker.log_metric(
                local_name=metric_api.MetricLocalName.Failed,
                task_name="",
                kind=metric_api.MetricKind.Counter,
                counter_kind=metric_api.CounterKind.Cumulative,
                data_type=metric_api.DataType.Int,
                value=[str(self.__job_failed_count)]
            )
            self.tracker.log_event(
                kind=event_api.EventKind.Failed,
                task_name="",
                reason=reason,
                message=str(e)[:500]
            )
            return

        logger.debug("SyncSkill skill: \n%s", self.skill)

        # 技能下发，目标是模型下发成功的那些target
        for device_local_name, device in device_map:
            logger.info("SyncSkillDeviceStart device: %s", device_local_name)
            device_displayname = device.get("displayName", "")

            try:
                result = self.__sync_skill(
                    device=device,
                    device_accelerator_config=device_accelerator_config)
                if result is None:
                    self.__skill_succeed_count += 1
                    self.__job_succeed_count += 1
                    reason = self.__event_reason_format.format(
                        device_displayname, device_local_name, "技能模板下发成功")
                    # sync_skill success count
                    self.tracker.log_metric(
                        local_name=metric_api.MetricLocalName.Success,
                        kind=metric_api.MetricKind.Counter,
                        data_type=metric_api.DataType.Int,
                        value=[str(self.__skill_succeed_count)]
                    )
                    # job success event
                    # job succeed count
                    self.tracker.log_metric(
                        local_name=metric_api.MetricLocalName.Success,
                        task_name="",
                        kind=metric_api.MetricKind.Counter,
                        data_type=metric_api.DataType.Int,
                        value=[str(self.__job_succeed_count)]
                    )
                    self.tracker.log_event(
                        kind=event_api.EventKind.Succeed,
                        task_name="",
                        reason=reason,
                        message=result["error"][:500]
                    )
                else:
                    self.__skill_failed_count += 1
                    self.__job_failed_count += 1
                    reason = self.__event_reason_format.format(
                        device_displayname, device_local_name, result["reason"])
                    # sync_skill failed count
                    self.tracker.log_metric(
                        local_name=metric_api.MetricLocalName.Failed,
                        kind=metric_api.MetricKind.Counter,
                        data_type=metric_api.DataType.Int,
                        value=[str(self.__skill_failed_count)]
                    )
                    # job failed event
                    # job failed count
                    self.tracker.log_metric(
                        local_name=metric_api.MetricLocalName.Failed,
                        task_name="",
                        kind=metric_api.MetricKind.Counter,
                        counter_kind=metric_api.CounterKind.Cumulative,
                        data_type=metric_api.DataType.Int,
                        value=[str(self.__job_failed_count)]
                    )
                    self.tracker.log_event(
                        kind=event_api.EventKind.Failed,
                        task_name="",
                        reason=reason,
                        message=result["error"][:500]
                    )
            except Exception as e:
                logger.error("SyncSkillDevice Failed: %s",
                             traceback.format_exc())
                self.__skill_failed_count += 1
                self.__job_failed_count += 1
                reason = self.__event_reason_format.format(
                    device_displayname, device_local_name, "技能模板下发系统内部错误")
                # sync_skill failed count
                self.tracker.log_metric(
                    local_name=metric_api.MetricLocalName.Failed,
                    kind=metric_api.MetricKind.Counter,
                    data_type=metric_api.DataType.Int,
                    value=[str(self.__skill_failed_count)]
                )
                # job failed event
                # job failed count
                self.tracker.log_metric(
                    local_name=metric_api.MetricLocalName.Failed,
                    task_name="",
                    kind=metric_api.MetricKind.Counter,
                    counter_kind=metric_api.CounterKind.Cumulative,
                    data_type=metric_api.DataType.Int,
                    value=[str(self.__job_failed_count)]
                )
                self.tracker.log_event(
                    kind=event_api.EventKind.Failed,
                    task_name="",
                    reason=reason,
                    message=result["error"][:500]
                )

            logger.info("SyncSkillDeviceEnd device: %s", device_local_name)

        logger.info("SyncSkillRun End")


def check_accelerators(skill_accelerator: str,
                       target_accelelator: str) -> Optional[str]:
    """
    检查硬件是否匹配

    Args:
        skill_accelerator(str): 技能硬件信息(tag['accelerator'])
        target_accelelator(str): 设备硬件型号
    Returns:
        bool: 是否匹配
        str: 错误信息
    """

    if skill_accelerator == "":
        return None

    if target_accelelator == "":
        return "设备硬件不适配"

    # 将技能硬件信息转换为列表
    skill_accelerators = json.loads(skill_accelerator)
    device_accelerators = [target_accelelator]

    for sac in skill_accelerators:
        if sac not in device_accelerators:
            return "设备硬件不适配"

    return None


def build_skill_graph(
        origin_graph: dict,
        replace: dict):
    """
    构建graph, 内容替换<old,new>

    Args:
        origin_graph: dict 原始图
        replace: dict 替换关系<old,new>
    Returns:
        dict: 新图
    """

    origin_graph_json = json.dumps(origin_graph)
    for old, new in replace.items():
        origin_graph_json = origin_graph_json.replace(old, new)
    return json.loads(origin_graph_json)


def get_model_name(graph: dict):
    """
    获取模型名称

    Args:
        graph: dict 图
    Returns:
        str: 模型名称, 若未找到返回None
    """

    nodes = graph['nodes']
    for node in nodes:
        if node['kind'] == 'ObjectDetectOperator':
            for property in node['properties']:
                if property['name'] == 'modelName':
                    return property['value']
    return None


def parse_args() -> ArgumentParser:
    """
    Parse arguments.
    """
    parser = ArgumentParser()
    parser.add_argument("--edge_kind", required=True, type=str, default="Edge")
    parser.add_argument("--skill_name",
                        required=True, type=str, default="")
    parser.add_argument("--device_names", required=True, type=str, default="")
    parser.add_argument(
        "--device_hub_name", default="default", type=str, help="Name of the device hub"
    )

    args, _ = parser.parse_known_args()
    return args


def main() -> int:
    """
    运行技能下发

    Returns:
        int: 返回值，0表示成功，非零表示失败
    """

    try:
        logger.info("SyncSkill Start")

        args = parse_args()
        logger.info("SyncSkillArgs: %s", args)

        config = Config.init_from_env()
        logger.info("SyncSkill params, \n \
                    org_id: %s, \n \
                    user_id: %s, \n \
                    job_name: %s, \n \
                    skill_task_name: %s, \n \
                    vistudio_endpoint: %s, \n \
                    windmill_endpoint: %s, \n \
                    device_names: %s, \n \
                    model_result_path: %s \n", config.org_id, config.user_id,
                    config.job_name, config.skill_task_name, config.vistudio_endpoint,
                    config.windmill_endpoint, args.device_names, config.model_result_path)

        model_succeed_result = {}
        if os.path.exists(config.model_result_path):
            with open(config.model_result_path, 'r', encoding='utf-8') as file:
                model_succeed_result = json.load(file)
                logger.info("SyncSkill ModelSucceedResult: %s",
                            model_succeed_result)
        else:
            logger.warning(
                "SyncSkill ModelSucceedResult File Not Exists")
        config.sync_model_result = model_succeed_result

        config.device_hub_name = args.device_hub_name
        device_names = args.device_names.split(",")
        config.device_names = device_names
        edge_kind = datasource_api.EdgeKind[args.edge_kind]
        config.sync_kind = edge_kind
        config.skill_from_kind = edge_kind.name
        config.skill_name = args.skill_name

        skill_cli = skill_client.SkillClient(endpoint=config.vistudio_endpoint,
                                             context={"OrgID": config.org_id,
                                                      "UserID": config.user_id})
        job_cli = job_client.JobClient(endpoint=config.windmill_endpoint,
                                       context={"OrgID": config.org_id,
                                                "UserID": config.user_id})
        device_cli = device_client.DeviceClient(endpoint=config.windmill_endpoint,
                                                context={"OrgID": config.org_id,
                                                         "UserID": config.user_id})

        syncer = SkillSynchronizer(config=config,
                                   skill_cli=skill_cli,
                                   device_cli=device_cli,
                                   job_cli=job_cli)
        syncer.run()
        logger.info("SyncSkill End")
        return 0
    except Exception as e:
        logger.error("SyncSkill Error: {%s}", str(e))
        logger.error("StackTrace: {%s}", traceback.format_exc())
        logger.info("SyncSkill End")
        return 1


if __name__ == "__main__":
    exit(main())
