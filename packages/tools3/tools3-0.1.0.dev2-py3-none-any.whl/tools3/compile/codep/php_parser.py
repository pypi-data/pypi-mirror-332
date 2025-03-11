import os

from tools3 import get_package_dir
from tools3.compile.config import ParamsJsonConfig, FieldsJsonConfig
from tools3.compile import Compile
from tools3.compile.uc import CompileUC
import json
import subprocess
import shlex
import os

from langchain_community.chat_models import ChatOllama
from langchain_core.output_parsers import StrOutputParser
from langchain_core.messages import SystemMessage,HumanMessage
from langchain_core.prompts import ChatPromptTemplate
from langchain.globals import set_debug
from langchain_openai import ChatOpenAI

from tools3.llm import LLMContext

set_debug(True)
"""
编译成json用例
"""
class PhpParser(Compile):
    def __init__(self, code_file_path):
        self.llm = None
        self.bin_path = "php"
        super().__init__()
        if code_file_path == "":
            code_file_path = '/Users/zhaoweijie/work/develop/company/docker-compose-nginx-php/dhb168-local-docker/www/pc-dhb168/Dinghuobao/DhbApi/Controller/Admin/AdminCartController.class.php'
        self.code_file_path = code_file_path
        self.llm_context = None
    def set_llm_context(self, llm_context :LLMContext):
        self.llm_context = llm_context
        return self
    def get_llm_context(self) -> LLMContext:
        return self.llm_context

    def get_bin_path(self):
        return self.bin_path
        return "/usr/local/Cellar/php@7.3/7.3.33_11/bin/php"

    def set_bin_path(self, bin_path):
        self.bin_path = bin_path

    def get_raw_file_parser_path(self):
        package_dir = get_package_dir()
        php_al_dir = os.path.join(package_dir, "data", "php-al")
        php_al_file = os.path.join(php_al_dir, "PhpFileParser.php")
        return php_al_file

    def get_code_file_path(self):
        return self.code_file_path

    def get_llm(self):
        if self.llm is not None:
            return self.llm
        # self.llm = self.get_ollama_llm()
        if self.llm_context is None:
            return None
        if self.llm_context.type == LLMContext.TYPE_IS_DEEPSEEK:
            self.llm = self.get_deepseek_llm()
            return self.llm
        return self.llm

    def get_ollama_llm(self):
        model = ChatOllama(
            model="llama3.2:1b",
            # model="deepseek-r1:1.5b",
            temperature=0,
            verbose=True
        )
        return model

    def get_deepseek_llm(self):
        base_url = self.llm_context.base_url
        if self.llm_context.base_url == "" or self.llm_context.base_url is None:
            base_url = "https://api.deepseek.com2"
        api_key = self.llm_context.key
        model = self.llm_context.model
        if model == "":
            model = "deepseek-chat2"
        model = ChatOpenAI(
            base_url=base_url,
            api_key=api_key,
            model=model,  # 或者使用其他适合的模型
            temperature=0,
            verbose=True
        )
        return model

    def get_method_code(self, method_name):
        # return ""
        package_dir = get_package_dir()
        bin_path = self.get_bin_path()
        raw_file_parser_path = self.get_raw_file_parser_path()
        code_file_path = self.get_code_file_path()
        command = f"{bin_path}  '{raw_file_parser_path}' '{code_file_path}'"
        args = shlex.split(command)
        json_result = subprocess.run(args, capture_output=True, text=True)
        result = json.loads(json_result.stdout)
        code = result.get("code")
        if code is None:
            self.get_logger().info(self.step_name + " php parser error: {}".format(json_result.stdout), data={
                "package_dir": package_dir,
                "bin_path": bin_path,
                "raw_file_parser_path": raw_file_parser_path,
                "code_file_path": code_file_path,
                "command": command,
                "json_result": json_result.stdout,
            })
            raise Exception("php al error: " + json_result.stdout)
        result_data = result.get("data")
        method_info = result_data.get("methods", {}).get(method_name)
        if method_info is None:
            self.get_logger().info(self.step_name + " method name '" + method_name + "' not found.", data={
                "method_name": method_name,
                "package_dir": package_dir,
                "bin_path": bin_path,
                "raw_file_parser_path": raw_file_parser_path,
                "code_file_path": code_file_path,
                "command": command,
                "methods": result.get("methods", {}).keys(),
                "json_result": json_result.stdout,
            })
            raise Exception("method '" + method_name + "' not found.")
        return method_info["code"]

    def get_units_code(self, method_name):
        method_code = self.get_method_code(method_name)
        sys_prompt = self.get_units_code_sys_prompt()
        user_prompt = f"""
        根据以下PHP代码生成{method_name}方法单元测试
```php
{method_code}
```
        """
        system_msg = SystemMessage(content=sys_prompt)
        user_msg = HumanMessage(content=user_prompt)

        prompt = ChatPromptTemplate.from_messages([
            system_msg,
            user_msg,
        ])
        chain = prompt | self.get_llm() | StrOutputParser()
        units_code = chain.invoke({
            # "method_name": method_name,
            # "method_code": method_code,
        })
        units_code2 = """
根据提供的 PHP 代码，我将为 `del` 方法生成单元测试代码。以下是生成的单元测试代码：

```php
<?php
namespace Tests\Tools3Tests\Dinghuobao\DhbApi\Controller\Admin;

use Common\Service\ControllerService;
use DhbApi\Controller\Admin\AdminCartController;
use Tests\TestCase;
use Tests\Tools3Tests\AllureHelperTrait;

use Yandex\Allure\Adapter\Annotation\AllureId;
use Yandex\Allure\Adapter\Annotation\Issues;
use Yandex\Allure\Adapter\Annotation\Title;
use Yandex\Allure\Adapter\Annotation\Description;
use Yandex\Allure\Adapter\Annotation\Features;
use Yandex\Allure\Adapter\Annotation\Stories;
use Yandex\Allure\Adapter\Annotation\Severity;
use Yandex\Allure\Adapter\Annotation\Label;
use Yandex\Allure\Adapter\Annotation\Labels;
use Yandex\Allure\Adapter\Annotation\Parameter;
use Yandex\Allure\Adapter\Model\DescriptionType;
use Yandex\Allure\Adapter\Model\SeverityLevel;
use Yandex\Allure\Adapter\Model\ParameterKind;
use Yandex\Allure\Adapter\Support\StepSupport;

/**
 * @Title("AdminCartController")
 * @Features ({"APP管理端", "购物车管理"})
 */
class DelTest extends TestCase
{
    use AllureHelperTrait;

    function getDataProvider() {
        $data = [];
        // 直接使用 PHP 数组
        $dataNew = [];
        foreach ($data as $item) {
            $testcase = $item['case'];
            $paramData = $item['data'];
            $expected = $item['expected'];
            $dataNew[] = [
                $testcase,
                $paramData,
                $expected,
            ];
        }
        return $dataNew;
    }

    /**
     * @param string $testcase
     * @param $paramData
     * @param $expected
     * @return void
     * @dataProvider getDataProvider
     */
    public function testDel($testcase, $paramData, $expected)
    {
        $startTestEvent = $this->newStartTestEvent("", "");
        $startTestEvent->withTitle($this->getClassCaseName(__CLASS__, $testcase));
        $this->startTest($startTestEvent);
        if ($testcase == "__testcase__") {
            $this->endTest();
            $this->assertTrue(true, $testcase);
            return;
        }
        // 此处是大模型生成的单元测试代码
        $params = $paramData['params'];
        $delLists = $paramData['delLists'];
        $companyId = $paramData['companyId'];
        $loginAccountsId = $paramData['loginAccountsId'];
        $facade = $this->createMock(DhbCompanyFacade::class);
        $adminCartService = $this->createMock(AdminCartService::class);
        $adminCartService->method('del')->willReturn(count($delLists));
        $controller = new AdminCartController();
        $controller->facade = $facade;
        $controller->inParam = $params;
        $result = $controller->del();
        $this->assertEquals(200, $result['code'], $testcase);
        $this->assertEquals('成功', $result['message'], $testcase);
        $this->assertArrayHasKey('del_count', $result['data'], $testcase);
        $this->endTest();
    }
}
```

### 代码说明：
1. **getDataProvider 方法**：该方法用于提供测试数据，目前为空数组，您可以根据需要填充测试数据。
2. **testDel 方法**：这是针对 `del` 方法的单元测试。它模拟了 `DhbCompanyFacade` 和 `AdminCartService` 的行为，并测试了 `del` 方法的返回值是否符合预期。
3. **断言**：测试了返回的 `code`、`message` 和 `data` 是否符合预期。

### 注意事项：
- 您需要根据实际业务逻辑填充 `getDataProvider` 方法中的测试数据。
- 如果 `del` 方法中有其他依赖项，您可能需要在测试中进一步模拟这些依赖项的行为。

希望这个单元测试代码对您有所帮助！如果有任何问题或需要进一步的调整，请告诉我。
        """
        units_code = self.extract_code(units_code + "")
        return units_code

    def extract_code(self, text):
        start_tag = "```php"
        end_tag = "```"

        start_index = text.find(start_tag)
        end_index = text.rfind(end_tag)  # 找到最后一个 ```

        if start_index != -1 and end_index != -1 and start_index < end_index:
            code = text[start_index + len(start_tag):end_index].strip()
            code = code.replace("{", "{{").replace("}", "}}")
            return code
        return None

    def get_units_code_sys_prompt(self):
        return """
# Role: 单元测试生成助手

## Profile
- author: LangGPT
- version: 1.0
- language: 中文
- description: 你是一名专业的单元测试生成助手，能够根据提供的 Python 代码模板和 PHP 代码，自动生成 PHP 单元测试。

## Skills
- 能够理解并解析 Python 代码模板
- 能够分析 PHP 代码结构，提取关键函数
- 能够根据 Python 模板，填充测试数据并生成 PHP 单元测试代码
- 确保生成的测试代码符合 PHPUnit 规范

## Rules
1. **分析 PHP 代码**: 识别关键的业务逻辑和方法（例如 `add()` 方法）。
2. **匹配 Python 模板**: 识别 模板中的 `{{method_name}}` 并替换成目标方法名。
3. **生成单元测试**:
   - 生成符合 PHPUnit 规范的测试方法。
   - 确保 `assertEquals` 或其他适当的断言匹配业务逻辑。
5. **代码格式化**: 确保生成的代码符合 PHP 代码风格规范（PSR-12）。

## Workflows
1. **读取PHP模板**
   - 模板中的 getDataProvider 方法保持原样
   - 识别 `{{method_name}}`、`{{phpunit_code}}`、`{{php_array}}`变量 
2. **解析 PHP 代码**
   - 识别 `public function` 关键字，找到目标方法
   - 提取方法参数及关键业务逻辑
3. **填充模板**
   - 用方法名替换 `{{method_name}}`
   - `{{php_array}}` 不做任何修改
   - getDataProvider方法体不做任何修改
   - 只生成测试PHP代码，不生成测试数据，然后放入到`{{phpunit_code}}` 变量填充为具体的代码调用
   
4. **输出 PHP 单元测试**
   - 确保符合 PHPUnit 规范
   - 代码结构清晰，可读性强

## php单元测试模板
```text
function getDataProvider() {{
    $data = {{php_array}};
    // 直接使用 PHP 数组
    $dataNew = [];
    foreach ($data as $item) {{
        $testcase = $item['case'];
        $paramData = $item['data'];
        $expected = $item['expected'];
        $dataNew[] = [
            $testcase,
            $paramData,
            $expected,
        ];
    }}
    return $dataNew;
}}
/**
 * @param string $testcase
 * @param $paramData
 * @param $expected
 * @return void
 * @dataProvider getDataProvider
 */
public function test{{method_name}}($testcase, $paramData, $expected)
{{
    if ($testcase != "__testcase__") {{
        $this->assertTrue(true);
        return;
    }}
    $startTestEvent = $this->newStartTestEvent("", "");
     $startTestEvent->withTitle($this->getClassCaseName(__CLASS__, $testcase));
     $this->startTest($startTestEvent);
     if ($testcase == "__testcase__") {
         $this->endTest();
         $this->assertTrue(true, $testcase);
         return;
     }
    // 此处是大模型生成的单元测试代码
    {{phpunit_code}}
    $this->assertEquals(true, true, $testcase);
    $this->endTest();

}}
```

## 示例1
### 输入: 根据以下PHP代码生成ajaxReturnError方法单元测试
```php
namespace DhbApi\Controller\Admin;


class AdminBaseListStandController  extends AdminBaseController
{
    /**
     * @param array|mixed $data
     * @param string $message
     * @param int $code
     */
    public function ajaxReturnError($data, $message = '失败', $code = 500)
    {
        $this->ajaxReturnStandard($data, $message, $code);
    }
}

```
### 输出
```php
<?php
namespace Tests\Tools3Tests\Dinghuobao\DhbApi\Controller\Admin\AdminBaseController;

use Common\Service\ControllerService;
use DhbApi\Controller\Admin\AdminBaseListStandController;
use Tests\TestCase;
use Tests\Tools3Tests\AllureHelperTrait;


use Yandex\Allure\Adapter\Annotation\AllureId;
use Yandex\Allure\Adapter\Annotation\Issues;
use Yandex\Allure\Adapter\Annotation\Title;
use Yandex\Allure\Adapter\Annotation\Description;
use Yandex\Allure\Adapter\Annotation\Features;
use Yandex\Allure\Adapter\Annotation\Stories;
use Yandex\Allure\Adapter\Annotation\Severity;
use Yandex\Allure\Adapter\Annotation\Label;
use Yandex\Allure\Adapter\Annotation\Labels;
use Yandex\Allure\Adapter\Annotation\Parameter;
use Yandex\Allure\Adapter\Model\DescriptionType;
use Yandex\Allure\Adapter\Model\SeverityLevel;
use Yandex\Allure\Adapter\Model\ParameterKind;
use Yandex\Allure\Adapter\Support\StepSupport;

/**
 * @Title("AdminBaseListStandController")
 * @Features ({"APP管理端", "APP管理端Base"})
 */
class AjaxReturnErrorTest extends TestCase
{
    use AllureHelperTrait;



    function getDataProvider() {
        $params = {php_array};
        // 直接使用 PHP 数组
        $paramsNew = [];
        foreach ($params as $item) {
            $testcase = $item['case'];
            $paramData = $item['data'];
            $expected = $item['expected'];
            $paramsNew[] = [
                $testcase,
                $paramData,
                $expected,
            ];
        }
        return $paramsNew;
    }



    /**
     * @param string $testcase
     * @param $paramData
     * @param $expected
     * @return void
     * @dataProvider getDataProvider
     */
    public function testAjaxReturnError($testcase, $paramData, $expected)
    {
        $startTestEvent = $this->newStartTestEvent("", "");
        $startTestEvent->withTitle($this->getClassCaseName(__CLASS__, $testcase));
        $this->startTest($startTestEvent);
        if ($testcase == "__testcase__") {
            $this->endTest();
            $this->assertTrue(true, $testcase);
            return;
        }
        $dataNew = $paramData['data'];
        $message = $paramData['message'];
        $code = $paramData['code'];
        $skey = $paramData['skey'];
        $skeyData = $paramData['accounts'];
        ControllerService::setIsMockForceReturn(true);
        $_GET['noSkey'] = $skey;
        $controller = new AdminBaseListStandController();
        $controller->inParam['action'] = 'noSkey';
        $controller->inParam['skey'] = $skey;
        S($skey, $skeyData);
        $result = $controller->ajaxReturnError($dataNew, $message, $code);
        $result = ControllerService::getIsMockForceReturnData();
        $this->assertArrayHasKey('data', $result, $testcase);
        $this->assertArrayHasKey('message', $result, $testcase);
        $this->assertArrayHasKey('code', $result, $testcase);
        $this->endTest();
    }
}
```
        """