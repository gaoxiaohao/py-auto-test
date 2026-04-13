import pymysql
from pymysql.cursors import DictCursor
from common.logger import logger
from common.read_data import ReadFileData, FileBasePath


class DataBase:

    def __init__(self, config_section="mysql"):
        self.config = self._get_db_config(config_section)
        self.connection = None
        self.cursor = None

    def _get_db_config(self, section):
        base_path = FileBasePath.get_file_base_path()  # 直接调用静态方法，无需实例化
        ini_path = base_path / 'config' / 'setting.ini'
        db_dict = ReadFileData.load_ini(str(ini_path), section)
        db_dict['MYSQL_PORT'] = int(db_dict['MYSQL_PORT'])
        return db_dict

    def __enter__(self):
        self.connect()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()

    def connect(self):
        try:
            self.connection = pymysql.connect(
                host=self.config.get("MYSQL_HOST"),
                user=self.config.get("MYSQL_USER"),
                port=self.config.get('MYSQL_PORT'),
                password=self.config.get('MYSQL_PASSWD'),
                db=self.config.get('MYSQL_DB'),
                charset='utf8mb4',
                cursorclass=DictCursor
            )
            self.cursor = self.connection.cursor()
            logger.info("数据库连接成功")
        except Exception as e:
            logger.error(f"数据库连接失败：{e}")
            raise

    def close(self):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()
            logger.info("数据库连接已关闭")

    def execute(self, sql, params=None):
        try:
            self.cursor.execute(sql, params)
            self.connection.commit()
            logger.info(f"执行sql：{sql} | 参数 {params}")
            return self.cursor.rowcount
        except Exception as error:
            self.connection.rollback()
            logger.error(f"执行sql失败：{error} | 参数 {params}")
            raise

    def select_one(self, sql, params=None):
        try:
            self.cursor.execute(sql, params)
            result = self.cursor.fetchone()
            logger.debug(f"查询 SQL: {sql} | 参数: {params}")
            return result
        except Exception as error:
            logger.error(f"查询失败: {error} | SQL: {sql}")
            raise

    def select_all(self, sql, params=None):
        try:
            self.cursor.execute(sql, params)
            result = self.cursor.fetchall()
            logger.debug(f"查询 SQL: {sql} | 参数: {params} | 返回行数: {len(result)}")
            return result
        except Exception as error:
            logger.error(f"查询失败: {error} | SQL: {sql}")
            raise

    def execute_many(self, sql, params_list):
        """批量执行 SQL（如批量插入）"""
        try:
            self.cursor.executemany(sql, params_list)
            self.connection.commit()
            logger.debug(f"批量执行 SQL: {sql} | 批次数: {len(params_list)}")
            return self.cursor.rowcount
        except Exception as e:
            self.connection.rollback()
            logger.error(f"批量执行失败: {e}")
            raise


# ================= 便捷函数（模块级别，自动管理连接） =================
def execute_sql(sql, params=None):
    """执行增删改SQL，返回影响行数"""
    with DataBase() as db:
        return db.execute(sql, params)


def fetch_one(sql, params=None):
    """查询单条记录，返回字典"""
    with DataBase() as db:
        return db.select_one(sql, params)


def fetch_all(sql, params=None):
    """查询多条记录，返回字典列表"""
    with DataBase() as db:
        return db.select_all(sql, params)


if __name__ == '__main__':
    # 简单测试连接
    db = DataBase()
    db.connect()
    try:
        db.cursor.execute("SELECT 1")
        result = db.cursor.fetchone()
        logger.info(f"测试查询结果: {result}")
    except Exception as e:
        logger.error(f"查询失败: {e}")
    finally:
        db.close()