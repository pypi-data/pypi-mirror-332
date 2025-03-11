<?php
require_once __DIR__ . '/vendor/autoload.php';

use PhpParser\Error;
use PhpParser\ParserFactory;
use PhpParser\Node;
use PhpParser\NodeFinder;
use PhpParser\PrettyPrinter\Standard as PrettyPrinter;

class PhpFileParser
{
    protected $parser;
    protected $printer;
    protected $nodeFinder;

    public function __construct()
    {
        $this->parser = (new ParserFactory)->create(ParserFactory::PREFER_PHP7);
        $this->printer = new PrettyPrinter();
        $this->nodeFinder = new NodeFinder();
    }

    /**
     * 解析指定 PHP 文件，并返回如下结构的数组：
     * {
     *   "file_path": "/path/to/file.php",
     *   "namespace": [ "Foo\\Bar" ],
     *   "uses": [ "Some\\Other\\Namespace", ... ],
     *   "class": "ClassName",
     *   "methods": [
     *      {
     *          "name": "methodName",
     *          "class": "al",
     *          "params": [ { "name": "$param1" }, ... ],
     *          "returns": { "type": "array" },
     *          "code": "注释及方法实现代码"
     *      },
     *      ...
     *   ]
     * }
     *
     * @param string $filePath
     * @return array
     * @throws \Exception
     */
    public function parseFile(string $filePath): array
    {
        if (!file_exists($filePath)) {
            throw new \Exception("File not found: {$filePath}");
        }

        $code = file_get_contents($filePath);

        try {
            $ast = $this->parser->parse($code);
        } catch (Error $e) {
            throw new \Exception("Parse error: " . $e->getMessage());
        }

        $result = [
            'file_path' => $filePath,
            'namespace' => [],
            'uses_namespaces'      => [],
            'class'     => '',
            'methods'   => []
        ];

        // 尝试在命名空间节点中解析
        $namespaceNodes = $this->nodeFinder->findInstanceOf($ast, Node\Stmt\Namespace_::class);

        if (!empty($namespaceNodes)) {
            foreach ($namespaceNodes as $namespaceNode) {
                // 保存当前命名空间（可能有多个）
                $result['namespace'][] = $namespaceNode->name->toString();

                // 在命名空间内查找 use 声明
                $useNodes = $this->nodeFinder->findInstanceOf($namespaceNode->stmts, Node\Stmt\Use_::class);
                foreach ($useNodes as $useNode) {
                    foreach ($useNode->uses as $useUse) {
                        $result['uses_namespaces'][] = $useUse->name->toString();
                    }
                }

                // 在当前命名空间中查找类
                $classNodes = $this->nodeFinder->findInstanceOf($namespaceNode->stmts, Node\Stmt\Class_::class);
                if (!empty($classNodes)) {
                    $classNode = $classNodes[0];
                    $result['class'] = $classNode->name->toString();

                    // 遍历类中的方法
                    foreach ($classNode->getMethods() as $method) {
                        $docComment = $method->getDocComment();
                        $docText = $docComment ? $docComment->getText() : '';
                        $methodCode = $this->printer->prettyPrint([$method]);

                        $methodData = [
                            'name'    => $method->name->toString(),
                            'code'    => $docText . "\n" . $methodCode
                        ];

                        // 获取方法参数
                        foreach ($method->getParams() as $param) {
                            $methodData['params'][] = ['name' => '$' . $param->var->name];
                        }

                        $result['methods'][] = $methodData;
                    }
                }
            }
        } else {
            // 如果没有命名空间，则在全局范围内解析 use 和 class
            $useNodes = $this->nodeFinder->findInstanceOf($ast, Node\Stmt\Use_::class);
            foreach ($useNodes as $useNode) {
                foreach ($useNode->uses as $useUse) {
                    $result['uses_namespaces'][] = $useUse->name->toString();
                }
            }

            $classNodes = $this->nodeFinder->findInstanceOf($ast, Node\Stmt\Class_::class);
            if (!empty($classNodes)) {
                $classNode = $classNodes[0];
                $result['class'] = $classNode->name->toString();

                foreach ($classNode->getMethods() as $method) {
                    $docComment = $method->getDocComment();
                    $docText = $docComment ? $docComment->getText() : '';
                    $methodCode = $this->printer->prettyPrint([$method]);
                    $methodData = [
                        'name'    => $method->name->toString(),
                        'code'    => $docText . "\n" . $methodCode
                    ];

                    foreach ($method->getParams() as $param) {
                        $methodData['params'][] = ['name' => '$' . $param->var->name];
                    }

                    $result['methods'][] = $methodData;
                }
            }
        }

        return $result;
    }

