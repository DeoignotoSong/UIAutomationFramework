# -*- encoding: utf-8 -*-

from Core.Decorator import test_scenario
from Core.Assert import Assert
from Core.Global import Data
from Projects.PC.TestCases.User.Common.go_to_user_center import go_to_user_center
from Projects.PC.TestCases.User.Common.user_login import user_login
from Projects.PC.TestCases.User.Teacher.teacher_create_small_class import teacher_create_small_class
from Projects.PC.TestCases.Console.Common.console_login import console_login
from Projects.PC.TestCases.Console.Admin.console_no_pass_small_class import console_no_pass_small_class
from Projects.PC.TestCases.User.Teacher.teacher_check_no_pass_small import teacher_check_no_pass_small
from Projects.PC.Base.ProjectHandler import *
from DB.MysqlDB import MysqlDB
from DB.MongoDB import MongoDB


@test_scenario()
def TeacherCheckNoPassSmall(*args, **kwargs):
    """
    讲师登录-发布直播小班课-后台登录-直播小班课审核不通过-讲师查看审核未通过直播小班课
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
    data = Data.TEST_DATA['TeacherCheckNoPassSmall']
    # 用户登录
    ul = user_login(*args, **kwargs)
    try:
        # 进入我的中心页
        gtuc = go_to_user_center(*args, **kwargs)
        # 用户发布直播小班课
        tcsc = teacher_create_small_class(*args, **kwargs)
        # 后台登录
        cl = console_login(*args, **kwargs)
        # 直播课小班课审核通过
        cnpsc = console_no_pass_small_class(*args, **kwargs)
        Assert.is_equal(data['teacher_create_small_class']['In']['product_name'], cnpsc['review_detail_product_name'])
        Assert.is_equal(data['teacher_create_small_class']['In']['sub_product_name'], cnpsc['review_detail_sub_product_name'])
        Assert.is_equal(data['teacher_create_small_class']['In']['first_item_name'], cnpsc['review_detail_first_item_name'])
        Assert.is_equal(data['teacher_create_small_class']['In']['second_item_name'], cnpsc['review_detail_second_item_name'])
        Assert.is_equal(data['teacher_create_small_class']['In']['first_question'], cnpsc['review_detail_first_question'])
        Assert.is_equal(data['teacher_create_small_class']['In']['first_answer'], cnpsc['review_detail_first_answer'])
        Assert.is_equal(data['teacher_create_small_class']['In']['second_question'], cnpsc['review_detail_second_question'])
        Assert.is_equal(data['teacher_create_small_class']['In']['second_answer'], cnpsc['review_detail_second_answer'])
        Assert.is_equal(data['teacher_create_small_class']['In']['class_name'], cnpsc['review_detail_first_class_name'])
        Assert.is_equal(data['teacher_create_small_class']['In']['price'], cnpsc['review_detail_first_class_price'])
        # 讲师查看未审核通过的直播讲堂
        tcnps = teacher_check_no_pass_small(*args, **kwargs)
        Assert.is_equal(data['teacher_create_small_class']['In']['product_name'], tcnps['product_name'])
        Assert.is_equal(data['teacher_create_small_class']['In']['sub_product_name'], tcnps['sub_product_name'])
    finally:
        # 重置讲师日历表信息
        reset_calendar(mysql, data['user_login']['In']['mobile'])