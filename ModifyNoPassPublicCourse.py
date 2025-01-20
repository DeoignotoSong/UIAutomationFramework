# -*- encoding: utf-8 -*-

from Core.Decorator import test_scenario
from Core.Assert import Assert
from Core.Global import Data
from Projects.PC.TestCases.User.Common.go_to_user_center import go_to_user_center
from Projects.PC.TestCases.User.Common.user_login import user_login
from Projects.PC.TestCases.User.Teacher.teacher_create_public_class import teacher_create_public_class
from Projects.PC.TestCases.Console.Common.console_login import console_login
from Projects.PC.TestCases.Console.Admin.console_no_pass_public_class import console_no_pass_public_class
from Projects.PC.TestCases.User.Teacher.teacher_edit_public_class import teacher_edit_public_class
from Projects.PC.Base.ProjectHandler import *
from DB.MysqlDB import MysqlDB
from DB.MongoDB import MongoDB


@test_scenario()
def ModifyNoPassPublicCourse(*args, **kwargs):
    """
    讲师登录-发布直播讲堂-后台登录-直播讲堂审核不通过-编辑未通过直播讲堂
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
    data = Data.TEST_DATA['ModifyNoPassPublicCourse']
    # 用户登录
    ul = user_login(*args, **kwargs)
    try:
        # 进入我的中心页
        gtuc = go_to_user_center(*args, **kwargs)
        # 用户发布直播课
        tcpc = teacher_create_public_class(*args, **kwargs)
        # 后台登录
        cl = console_login(*args, **kwargs)
        # 公开讲堂审核未通过
        cnppc = console_no_pass_public_class(*args, **kwargs)
        Assert.is_equal(data['teacher_create_public_class']['In']['product_name'], cnppc['review_detail_product_name'])
        Assert.is_equal(data['teacher_create_public_class']['In']['sub_product_name'], cnppc['review_detail_sub_product_name'])
        Assert.is_equal(data['teacher_create_public_class']['In']['first_item_name'], cnppc['review_detail_first_item_name'])
        Assert.is_equal(data['teacher_create_public_class']['In']['second_item_name'], cnppc['review_detail_second_item_name'])
        Assert.is_equal(data['teacher_create_public_class']['In']['first_question'], cnppc['review_detail_first_question'])
        Assert.is_equal(data['teacher_create_public_class']['In']['first_answer'], cnppc['review_detail_first_answer'])
        Assert.is_equal(data['teacher_create_public_class']['In']['second_question'], cnppc['review_detail_second_question'])
        Assert.is_equal(data['teacher_create_public_class']['In']['second_answer'], cnppc['review_detail_second_answer'])
        Assert.is_equal(data['teacher_create_public_class']['In']['class_name'], cnppc['review_detail_first_class_name'])
        Assert.is_equal(data['teacher_create_public_class']['In']['price'], cnppc['review_detail_first_class_price'])
        # 编辑未通过公开讲堂
        tepc = teacher_edit_public_class(*args, **kwargs)
    finally:
        # 重置讲师日历表信息
        reset_calendar(mysql, data['user_login']['In']['mobile'])
