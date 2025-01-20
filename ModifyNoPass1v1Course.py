# -*- encoding: utf-8 -*-

from Core.Decorator import test_scenario
from Core.Assert import Assert
from Core.Global import Data
from Projects.PC.TestCases.User.Common.go_to_user_center import go_to_user_center
from Projects.PC.TestCases.User.Common.user_login import user_login
from Projects.PC.TestCases.User.Teacher.teacher_create_1v1_course import teacher_create_1v1_course
from Projects.PC.TestCases.Console.Common.console_login import console_login
from Projects.PC.TestCases.Console.Admin.console_no_pass_1v1_course import console_no_pass_1v1_course
from Projects.PC.TestCases.User.Teacher.teacher_edit_1v1_course import teacher_edit_1v1_course
from Projects.PC.Base.ProjectHandler import *
from DB.MysqlDB import MysqlDB
from DB.MongoDB import MongoDB


@test_scenario()
def ModifyNoPass1v1Course(*args, **kwargs):
    """
    讲师登录-发布1对1直播课-后台登录-1对1课审核不通过-讲师查看审核未通过直播1对1
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
    data = Data.TEST_DATA['ModifyNoPass1v1Course']
    # 用户登录
    ul = user_login(*args, **kwargs)
    try:
        # 进入我的中心页
        gtuc = go_to_user_center(*args, **kwargs)
        # 用户发布直播课
        ucvc = teacher_create_1v1_course(*args, **kwargs)
        # 后台登录
        cl = console_login(*args, **kwargs)
        # 直播课审核不通过
        cnpvc = console_no_pass_1v1_course(*args, **kwargs)
        Assert.is_equal(data['teacher_create_1v1_course']['In']['product_name'], cnpvc['review_detail_product_name'])
        Assert.is_equal(data['teacher_create_1v1_course']['In']['sub_product_name'], cnpvc['review_detail_sub_product_name'])
        Assert.is_equal(data['teacher_create_1v1_course']['In']['first_item_name'], cnpvc['review_detail_first_item_name'])
        Assert.is_equal(data['teacher_create_1v1_course']['In']['first_question'], cnpvc['review_detail_first_question'])
        Assert.is_equal(data['teacher_create_1v1_course']['In']['first_answer'], cnpvc['review_detail_first_answer'])
        # 编辑未通过直播1对1
        tepc = teacher_edit_1v1_course(*args, **kwargs)
    finally:
        # 重置讲师日历表信息
        reset_calendar(mysql, data['user_login']['In']['mobile'])
