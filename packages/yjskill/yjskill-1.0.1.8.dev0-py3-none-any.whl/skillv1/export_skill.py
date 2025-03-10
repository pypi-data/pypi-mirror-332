"""
Authors: duanshichao(duanshichao@baidu.com)
Date: 2025/03/09
"""
import json
import os
import traceback
from argparse import ArgumentParser
# import bcelogger
from dataclasses import dataclass

import bcelogger as logger
import yaml
from graphv1.graph_api_graph import GraphContent
from jobv1.client.job_api_event import EventKind
from jobv1.client.job_api_job import parse_job_name, GetJobRequest
from jobv1.client.job_api_metric import MetricLocalName, MetricKind, CounterKind, DataType
from jobv1.client.job_client import (
    JobClient
)
from jobv1.tracker.tracker import Tracker
from windmillartifactv1.client.artifact_api_artifact import parse_artifact_name

from .skill_api_skill import GetSkillRequest, parse_skill_name
from .skill_client import SkillClient

EXPORT_SKILL = "Export/Skill"
EXPORT_SKILL_TASK = "export-skill"


@dataclass
class Config:
    """Configuration container for model synchronization.

    Attributes:
        org_id: Organization ID
        user_id: User ID
        job_name: Name of the job
        windmill_endpoint: Endpoint for windmill service
        output_artifact_path: Path for output artifacts
        job_kind: Kind of job (default: SYNC_MODEL)
        task_name: Name of the task (default: sync-model)
    """

    org_id: str
    user_id: str
    job_name: str
    windmill_endpoint: str
    vistudio_endpoint: str
    output_artifact_path: str

    workspace_id: str = ""
    job_local_name: str = ""

    job_kind: str = EXPORT_SKILL
    task_name: str = EXPORT_SKILL_TASK

    @classmethod
    def from_env(cls) -> "Config":
        """Create configuration from environment variables."""
        return cls(
            org_id=os.getenv("ORG_ID"),
            user_id=os.getenv("USER_ID"),
            job_name=os.getenv("JOB_NAME"),
            windmill_endpoint=os.getenv("WINDMILL_ENDPOINT"),
            vistudio_endpoint=os.getenv("VISTUDIO_ENDPOINT"),
            output_artifact_path=os.getenv(
                "PF_OUTPUT_ARTIFACT_SKILL_DATA", "./skill_data"
            ),
        )

    def validate(self) -> None:
        """Validate configuration parameters."""
        if not self.org_id:
            raise ValueError("org_id cannot be empty")
        if not self.user_id:
            raise ValueError("user_id cannot be empty")
        if not self.job_name:
            raise ValueError("job_name cannot be empty")
        if not self.windmill_endpoint:
            raise ValueError("windmill_endpoint cannot be empty")
        if not self.vistudio_endpoint:
            raise ValueError("vistudio_endpoint cannot be empty")


def parse_args():
    """
    Parse arguments.
    """
    parser = ArgumentParser()
    parser.add_argument("--skill_name", required=True, type=str, default="")

    args, _ = parser.parse_known_args()
    return args


def run():
    """
    Export skill.
    """
    try:
        logger.info("Starting export skill")
        args = parse_args()
        config = Config.from_env()
        config.validate()
        logger.info(f"Configuration: {config}")

        job_client = JobClient(
            endpoint=config.windmill_endpoint,
            context={"OrgID": config.org_id, "UserID": config.user_id},
        )
        skill_client = SkillClient(endpoint=config.vistudio_endpoint,
                                   context={"OrgID": config.org_id, "UserID": config.user_id})

        sync_manager = SkillExportManager(
            config, job_client=job_client, skill_client=skill_client
        )

        sync_manager.export_skill(args.skill_name)
        logger.info("ExportSkill End")
    except Exception as e:
        logger.error(f"ExportSkill Error: {str(e)}")
        logger.error(f"StackTrace: {traceback.format_exc()}")
        logger.error("ExportSkill End")
        return 1


