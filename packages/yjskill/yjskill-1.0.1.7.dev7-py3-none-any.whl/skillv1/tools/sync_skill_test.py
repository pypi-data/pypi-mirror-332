# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
import json

from .sync_skill import Config
from skillv1.client import skill_api_datasource as datasource


class TestSkillAPI(unittest.TestCase):
    """
    Test Device
    """

    def test_config(self):
        """"""

        config = Config.init_from_env()
        config.skill_from_kind = datasource.EdgeKind.Edge.name
        print(f"%s", config)
        print(datasource.EdgeKind.Edge.name)


def suite():
    """
    suite
    """
    suite = unittest.TestSuite()
    # suite.addTest(TestSkillAPI('test_check_accelerator'))
    suite.addTest(TestSkillAPI('test_config'))
    return suite


if __name__ == '__main__':
    unittest.main(defaultTest='suite')
