# -*- encoding: utf-8 -*-

from Core.Decorator import test_scenario
from Core.Assert import Assert
from Core.Global import Data
from Projects.PC.TestCases.Console.Admin.console_institution_rv_pass import console_institution_rv_pass
from Projects.PC.TestCases.Console.Common.console_login import console_login
from Projects.PC.TestCases.Organization.Institute.institution_register import institution_register
from Projects.PC.TestCases.Organization.Common.organization_login import organization_login
from Projects.PC.TestCases.Organization.Institute.institution_home_review import institution_home_review
from Projects.PC.TestCases.Organization.Institute.institution_home import institution_home

from DB.MysqlDB import MysqlDB
from DB.MongoDB import MongoDB


@test_scenario()
def ForeignInsRvPass(*args, **kwargs):
    """
    国外机构注册-信息完善-审核通过-机构用户登录-进入机构院校首页
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
    data = Data.TEST_DATA['ForeignInsRvPass']
    # 用户注册
    ir = institution_register(*args, **kwargs)
    # 用户登录
    ol = organization_login(*args, **kwargs)
    # 输入信息提交审核
    ihr = institution_home_review(*args, **kwargs)
    # 管理后台用户登录
    clg = console_login(*args, **kwargs)
    # 审核通过
    cirp = console_institution_rv_pass(*args, **kwargs)
    # 用户登录
    ol2 = organization_login(*args, **kwargs)
    # 进入机构院校首页
    inh = institution_home(*args, **kwargs)
    Assert.is_equal(data['institution_home_review']['In']['institution_name'], inh['ch_institution_school_name'])
