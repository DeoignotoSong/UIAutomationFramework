# -*- encoding: utf-8 -*-

from Core.Decorator import test_scenario
from Core.Global import Data
from Projects.PC.TestCases.Console.Admin.console_institution_create import console_institution_create
from Projects.PC.TestCases.Console.Admin.console_institution_review_no2 import console_institution_review_no2
from Projects.PC.TestCases.Console.Common.console_login import console_login

from DB.MysqlDB import MysqlDB
from DB.MongoDB import MongoDB


@test_scenario()
def ConsoleInstitutionCreateNo(*args, **kwargs):
    """
    国内机构后台注册-审核不通过
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
    # 初始化文件
    data = Data.TEST_DATA['ConsoleInstitutionCreateNo']
    # 管理后台用户登录
    cl = console_login(*args, **kwargs)
    # 管理后台用户注册
    cic = console_institution_create(*args, **kwargs)
    # 用户审核不通过
    cirn = console_institution_review_no2(*args, **kwargs)
