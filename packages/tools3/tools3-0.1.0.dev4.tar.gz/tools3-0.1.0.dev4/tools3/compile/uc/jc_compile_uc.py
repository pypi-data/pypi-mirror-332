from tools3.compile.config import ParamsJsonConfig, FieldsJsonConfig
from tools3.compile import Compile
from tools3.compile.uc import CompileUC
import json

"""
编译成json用例
"""
class JCCompileUC(Compile):
    step_name = "jc_compile_uc"
    params = {}
    fields_formatters = {}
    expected = None
    include_field_names = False
    separator = "_"

    json_file_path = ""

    def __init__(self, json_file_path):
        super().__init__()
        self.json_file_path = json_file_path

    def get_json_file_path(self):
        return self.json_file_path

    def compile(self, compile_json_file_path) -> bool:
        self.get_logger().info(self.step_name + " compile start", data={
            "json_file_path": self.json_file_path,
            "compile_json_file_path": compile_json_file_path,
        })
        try:
            json_config_file_path = self.get_json_file_path()
            fields_config = FieldsJsonConfig.new_instance(json_config_file_path)
            expected = fields_config.get_expected()

            uc = CompileUC(
                fields=fields_config.get_fields(),
                expected=expected,
                include_field_names=fields_config.get_include_field_names(),
                separator=fields_config.get_separator(),
            )
            uc.set_base_logger(self.get_base_logger())
            result = uc.compile(compile_json_file_path)
        except Exception as e:
            self.get_logger().error(self.step_name + " compile error: {}".format(e))
            raise e
        self.get_logger().info(self.step_name + " compile end")
        return result