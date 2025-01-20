# -*- encoding: utf-8 -*-

from Core.Decorator import test_scenario
from Core.Assert import Assert
from Core.Global import Data
from Projects.PC.TestCases.Organization.Common.organization_login import organization_login
from Projects.PC.TestCases.Organization.Institute.institute_create_public_class import institute_create_public_class
from Projects.PC.TestCases.Organization.Institute.institution_home import institution_home
from Projects.PC.TestCases.Console.Common.console_login import console_login
from Projects.PC.TestCases.Console.Admin.console_pass_public_class import console_pass_public_class
from Projects.PC.Base.ProjectHandler import *
from DB.MysqlDB import MysqlDB
from DB.MongoDB import MongoDB


@test_scenario()
def ConsolePassInstitutePublic(*args, **kwargs):
    """
    机构院校主账号登录-发布直播讲堂-后台登录-直播讲堂审核通过
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
    data = Data.TEST_DATA['ConsolePassInstitutePublic']
    # 机构登录
    ol = organization_login(*args, **kwargs)
    # 进入机构院校首页
    inh = institution_home(*args, **kwargs)
    # 发布直播讲堂
    icpc = institute_create_public_class(*args, **kwargs)
    try:
        # 后台登录
        cl = console_login(*args, **kwargs)
        # 直播讲堂审核通过
        cppc = console_pass_public_class(*args, **kwargs)
        Assert.is_equal(data['institute_create_public_class']['In']['product_name'], cppc['review_detail_product_name'])
        Assert.is_equal(data['institute_create_public_class']['In']['sub_product_name'], cppc['review_detail_sub_product_name'])
        Assert.is_equal(data['institute_create_public_class']['In']['first_item_name'], cppc['review_detail_first_item_name'])
        Assert.is_equal(data['institute_create_public_class']['In']['first_question'], cppc['review_detail_first_question'])
        Assert.is_equal(data['institute_create_public_class']['In']['first_answer'], cppc['review_detail_first_answer'])
        Assert.is_equal(data['institute_create_public_class']['In']['class_name'], cppc['review_detail_first_class_name'])
        Assert.is_equal(data['institute_create_public_class']['In']['sale_price'], cppc['review_detail_first_class_price'])
    finally:
        # 重置讲师日历时间
        if 'teacher_info' in icpc.keys():
            reset_calendar(mysql, icpc['teacher_mobile'])

