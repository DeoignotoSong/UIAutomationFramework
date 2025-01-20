# -*- encoding: utf-8 -*-

from Core.Decorator import test_scenario
from Core.Global import Data
from Projects.PC.TestCases.Console.Admin.console_institution_rv_pass import console_institution_rv_pass
from Projects.PC.TestCases.Console.Common.console_login import console_login
from Projects.PC.TestCases.Organization.Institute.institution_register import institution_register
from Projects.PC.TestCases.Organization.Common.organization_login import organization_login
from Projects.PC.TestCases.Organization.Institute.ins_reset_password import ins_reset_password
from Projects.PC.TestCases.Organization.Institute.ins_bind_bank_card import ins_bind_bank_card
from Projects.PC.TestCases.Organization.Institute.institution_home_review import institution_home_review

from DB.MysqlDB import MysqlDB
from DB.MongoDB import MongoDB


@test_scenario()
def InstitutionAccountSecurityInfo(*args, **kwargs):
    """
    修改机构密码-绑定银行卡-解除绑定银行卡
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
    data = Data.TEST_DATA['InstitutionAccountSecurityInfo']
    # 机构注册
    ir = institution_register(*args, **kwargs)
    # 机构登录
    ol = organization_login(*args, **kwargs)
    # 输入信息提交审核
    ihr = institution_home_review(*args, **kwargs)
    # 管理后台用户登录
    cl = console_login(*args, **kwargs)
    # 审核通过
    cirp = console_institution_rv_pass(*args, **kwargs)
    # 机构登录
    ol2 = organization_login(*args, **kwargs)
    # 修改密码
    irp = ins_reset_password(*args, **kwargs)
    # 修改密码后登录
    ol3 = organization_login(*args, **kwargs)
    # 绑定银行卡-解除绑定
    inbbc = ins_bind_bank_card(*args, **kwargs)

