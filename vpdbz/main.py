#! /usr/bin/env python
"""生成vscode的调试配置。执行后将对应配置复制到launch.json中即可。
"""
import sys
import os
import jstyleson as json
from pprint import pprint

def main():
    cwd = os.getcwd()
    if "python" in sys.argv:
        python_idx = sys.argv.index("python")
    elif "python3" in sys.argv:
        python_idx = sys.argv.index("python3")
    else:
        print("Can't find python or python3 in your command")

    envs = sys.argv[1:python_idx]
    env_dict = {}
    for env in envs:
        key, value = env.split("=")
        env_dict[key] = value

    file_ = sys.argv[python_idx + 1]
    args = sys.argv[python_idx + 2:]
    if os.path.exists('.vscode/launch.json'):
        launch = json.load(open('.vscode/launch.json'))
    else:
        launch = {
            "version": "1.1.0",
            "configurations": []
        }

    config = {
        "name": f"Python: {' '.join(sys.argv[2:])}",
        # 语言类型， 默认就可以
        "type": "python",
        # 应答类型， 默认就可以
        "request": "launch",
        "program": f"{file_}",
        "env": env_dict,
        # 显示控制台，默认用 VScode 自带的，也可以用系统的。
        "console": "integratedTerminal",
        "args": args,
        "cwd": cwd,
        # true 只调试当前 py 文件，默认值; false 也调试引用的模块
        "justMyCode": False,
        # hide special variables and function variables
        "variablePresentation": {
            "all": "hide",
            "protected": "inline"
        }
    }

    launch['configurations'].append(config)
    if not os.path.exists('.vscode'):
        os.makedirs('.vscode')
    with open('.vscode/launch.json', 'w') as f:
        json.dump(launch, f, indent=4)    

if __name__ == "__main__":
    main()
