from configparser import ConfigParser
from pathlib import Path
import yaml

from common.logger import logger


class MyConfigParser(ConfigParser):
    # 重写 configparser 中的 optionxform 函数，解决 .ini 文件中的 键option 自动转为小写的问题
    def __init__(self, defaults=None):
        ConfigParser.__init__(self, defaults=defaults)

    def optionxform(self, optionator):
        return optionator

class ReadFileData:

    @staticmethod
    def load_yaml(file_path):
        logger.info("加载 {} 文件......".format(file_path))
        with open(file_path, encoding='utf-8') as f:
            yml_data = yaml.safe_load(f)
        logger.info("读到数据 ==>>  {} ".format(yml_data))
        return yml_data


    @staticmethod
    def load_ini(file_path,section=None):
        logger.info("加载ini文件:{}".format(file_path))
        config = MyConfigParser()
        config.read(file_path,encoding="utf-8")
        if section is None:
            return config
        else:
            if not config.has_section(section):
                raise KeyError(f"配置文件中不存在section：{section}")
            section_dict = dict(config.items(section))
            logger.info("读取section{}的数据：{}".format(section,section_dict))
            return section_dict

class FileBasePath:
    @staticmethod
    def get_file_base_path():
        return Path(__file__).resolve().parent.parent
