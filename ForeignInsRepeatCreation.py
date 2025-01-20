# -*- encoding: utf-8 -*-

from Core.Decorator import test_scenario
from Core.Global import Data
from Projects.PC.TestCases.Organization.Institute.foreign_ins_register_ag import foreign_ins_register_ag
from Projects.PC.TestCases.Organization.Institute.institution_register import institution_register
from Projects.PC.TestCases.Organization.Common.organization_login import organization_login
from Projects.PC.TestCases.Organization.Institute.institution_home_review import institution_home_review
from Projects.PC.TestCases.Console.Common.console_login import console_login
from Projects.PC.TestCases.Console.Admin.foreign_cons_ins_edit import foreign_cons_ins_edit

from DB.MysqlDB import MysqlDB
from DB.MongoDB import MongoDB


@test_scenario()
def ForeignInsRepeatCreation(*args, **kwargs):
    """
    海外机构重复注册
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
    data = Data.TEST_DATA['ForeignInsRepeatCreation']
    # 用户注册
    ir = institution_register(*args, **kwargs)
    # 用户登录
    ol = organization_login(*args, **kwargs)
    # 输入信息提交审核
    ihr = institution_home_review(*args, **kwargs)
    # 管理后台登录
    clg = console_login(*args, **kwargs)
    # 补充机构院校信息
    fcie = foreign_cons_ins_edit(*args, **kwargs)
    # 重复用户再次注册
    fira = foreign_ins_register_ag(*args, **kwargs)

