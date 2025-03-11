# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import unittest



class TestExportSkill(unittest.TestCase):
    """
    Test WindmillDevice Python SDK
    """

    def __init__(self, methodName='runTest'):
        super().__init__(methodName=methodName)

    def test_write_artifact(self):
        """
        Test List Devices
        """

        model_artifact_names = []
        models_artifact_path = os.path.join("./skill_data", 'artifact.txt')
        model_artifact_string = ",".join(model_artifact_names)
        with open(models_artifact_path, 'w', encoding='utf-8') as file:
            file.write(model_artifact_string)
        print(f"tags: {1}")



def suite():
    """
    suite
    """
    suite = unittest.TestSuite()
    suite.addTest(TestExportSkill('test_metric'))
    return suite


if __name__ == '__main__':
    print('starting tests...')
    unittest.main(defaultTest='suite')
