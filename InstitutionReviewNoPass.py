# -*- encoding: utf-8 -*-

from Core.Decorator import test_scenario
from Core.Global import Data
from Projects.PC.TestCases.Console.Admin.console_institution_review_no import console_institution_review_no
from Projects.PC.TestCases.Console.Common.console_login import console_login
from Projects.PC.TestCases.Organization.Institute.institution_register import institution_register
from Projects.PC.TestCases.Organization.Common.organization_login import organization_login
from Projects.PC.TestCases.Organization.Institute.institution_home_review import institution_home_review

from DB.MysqlDB import MysqlDB
from DB.MongoDB import MongoDB


@test_scenario()
def InstitutionReviewNoPass(*args, **kwargs):
    """
    国内机构注册-后台审核不通过
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
    data = Data.TEST_DATA['InstitutionReviewNoPass']
    # 机构注册
    ir = institution_register(*args, **kwargs)
    # 机构登录
    ol = organization_login(*args, **kwargs)
    # 输入信息提交审核
    ihr = institution_home_review(*args, **kwargs)
    # 管理后台用户登录
    cl = console_login(*args, **kwargs)
    # 审核不通过
    cinrn = console_institution_review_no(*args, **kwargs)

