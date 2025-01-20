# -*- encoding: utf-8 -*-

from Core.Decorator import test_scenario
from Core.Assert import Assert
from Core.Global import Data
from Projects.PC.TestCases.User.Common.go_to_user_center import go_to_user_center
from Projects.PC.TestCases.User.Common.user_login import user_login
from Projects.PC.TestCases.User.Teacher.teacher_create_public_class import teacher_create_public_class
from Projects.PC.TestCases.Console.Common.console_login import console_login
from Projects.PC.TestCases.Console.Admin.console_pass_public_class import console_pass_public_class
from Projects.PC.TestCases.User.Teacher.teacher_lower_public_course import teacher_lower_public_course
from Projects.PC.TestCases.User.Teacher.teacher_upper_public_course import teacher_upper_public_course
from Projects.PC.Base.ProjectHandler import *
from DB.MysqlDB import MysqlDB
from DB.MongoDB import MongoDB


@test_scenario()
def TeacherUpperAndLowerPublic(*args, **kwargs):
    """
    讲师登录-发布直播讲堂-后台登录-直播讲堂审核通过-讲师下架直播讲堂-讲师上架直播讲堂
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
    data = Data.TEST_DATA['TeacherUpperAndLowerPublic']
    # 用户登录
    ul = user_login(*args, **kwargs)
    try:
        # 进入我的中心页
        gtuc = go_to_user_center(*args, **kwargs)
        # 用户发布直播课
        tcpc = teacher_create_public_class(*args, **kwargs)
        # 后台登录
        cl = console_login(*args, **kwargs)
        # 公开讲堂审核通过
        cppc = console_pass_public_class(*args, **kwargs)
        Assert.is_equal(data['teacher_create_public_class']['In']['product_name'], cppc['review_detail_product_name'])
        Assert.is_equal(data['teacher_create_public_class']['In']['sub_product_name'], cppc['review_detail_sub_product_name'])
        Assert.is_equal(data['teacher_create_public_class']['In']['first_item_name'], cppc['review_detail_first_item_name'])
        Assert.is_equal(data['teacher_create_public_class']['In']['second_item_name'], cppc['review_detail_second_item_name'])
        Assert.is_equal(data['teacher_create_public_class']['In']['first_question'], cppc['review_detail_first_question'])
        Assert.is_equal(data['teacher_create_public_class']['In']['first_answer'], cppc['review_detail_first_answer'])
        Assert.is_equal(data['teacher_create_public_class']['In']['second_question'], cppc['review_detail_second_question'])
        Assert.is_equal(data['teacher_create_public_class']['In']['second_answer'], cppc['review_detail_second_answer'])
        Assert.is_equal(data['teacher_create_public_class']['In']['class_name'], cppc['review_detail_first_class_name'])
        Assert.is_equal(data['teacher_create_public_class']['In']['price'], cppc['review_detail_first_class_price'])
        # 讲师下架直播讲堂
        tlpc = teacher_lower_public_course(*args, **kwargs)
        Assert.is_equal(data['teacher_create_public_class']['In']['product_name'], tlpc['on_shelf_product_name'])
        Assert.is_equal(data['teacher_create_public_class']['In']['product_name'], tlpc['off_shelf_product_name'])
        # 讲师上架直播讲堂
        tupc = teacher_upper_public_course(*args, **kwargs)
        Assert.is_equal(data['teacher_create_public_class']['In']['product_name'], tupc['off_shelf_product_name'])
        Assert.is_equal(data['teacher_create_public_class']['In']['product_name'], tupc['on_shelf_product_name'])
    finally:
        # 重置讲师日历表信息
        reset_calendar(mysql, data['user_login']['In']['mobile'])
