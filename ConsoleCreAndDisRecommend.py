# -*- encoding: utf-8 -*-
from Core.Decorator import test_scenario
from Core.Global import Data,DataBaseName

from Projects.PC.TestCases.Console.Common.console_login import console_login
from Projects.PC.TestCases.Console.Admin.console_create_recommend_place import console_create_recommend_place
from Projects.PC.TestCases.Console.Admin.console_edit_recommend_place import console_edit_recommend_place
from Projects.PC.TestCases.Console.Admin.console_disable_recommend_place import console_disable_recommend_place

from DB.MysqlDB import MysqlDB
from DB.MongoDB import MongoDB
@test_scenario()
def ConsoleCreAndDisRecommend(*args, **kwargs):
    """
    后台登录-创建推荐位-编辑推荐位-禁用推荐位
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
    data = Data.TEST_DATA['ConsoleCreAndDisRecommend']
    # 后台登录
    cl = console_login(*args, **kwargs)
    try:
        # 创建推荐位
        ccrp = console_create_recommend_place(*args, **kwargs)
        # 编辑推荐位
        cerp = console_edit_recommend_place(*args, **kwargs)
        # 禁用推荐位
        cdrp = console_disable_recommend_place(*args, **kwargs)
    finally:
        reset_sql = 'UPDATE '+DataBaseName.DATABASE_NAME['dxz_lan']+'.dxz_system_recommend_place SET status="1", is_deleted="1" WHERE floor_column_name = "{}" and is_deleted="0"'.format(data['console_create_recommend_place']['In']['floor_column_name'])

        log(reset_sql)
        mysql.execute_modify_sql(reset_sql)
