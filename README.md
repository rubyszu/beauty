
```sh

lucky
    - config		// 配置
    	- setting.json     //配置分支
    	- variable_F5001.json      //F5001分支的环境变量
    	- ...
    - cases		// 测试用例
    	- login    //login模块
    	- task     //task模块
    	- ...
    - run
    	- run_test_case.py    //运行测试用例

#运行测试用例
python testcase.py --branch=XXXX


```