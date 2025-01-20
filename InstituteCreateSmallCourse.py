# -*- encoding: utf-8 -*-

from Core.Decorator import test_scenario
from Core.Global import Data
from Projects.PC.TestCases.Organization.Common.organization_login import organization_login
from Projects.PC.TestCases.Organization.Institute.institution_home import institution_home
from Projects.PC.TestCases.Organization.Institute.institute_create_small_class import institute_create_small_class
from Projects.PC.Base.ProjectHandler import *
from DB.MysqlDB import MysqlDB
from DB.MongoDB import MongoDB


@test_scenario()
def InstituteCreateSmallCourse(*args, **kwargs):
    """
    机构院校主账号登录-发布直播小班课
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
    data = Data.TEST_DATA['InstituteCreateSmallCourse']
    # 机构登录
    ol = organization_login(*args, **kwargs)
    # 进入机构院校首页
    inh = institution_home(*args, **kwargs)
    # 发布直播讲堂
    icsc = institute_create_small_class(*args, **kwargs)
    # 重置讲师日历时间
    if 'teacher_info' in icsc.keys():
        reset_calendar(mysql, icsc['teacher_mobile'])
