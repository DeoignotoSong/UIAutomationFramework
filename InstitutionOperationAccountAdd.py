# -*- encoding: utf-8 -*-

from Core.Decorator import test_scenario
from Core.Global import Data
from Projects.PC.TestCases.Console.Common.console_login import console_login
from Projects.PC.TestCases.Console.Admin.cons_ins_sub_inq import cons_ins_sub_inq
from Projects.PC.TestCases.Organization.Common.organization_login import organization_login
from Projects.PC.TestCases.Organization.Institute.ins_invalid_login import ins_invalid_login
from Projects.PC.TestCases.Organization.Institute.ins_operation_account_add import ins_operation_account_add
from Projects.PC.TestCases.Organization.Institute.ins_operation_account_dle import ins_operation_account_dle

from DB.MysqlDB import MysqlDB
from DB.MongoDB import MongoDB


@test_scenario()
def InstitutionOperationAccountAdd(*args, **kwargs):
    """
    机构新增子账号-删除
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
    data = Data.TEST_DATA['InstitutionOperationAccountAdd']
    # 用户登录
    ol = organization_login(*args, **kwargs)
    # 新增运营账号
    ioaa = ins_operation_account_add(*args, **kwargs)
    # 运营账号登录
    ol2 = organization_login(*args, **kwargs)
    # 主账号登录
    ol3 = organization_login(*args, **kwargs)
    # 删除运营账号
    ioad = ins_operation_account_dle(*args, **kwargs)
    # 使用已删除账号登录
    inil = ins_invalid_login(*args, **kwargs)
    # 管理后台登录
    clg = console_login(*args, **kwargs)
    # 查询已删除的子账号
    cinsi = cons_ins_sub_inq(*args, **kwargs)