    /**
     * 根据解析结果中的方法信息，提取指定方法的代码，并返回一个完整的代码定义：
     *
     * - 如果解析结果为类文件（存在 'class' 字段），则返回完整的文件代码定义，包括：
     *   - 文件开头的 <?php 声明
     *   - 定义的命名空间（取第一个，如果有多个）
     *   - use 声明的命名空间
     *   - 类的定义（仅包含指定方法的代码）
     *
     * - 如果未指定方法名称，则返回空字符串，防止无意中传递过多代码给大模型。
     *
     * @param array $result parseFile 方法的返回结果
     * @param array $methodNames 指定需要提取的方法名称数组；对于类文件必须指定
     * @return string 拼接后的完整代码定义
     */
    public function getAssembledMethodCode(array $result, array $methodNames = []): string
    {
        // 如果是类文件且未指定方法名称，直接返回空字符串
        if (!empty($result['class']) && empty($methodNames)) {
            return '';
        }
        $methodNames = array_unique($methodNames);
        $assembledMethods = '';
        if (isset($result['methods']) && is_array($result['methods'])) {
            foreach ($result['methods'] as $method) {
                // 对于类文件，只提取用户指定的方法代码
                if (!in_array($method['name'], $methodNames, true)) {
                    continue;
                }
                $assembledMethods .= $method['code'] . "\n\n";
            }
        }

        // 如果是类文件，则组装完整的代码定义
        if (!empty($result['class'])) {
            $code = "<?php\n\n";

            // 添加定义的命名空间（取第一个）
            if (!empty($result['namespace'])) {
                $code .= "namespace " . $result['namespace'][0] . ";\n\n";
            }

            // 添加 use 声明
            if (!empty($result['uses_namespaces'])) {
                foreach ($result['uses_namespaces'] as $use) {
                    $code .= "use " . $use . ";\n";
                }
                $code .= "\n";
            }

            // 组装类的定义，仅包含指定方法的代码
            $code .= "class " . $result['class'] . "\n{\n";
            // 对于每个方法，缩进处理
            $methodLines = explode("\n", trim($assembledMethods));
            foreach ($methodLines as $line) {
                $code .= "    " . $line . "\n";
            }
            $code .= "}\n";

            return $code;
        }

        // 非类文件则直接返回拼接后的方法代码
        return $assembledMethods;
    }

    public function getJsonData($code, $message, $data = []) {
        return json_encode([
            'code' => $code,
            'msg'  => $message,
            'data' => $data
        ]);
    }
}

$parser = new PhpFileParser();
if ($argc < 2) {
    echo $parser->getJsonData(422, 'php_file参数', [
        '$argc' => $argc,
        '$argv' => $argv,
        '/usr/local/Cellar/php@7.3/7.3.33_11/bin/php tools3/data/php-al/PhpFileParser.php php_file'
    ]);
    exit(1);
}

$filePath = $argv[1];
if ($filePath) {
//     $filePath = '/Users/zhaoweijie/work/develop/company/docker-compose-nginx-php/dhb168-local-docker/www/pc-dhb168/Dinghuobao/DhbApi/Controller/Admin/AdminCartController.class.php';
}
try {
    $result = $parser->parseFile($filePath);
    if (isset($result['methods']) && $result['methods']) {
        $resultNew = $result;
        $resultNew['methods'] = [];
        foreach ($result['methods'] as $key => $method) {
            $methodName = $method['name'];
            $methods = [
                '__construct',
                '_initialize',
                $methodName,
            ];

            $code = $parser->getAssembledMethodCode($result, $methods);
            $resultNew['methods'][$methodName] = $result['methods'][$key];
            $resultNew['methods'][$methodName]['code'] = $code;
            if ($methodName == "add") {
//                 print_r($result['methods'][$methodName]);
//                 print_r("===>>");
//                 print_r($code);
//                 exit;
                continue;
            }
        }
    }
    echo $parser->getJsonData(200, 'success', $resultNew);
} catch (\Exception $e) {
    echo $parser->getJsonData(500, $e->getMessage(), [
        'code' => $e->getCode(),
        'file' => $e->getFile(),
        'line' => $e->getLine(),
        'trace' => $e->getTraceAsString(),
    ]);
    exit(1);
}