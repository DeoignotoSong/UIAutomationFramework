# -*- encoding: utf-8 -*-

from Core.Decorator import test_scenario
from Core.Global import Data

from Core.Assert import Assert
from Projects.PC.TestCases.Console.Common.console_login import console_login
from Projects.PC.TestCases.Console.Admin.console_add_abroad_service import console_add_abroad_service
from Projects.PC.TestCases.Console.Admin.console_check_abroad_service import console_check_abroad_service

from DB.MysqlDB import MysqlDB
from DB.MongoDB import MongoDB


@test_scenario()
def ConsoleCheckService(*args, **kwargs):
    """
    后台登录-创建服务-服务管理页面检查
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
    data = Data.TEST_DATA['ConsoleCheckService']
    # 后台登录
    cl = console_login(*args, **kwargs)
    # 创建服务
    ccrp = console_add_abroad_service(*args, **kwargs)
    # 检查服务
    ccsp = console_check_abroad_service(*args, **kwargs)
    Assert.is_containing(ccrp['service_id'], ccsp['abroad_url'])
    Assert.is_equal(ccrp['service_name'], ccsp['servicdetailename'])