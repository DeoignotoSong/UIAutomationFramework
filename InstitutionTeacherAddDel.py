# -*- encoding: utf-8 -*-

from Core.Decorator import test_scenario
from Core.Global import Data
from Projects.PC.TestCases.Console.Admin.console_institution_rv_pass import console_institution_rv_pass
from Projects.PC.TestCases.Console.Common.console_login import console_login
from Projects.PC.TestCases.Organization.Institute.institution_register import institution_register
from Projects.PC.TestCases.Organization.Common.organization_login import organization_login
from Projects.PC.TestCases.Organization.Institute.institution_home_review import institution_home_review
from Projects.PC.TestCases.Organization.Institute.ins_add_teacher import ins_add_teacher
from Projects.PC.TestCases.Organization.Institute.ins_import_teacher import ins_import_teacher
from Projects.PC.TestCases.Organization.Institute.ins_del_teacher import ins_del_teacher

from DB.MysqlDB import MysqlDB
from DB.MongoDB import MongoDB


@test_scenario(csv_download=True)
def InstitutionTeacherAddDel(*args, **kwargs):
    """
    机构讲师新增-导入-查询
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
    data = Data.TEST_DATA['InstitutionTeacherAddDel']
    # 用户注册
    ir = institution_register(*args, **kwargs)
    # 用户登录
    ol = organization_login(*args, **kwargs)
    # 输入信息提交审核
    ihr = institution_home_review(*args, **kwargs)
    # 管理后台用户登录
    cl = console_login(*args, **kwargs)
    # 审核通过
    cirp = console_institution_rv_pass(*args, **kwargs)
    # 用户登录
    ol2 = organization_login(*args, **kwargs)
    # 新增讲师
    iat = ins_add_teacher(*args, **kwargs)
    # 删除讲师
    idt = ins_del_teacher(*args, **kwargs)
    # 导入讲师
    iit = ins_import_teacher(*args, **kwargs)
    # 删除讲师
    idt2 = ins_del_teacher(*args, **kwargs)

