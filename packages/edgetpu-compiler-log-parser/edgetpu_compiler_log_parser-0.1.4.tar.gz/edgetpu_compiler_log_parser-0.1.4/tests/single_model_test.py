import unittest

import subprocess
from edgetpu_compiler_log_parser import EdgeTPUCompilerLogParser
from pprint import pprint


class TestSingleModel(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        super(TestSingleModel, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        super(TestSingleModel, cls).tearDownClass()

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test(self):
        model_path = "tests/model/mobilenet_v2_1.0_224_inat_bird_quant.tflite"
        cmd = f"edgetpu_compiler -a -o tests/model/compiled {model_path}"
        result = subprocess.check_output(cmd, shell=True)

        log_parser = EdgeTPUCompilerLogParser(result)
        pprint(log_parser.get_compiled_infos())


if __name__ == "__main__":
    unittest.main()
