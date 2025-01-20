# -*- encoding: utf-8 -*-

from Core.Decorator import test_scenario
from Core.Global import Data
from Projects.PC.TestCases.Organization.School.school_register import school_register
from Projects.PC.TestCases.Organization.Common.organization_login import organization_login
from Projects.PC.TestCases.Organization.School.school_home_review import school_home_review
from Projects.PC.TestCases.Console.Common.console_login import console_login
from Projects.PC.TestCases.Console.Admin.console_school_list_edit import console_school_list_edit
from Projects.PC.TestCases.Console.Admin.console_school_review_no import console_school_review_no

from DB.MysqlDB import MysqlDB
from DB.MongoDB import MongoDB


@test_scenario()
def FoSchoolRegisterNoPass(*args, **kwargs):
    """
    海外院校注册-提交审核信息-后台登录-院校信息完善-院校审核不通过
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
    data = Data.TEST_DATA['FoSchoolRegisterNoPass']
    # 院校注册
    sr = school_register(*args, **kwargs)
    # 院校登录
    ol = organization_login(*args, **kwargs)
    # 输入信息提交审核
    shr = school_home_review(*args, **kwargs)
    # 管理后台用户登录
    cl = console_login(*args, **kwargs)
    # 补全院校机构信息
    cile = console_school_list_edit(*args, **kwargs)
    # 院校审核不通过
    cinrn = console_school_review_no(*args, **kwargs)