class SkillExportManager:
    """Manages Skill Export """

    def __init__(
            self, config: Config, skill_client: SkillClient, job_client: JobClient
    ):
        """
        Initialize the sync manager.

        Args:
            config: Configuration object
            skill_client: Vistudio client instance
            job_client: Job client instance
        """
        self.config = config
        self.skill_client = skill_client
        self.job_client = job_client
        self.tracker = None

    def export_skill(
            self, skill_version_name: str
    ) -> None:
        """
        Synchronize model to devices.

        Args:
            skill_version_name: skill artifact name
        """
        # 1.初始化基础配置
        try:
            model_artifact_names = []
            self._initialize_tracker()
            logger.info("ExportSkill _initialize_tracker")

            self._log_task_total_skills(1)
            logger.info("ExportSkill _log_task_total_skills")
            artifact = parse_artifact_name(skill_version_name)
            skill_name = parse_skill_name(artifact.object_name)
            skill = self.skill_client.get_skill(req=GetSkillRequest(
                workspaceID=skill_name.workspace_id,
                localName=skill_name.local_name,
                version=artifact.version))

            if skill.graph:
                graph_content = GraphContent(nodes=skill.graph["nodes"], )
                nodes = graph_content.get_nodes("ObjectDetectOperator")
                logger.info(f"ExportSkill get ObjectDetectOperator nodes {str(nodes)}")

                for node in nodes:
                    model = node.get_property("modelName")
                    if model:
                        model_artifact_names.append(model.value)
            else:
                raise ValueError(f"Invalid skill graph content. job: {self.config.job_name}, "
                                 f"skill_name:{skill_version_name},"
                                 f"skill: {skill}")

            skill_file_path = os.path.join(self.config.output_artifact_path, 'skill.yaml')
            models_file_path = os.path.join(self.config.output_artifact_path, 'models.json')

            # 将 skill 写入 YAML
            with open(skill_file_path, 'w', encoding='utf-8') as file:
                yaml.dump(skill, file, allow_unicode=True)
            logger.info(f"ExportSkill write skill yaml {str(skill)}")

            # 将模型工件名称写入 JSON
            with open(models_file_path, 'w', encoding='utf-8') as file:
                json.dump(model_artifact_names, file, ensure_ascii=False)
            logger.info(f"ExportSkill write model names {str(model_artifact_names)}")

            self.tracker.log_metric(
                local_name=MetricLocalName.Success,
                kind=MetricKind.Counter,
                counter_kind=CounterKind.Cumulative,
                data_type=DataType.Int,
                value=[str(1)],
            )
            self.tracker.log_event(
                kind=EventKind.Succeed,
                reason=f"技能名称(版本)：{str(skill.display_name)}(v{str(artifact.version)})",
            )
            self.tracker.log_event(
                kind=EventKind.Succeed,
                reason=f"技能ID：{str(skill_version_name)}",
            )
        except Exception as e:
            self.tracker.log_event(
                kind=EventKind.Failed,
                reason="技能导出错误：技能模板导出失败",
                message=f"技能导出失败：系统内部错误 {str(e)}",
            )
            self.tracker.log_metric(
                local_name=MetricLocalName.Failed,
                kind=MetricKind.Gauge,
                counter_kind=CounterKind.Cumulative,
                data_type=DataType.Int,
                value=[str(1)],
            )
            logger.error(f"Failed to export skill: {str(e)}")
            return

    def _initialize_tracker(self) -> None:
        """Initialize the tracker with parsed job name."""
        parsed_job_name = parse_job_name(self.config.job_name)
        if not parsed_job_name or not (
                parsed_job_name.local_name and parsed_job_name.workspace_id
        ):
            raise ValueError(f"Invalid job name: {self.config.job_name}")

        self.config.workspace_id = parsed_job_name.workspace_id
        self.config.job_local_name = parsed_job_name.local_name
        self._set_job_kind(parsed_job_name)
        self.tracker = Tracker(
            windmill_client=self.job_client,
            workspace_id=parsed_job_name.workspace_id,
            job_name=self.config.job_name,
            # pf 生成
            task_name=self.config.task_name,
        )

    def _set_job_kind(self, job_name) -> None:
        """Set job kind based on job name."""
        job = self.job_client.get_job(
            GetJobRequest(
                workspace_id=job_name.workspace_id,
                local_name=job_name.local_name,
            )
        )
        self.config.job_kind = job.kind

    def _log_task_total_skills(self, skill_total: int) -> None:
        """Log the total number of skill."""
        self.tracker.log_metric(
            local_name=MetricLocalName.Total,
            kind=MetricKind.Counter,
            counter_kind=CounterKind.Cumulative,
            data_type=DataType.Int,
            value=[str(skill_total)],
        )

    def _log_job_total_skills(self, job_total) -> None:
        if self.config.job_kind == EXPORT_SKILL:
            self.tracker.log_metric(
                local_name=MetricLocalName.Total,
                kind=MetricKind.Counter,
                counter_kind=CounterKind.Cumulative,
                data_type=DataType.Int,
                value=[str(job_total)],
                task_name="",
            )


if __name__ == "__main__":
    run()
