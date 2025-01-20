# -*- encoding: utf-8 -*-

from Core.Decorator import test_scenario
from Core.Assert import Assert
from Core.Global import Data
from Projects.PC.TestCases.User.Common.go_to_user_center import go_to_user_center
from Projects.PC.TestCases.User.Common.user_login import user_login
from Projects.PC.TestCases.User.Teacher.teacher_create_1v1_course import teacher_create_1v1_course
from Projects.PC.TestCases.Console.Common.console_login import console_login
from Projects.PC.TestCases.Console.Admin.console_pass_1v1_course import console_pass_1v1_course
from Projects.PC.TestCases.Console.Admin.console_lower_live_course import console_lower_live_course
from Projects.PC.TestCases.Console.Admin.console_upper_live_course import console_upper_live_course
from Projects.PC.Base.ProjectHandler import *
from DB.MysqlDB import MysqlDB
from DB.MongoDB import MongoDB


@test_scenario()
def ConsoleUpperAndLower1v1(*args, **kwargs):
    """
    讲师登录-发布1对1直播课-后台登录-1对1课审核通过-讲师下架直播1对1课-讲师上架直播1对1课
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
    # test_data列表
    data = Data.TEST_DATA['ConsoleUpperAndLower1v1']
    # 用户登录
    ul = user_login(*args, **kwargs)
    try:
        # 进入我的中心页
        gtuc = go_to_user_center(*args, **kwargs)
        # 用户发布直播课
        ucvc = teacher_create_1v1_course(*args, **kwargs)
        # 后台登录
        cl = console_login(*args, **kwargs)
        # 直播课审核通过
        cpvc = console_pass_1v1_course(*args, **kwargs)
        Assert.is_containing(ucvc['category'], cpvc['review_detail_category'])
        Assert.is_containing(data['teacher_create_1v1_course']['In']['product_name'], cpvc['review_detail_product_name'])
        Assert.is_containing(data['teacher_create_1v1_course']['In']['sub_product_name'], cpvc['review_detail_sub_product_name'])
        Assert.is_containing(data['teacher_create_1v1_course']['In']['first_item_name'], cpvc['review_detail_first_item_name'])
        Assert.is_containing(data['teacher_create_1v1_course']['In']['first_question'], cpvc['review_detail_first_question'])
        Assert.is_containing(data['teacher_create_1v1_course']['In']['first_answer'], cpvc['review_detail_first_answer'])
        # 下架直播小班课
        cllc = console_lower_live_course(*args, **kwargs)
        # 上架直播小班课
        culc = console_upper_live_course(*args, **kwargs)
    finally:
        # 重置讲师日历表信息
        reset_calendar(mysql, data['user_login']['In']['mobile'])
