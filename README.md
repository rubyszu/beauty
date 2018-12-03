
```sh

asuna
    - config		//build api parameter
    - context  
        - comonse.py
        - context.py

    - core
        - entry.py    //程序入口
        - extension.py    //ext   
        - request.py     
        - response.py    //validate response，save data to context
        - resolve.stage.py  //处理stage
    - docs
        - stage yaml file desc
    - uitl     //工具类
        - cmdline_args.py    // Command Line Arguments
        - dict_util.py  //处理type(dict)
        - http_base.py   //Base Url
        - generate_random.py    //generate random data
        - loader.py     //load json or yaml file to dict
        - replace_str.py   //处理type(str)

    - test_schemas		// 业务场景集合
    	- {api module}
            - {api}
    - test_data    //测试数据文件
        - {branch}  
            - {product}
                - {api module}
    - conftest.py   //pytest配置文件

# To install the library, run the following
python setup.py install

#run testcase
#run all testcase in this director
pytest {test case director} --env=development --branch=master --product=project
#run the testcase file
pytest {test case path} --env=development --branch=master --product=project


```