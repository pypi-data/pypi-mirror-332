from pprint import pprint
import unittest

import subprocess
from edgetpu_compiler_log_parser import EdgeTPUCompilerLogParser


class TestMultipleModel(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        super(TestMultipleModel, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        super(TestMultipleModel, cls).tearDownClass()

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test(self):
        model_path1 = "tests/model/mobilenet_v2_1.0_224_inat_bird_quant.tflite"
        model_path2 = "tests/model/efficientnet-edgetpu-M_quant.tflite"
        model_path3 = "tests/model/dummy.tflite"
        cmd = f"edgetpu_compiler -a -o tests/model/compiled "
        cmd += f"{model_path1} "
        cmd += f"{model_path2} "
        cmd += f"{model_path3} "
        cmd += f"{model_path3} "
        cmd += f"{model_path3} "

        result = subprocess.check_output(cmd, shell=True)
        print(result.decode("utf-8"))

        log_parser = EdgeTPUCompilerLogParser(result)
        pprint(log_parser.get_compiled_infos())


if __name__ == "__main__":
    unittest.main()
