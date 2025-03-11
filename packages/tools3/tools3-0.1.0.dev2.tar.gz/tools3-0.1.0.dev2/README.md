
## 使用示例
```shell
# 安装
pip install tools3
# 会在 demo.py 生成测试用例
tools3-cli -t json_phpunit examples/demo_config.json
# 会生成phpunit文件
examples/demo_config.json.phpunit
```
# examples/demo_config.json
```json
{
  "params": {
    "can_use_integral": {
      "values": {
        "积分_null": null,
        "积分_空字符串": "",
        "积分_数字零": "0",
        "积分_是": "1",
        "积分_否": "2"
      }
    },
    "enable_integral": {
      "values": {
        "积分应用未安装": null,
        "积分应用已启用": "T",
        "积分应用禁用": "F",
        "积分应用已过期": "E",
        "积分应用非法数组": [1,2,3, {"ok":  true}]
      }
    }
  },
  "expected": {
    "hasException": false,
    "code": [422, 500]
  }
}

```

```text
tools3-cli -t jc_py examples/demo_config.json
tools3-cli -t py_uc examples/demo_config.py
tools3-cli -t uc_phpunit examples/demo_config.uc.json

tools3-cli -t jc_uc examples/demo_config.json
tools3-cli -t jc_phpunit examples/demo_config.json

```

```shell
pip install unittest
pip install python-json-logger

```

### 运行单元测试

```shell
python3.11 -m unittest tests/compile/uc/test_al_compile_uc.py

python3.10 -m unittest discover tests
python3.10 -m unittest discover tests/compile/uc
```

### 构建包上传包到PyPI
```shell
python3.11 setup.py sdist bdist_wheel
python3.11 -m twine upload dist/*
```

### 运行示例
```shell
python3.10 examples/demo.py
python3.10 examples/bug_11741.py
python3.10 examples/bug_11768.py
python3.10 examples/bug_11775.py
python3.10 examples/bug_11779.py
python3.10 examples/xq_14941.py
```

### 安装本地包
> 在开发过程中，你可以通过 pip install -e . 将包以“可编辑模式”安装到本地环境
```shell
pip install -e .
```

```shell
pip install tools3
which tools3-cli
```

```shell
pip install allure-pytest
brew install allure
allure serve allure-results
```