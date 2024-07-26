# vpdbz

为vscode生成Python调试配置生成器

## 安装
```shell
pip install vpdbz
```

## 命令行工具

使用`Python`命令行生成`VSCode`调试配置。

只需在`Python`命令前加上`vpdbz`，它就能自动生成`VSCode`的调试配置文件。它会正确解析环境变量和参数列表。

例如：

```shell
vpdbz CUDA_VISIBLE_DEVICES=1,2 python train.py --batch-size 16 --lr 1e-4
```

它会在`.vscode/launch.json`中生成调试配置。然后你可以通过点击相应的按钮来调试你的`Python`文件。

```shell

{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python: python train.py --batch-size 16 --lr 1e-4",
            "type": "python",
            "request": "launch",
            "program": "train.py",
            "env": {
                "CUDA_VISIBLE_DEVICES": "1,2"
            },
            "console": "integratedTerminal",
            "args": [
                "--batch-size",
                "16",
                "--lr",
                "1e-4"
            ],
            "cwd": "/home/xxx/demo_project",
            "justMyCode": false,
            "variablePresentation": {
                "all": "hide",
                "protected": "inline"
        }
        }
    ]
}

```
注意：vpdbz命令必须在vscode项目的根文件夹中执行。


## 更新日志

2024.07.17
1. 为vpdbz自动安装依赖项。
2. 处理环境变量。
3. 隐藏特殊变量和函数变量。
4. 调试所有Python文件。