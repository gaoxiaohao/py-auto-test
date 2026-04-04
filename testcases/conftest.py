import json
from pathlib import Path
import pytest
import allure
from common.logger import logger
from common.read_data import data


# 项目根目录（本文件所在目录的父目录）
BASE_PATH = Path(__file__).resolve().parent.parent

def load_yaml_data(yaml_file_name: str) -> dict:
    """
    从 data 目录加载 YAML 文件，返回字典。
    如果文件不存在或解析失败，抛出异常（让测试会话失败）。
    """
    data_file_path = BASE_PATH / "data" / yaml_file_name
    try:
        return data.load_yaml(data_file_path)
    except FileNotFoundError:
        raise FileNotFoundError(f"YAML 数据文件不存在: {data_file_path}")
    except Exception as ex:
        raise RuntimeError(f"加载 YAML 文件 {yaml_file_name} 失败: {ex}")

# 加载基础数据和接口测试数据
api_data = load_yaml_data("api_data.yml")


@allure.step("前置步骤 ==>> 清理数据")
def step_first():
    logger.info("******************************")
    logger.info("前置步骤开始 ==>> 清理数据")


@allure.step("后置步骤 ==>> 清理数据")
def step_last():
    logger.info("后置步骤开始 ==>> 清理数据")



@pytest.fixture(scope="session")
def credit_fixture():
    step_first()
    step_last()
