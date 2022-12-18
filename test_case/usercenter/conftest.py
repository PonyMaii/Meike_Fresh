# 获取短信验证码
from utils.my_logging import logger
from utils.mysql_util import db
import time

# 获取验证码
def get_code(mobile):
    sql = "select code from users_verifycode where mobile = '%s' order by id desc limit 1" % mobile
    result = db.select_db_one(sql)
    logger.info(f'sql执行结果：{result}')
    return result['code']


# 删除用户
def delete_user(mobile):
    sql = "delete from users_userprofile where mobile = '%s';" % mobile
    result = db.execute_db(sql)
    logger.info(f'sql执行结果：{result}')


# 删除用户验证码
def delete_code(mobile):
    sql = "delete from users_verifycode where mobile = '%s';" % mobile
    result = db.execute_db(sql)
    logger.info(f'sql执行结果：{result}')

# 修改用户验证码超时
def update_code(mobile):
    sql = "UPDATE users_verifycode SET add_time = '{}' WHERE mobile = '{}';".format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time() - 3600)) , mobile)
    result = db.execute_db(sql)
    logger.info(f'sql执行结果:{result}')

def get_shop_cart_num(username, good_id):
    # 查询UID
    id = user_id(username)
    sql = "select nums from trade_shoppingcart where user_id = %d and goods_id = %d" % (id, good_id)
    result = db.select_db_one(sql)
    return result['nums']


# 查询userid
def user_id(mobile):
    sql = "select id from users_userprofile where mobile = '%s';" % mobile
    result = db.select_db_one(sql)
    return result['id']
