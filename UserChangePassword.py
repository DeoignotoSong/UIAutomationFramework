# -*- encoding: utf-8 -*-
from Core.Decorator import test_scenario
from Core.Global import Data, DataBaseName
from Projects.PC.Base.ProjectHandler import *
from Projects.PC.TestCases.User.Common.user_register import user_register
from Projects.PC.TestCases.User.Common.go_to_user_center import go_to_user_center
from Projects.PC.TestCases.User.Common.user_change_password import user_change_password
from DB.MysqlDB import MysqlDB
from DB.MongoDB import MongoDB


@test_scenario()
def UserChangePassword(*args, **kwargs):
    """
    用户注册-用户修改密码
    :param args:
        0: ProjectBase
        1: mysql
        2: mongo
    :param kwargs:
    :return:
    """
    project = args[0]  # type: ProjectBase
    mysql = args[1]  # type: MysqlDB
    mongo = args[2]  # type: MongoDB
    data = Data.TEST_DATA['UserChangePassword']
    # 用户注册
    ur = user_register(*args, **kwargs)
    try:
        # 进入我的中心页
        gtuc = go_to_user_center(*args, **kwargs)
        # 修改密码
        ucp = user_change_password(*args, **kwargs)
    finally:
        # 防止server问题，最后数据库重置一遍密码，重置密码: dxz11111111
        mobile_cipher = parse_encrypt_base64(mysql, data['user_register']['In']['mobile'])
        reset_password_sql = 'UPDATE '+DataBaseName.DATABASE_NAME['dxz_lan']+'.dxz_user SET password="1258@ddcf5a4ae085a511f463" WHERE mobile_cipher="{}"'.format(mobile_cipher)

        log(reset_password_sql)
        mysql.execute_modify_sql(reset_password_sql)
