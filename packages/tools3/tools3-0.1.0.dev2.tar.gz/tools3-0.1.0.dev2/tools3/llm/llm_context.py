class LLMContext(object):
    TYPE_IS_DEEPSEEK = "deepseek"
    TYPE_IS_OPENAI = "openai"

    def __init__(self):
        self.type = ""
        self.key = ""
        self.base_url = ""
        self.model = ""
        self.use_code_file = ""
        self.use_code_method = ""
        self.php_bin_path = ""

    def is_llm(self):
        if self.type != "":
            return True

        if self.use_code_file != "":
            return True

        if self.use_code_method != "":
            return True
        return False