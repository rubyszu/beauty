
```sh

asuna
    - config		//build api parameter
    - common     //公共方法
        - api_operation.py  //封装api方法
        - cmdline_args.py    // Command Line Arguments
        - configuration.py   //Base Url
        - find_node.py      //recursive query in dict
        - generate_random.py    //generate random data
        - load_file.py     //load json or yaml file to dict

    - cases		// 测试用例集合
    	- {api module}
    - test_data    //测试数据文件
        - {branch}  
            - {product}
                - {api module}
    - run
    	- run_test_case.py    //运行测试用例

# To install the library, run the following
python setup.py install

#run testcase
python run/run_test_case.py --env=development --branch=master --case_path={specified case folder} --pattern={rule to match file name}


```