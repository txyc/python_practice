import yaml
import json
import os

if __name__ == "__main__":
    data_test = {"name":"Jack","age":25,"job":"teacher"}

    config_dir = os.sep.join([os.path.dirname(__file__), "config"])
    if not os.path.exists(config_dir):
        os.mkdir(config_dir)

    # dict存入yaml文件
    yaml_path = os.sep.join([config_dir,"yamldata.yml"])
    f = open(yaml_path,"w")
    yaml.dump(data_test,f)
    f.close()

    # 从yaml文件中读取数据
    f = open(yaml_path,"r")
    data_test1 = yaml.safe_load(f)
    f.close()
    print(data_test1)

    # dict数据存入json文件
    json_path = os.sep.join([config_dir,"jsondata.json"])
    f = open(json_path,'w')
    json_test = json.dumps(data_test)
    f.write(json_test)
    f.close()
    
    # 从json文件中读取数据
    f = open(json_path,"rb")
    data_test2 = json.loads(f.read())
    f.close()
    print(data_test2)