import configparser
import yaml
from global_variable import BASE_DIR

data_path = BASE_DIR+"/data/test_case_data/testUser"
ini_path = BASE_DIR+"/configs/settings.ini"


class FileRead:
    def __init__(self):
        self.data_path = data_path
        self.ini_path = ini_path

    def read_data(self):
        f = open(self.data_path, encoding="utf8")
        data = yaml.safe_load(f)
        print(data)
        return data

    def read_ini(self):
        config = configparser.ConfigParser()
        config.read(self.ini_path, encoding='utf8')
        return config


base_data = FileRead()

print(base_data.read_ini()['host']['api_sit_url'])