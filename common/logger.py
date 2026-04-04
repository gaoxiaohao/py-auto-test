import logging
import time
from pathlib import Path

# 获取项目根目录（假设本文件在项目根目录下的 common 或 utils 中，这里做兼容）
def get_project_root():
    """自动定位项目根目录（当前文件向上两级）"""
    return Path(__file__).resolve().parent.parent

BASE_PATH = get_project_root()
LOG_PATH = BASE_PATH / "log"
LOG_PATH.mkdir(exist_ok=True)  # 自动创建目录，exist_ok=True 避免异常


class Logger:
    """
    日志类，支持同时输出到控制台和文件，按天分割日志文件
    使用单例模式避免重复添加 handler
    """
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, log_name="auto_test", log_level=logging.INFO, console_level=logging.INFO):
        # 内置函数，用于判断一个对象是否具有指定的属性或者方法，有返回true，没有返回false
        # 首次执行init方法，没有self._initialized，返回false，继续执行后续的代码；二次执行init方法，self._initialized = True，直接return
        # 防止重复调用
        if hasattr(self, '_initialized'):
            return
        self._initialized = True
        # 获取logging对象并赋值给logger
        self.logger = logging.getLogger(log_name)
        # 设置日志级别
        self.logger.setLevel(log_level)
        # 如果已经有 handler，不再重复添加（防止多次导入导致日志重复）
        if self.logger.handlers:
            return

        # 日志格式
        formatter = logging.Formatter(
            '[%(asctime)s][%(filename)s %(lineno)d][%(levelname)s]: %(message)s'
        )

        # 文件 handler
        log_filename = LOG_PATH / f"{time.strftime('%Y%m%d')}.log"
        file_handler = logging.FileHandler(log_filename, mode='a', encoding='utf-8')
        file_handler.setLevel(log_level)
        file_handler.setFormatter(formatter)

        # 控制台 handler
        console_handler = logging.StreamHandler()
        console_handler.setLevel(console_level)
        console_handler.setFormatter(formatter)

        self.logger.addHandler(file_handler)
        self.logger.addHandler(console_handler)

    def get_logger(self):
        return self.logger


# 返回logging的实例对象
logger = Logger().get_logger()
