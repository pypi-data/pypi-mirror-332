import json
class FieldsJsonConfig(object):
    name = ""
    desc = ""
    fields = {}
    expected = {}
    config = {}

    def __init__(self, name, desc, fields, expected, config = {}):
        self.name = name
        self.desc = desc
        self.fields = fields
        self.expected = expected
        self.config = config

    def get_name(self):
        return self.name
    def get_desc(self):
        return self.desc

    def get_fields(self):
        if self.fields:
            return self.fields
        else:
            return {}

    def get_expected(self):
        if self.expected:
            return self.expected
        else:
            return None

    def get_config(self):
        if self.config is None:
            return {}
        return self.config

    def get_include_field_names(self):
        return self.get_config().get("include_field_names", False)

    def get_separator(self):
        return self.get_config().get("separator", "_")


    @staticmethod
    def new_instance(json_config_file_path):
        with open(json_config_file_path) as json_file:
            json_data = json.loads(json_file.read())
        fields_json_config = FieldsJsonConfig(
            name=json_data.get("name", ""),
            desc=json_data.get("desc", ""),
            fields=json_data.get("params", {}),
            expected=json_data.get("expected", {}),
            config=json_data.get("config", {}),
        )
        return fields_json_config

    @staticmethod
    def new_instance_from_data(jc_data):
        fields_json_config = FieldsJsonConfig(
            name=jc_data.get("name", ""),
            desc=jc_data.get("desc", ""),
            fields=jc_data.get("params", {}),
            expected=jc_data.get("expected", {}),
            config=jc_data.get("config", {}),
        )
        return fields_json_config