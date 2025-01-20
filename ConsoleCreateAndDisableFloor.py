# -*- encoding: utf-8 -*-
import time
from Core.Decorator import test_scenario
from Core.Global import Data,DataBaseName

from Projects.PC.TestCases.Console.Common.console_login import console_login
from Projects.PC.TestCases.Console.Admin.console_create_floor_column import console_create_floor_column
from Projects.PC.TestCases.Console.Admin.console_edit_floor_column import console_edit_floor_column
from Projects.PC.TestCases.Console.Admin.console_disable_floor_column import console_disable_floor_column

from DB.MysqlDB import MysqlDB
from DB.MongoDB import MongoDB
@test_scenario()
def ConsoleCreateAndDisableFloor(*args, **kwargs):
    """
    后台登录-创建楼层栏目-编辑楼层栏目-禁用楼层栏目
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
    data = Data.TEST_DATA['ConsoleCreateAndDisableFloor']
    # 后台登录
    cl = console_login(*args, **kwargs)
    try:
        # 创建楼层栏目
        ccfc = console_create_floor_column(*args, **kwargs)
        # 编辑楼层栏目
        cefc = console_edit_floor_column(*args, **kwargs)
        # 禁用楼层栏目
        cdfc = console_disable_floor_column(*args, **kwargs)
    finally:
        reset_sql = 'UPDATE '+DataBaseName.DATABASE_NAME['dxz_lan']+'.dxz_system_floor_column SET floor_column_name="{0}", is_enable=0 WHERE floor_name="{1}" AND address_name="{2}" AND floor_column_name IN ("{3}", "{4}")'

        reset_sql = reset_sql.format('UI楼层栏目重置' + str(time.time()).split('.')[0],

                                     data['console_create_floor_column']['In']['floor_name'],
                                     data['console_create_floor_column']['In']['address'],
                                     data['console_create_floor_column']['In']['floor_column_name'],
                                     data['console_edit_floor_column']['In']['edit_floor_column_name'])
        mysql.execute_modify_sql(reset_sql)
