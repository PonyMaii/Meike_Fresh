import pymysql

from utils.my_logging import logger
from global_variable import DB


DB_CONF = {
    "host": DB['MYSQL_HOST'],
    "port": int(DB['MYSQL_PORT']),
    "user": DB['MYSQL_USER'],
    "password": DB['MYSQL_PASSWD'],
    "db": DB['MYSQL_DB']
}


class MysqlDb:
    def __init__(self):
        # mysql连接
        self.conn = pymysql.connect(**DB_CONF, autocommit=True)
        self.cur = self.conn.cursor(cursor=pymysql.cursors.DictCursor)

    # 释放资源
    def __del__(self):
        self.cur.close()
        self.conn.close()

    # 查询一条
    def select_db_one(self, sql):
        logger.info(f'执行sql：{sql}')
        self.cur.execute(sql)
        # 获取数据
        result = self.cur.fetchone()
        logger.info(f'sql执行结果：{result}')
        return result

    # 查询多条
    def select_db_all(self, sql):
        logger.info(f'sql执行sql：{sql}')
        self.cur.execute(sql)
        # 获取数据
        result = self.cur.fetchall()
        logger.info(f'执行结果：{result}')
        return result

    def execute_db(self, sql):
        try:
            logger.info(f'执行sql：{sql}')
            self.cur.execute(sql)
            self.conn.commit()
        except Exception as e:
            logger.info("执行sql出错{}".format(e))


db = MysqlDb()
if __name__ == '__main__':
    db = MysqlDb()
    result = db.select_db_one(
        "select code from users_verifycode where mobile = '15397919586' order by id desc limit 1;")
    print(result['code'])
