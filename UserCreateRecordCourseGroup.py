# -*- encoding: utf-8 -*-

from Core.Decorator import test_scenario
from Core.Assert import Assert
from Core.Global import Data
from Projects.PC.TestCases.User.Common.go_to_user_center import go_to_user_center
from Projects.PC.TestCases.User.Common.user_login import user_login
from Projects.PC.TestCases.User.Teacher.user_create_record_course import user_create_record_course
from Projects.PC.TestCases.Console.Common.console_login import console_login
from Projects.PC.TestCases.Console.Admin.console_pass_record_course import console_pass_record_course
from Projects.PC.TestCases.User.Teacher.user_create_record_group import user_create_record_group
from Projects.PC.TestCases.Common.record_course_video_parsing import record_course_video_parsing

from DB.MysqlDB import MysqlDB
from DB.MongoDB import MongoDB


@test_scenario()
def UserCreateRecordCourseGroup(*args, **kwargs):
    """
    登录-创建录播课-录播课审核通过-创建学友群
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
    data = Data.TEST_DATA['UserCreateRecordCourseGroup']
    # 用户登录
    ul = user_login(*args, **kwargs)
    # 进入我的中心页
    gtuc = go_to_user_center(*args, **kwargs)
    # 用户发布录播课
    ucrc = user_create_record_course(*args, **kwargs)
    # 等待视频解析
    rcp = record_course_video_parsing(*args, **kwargs)
    # 后台登录
    cl = console_login(*args, **kwargs)
    # 录播课审核通过
    cprc = console_pass_record_course(*args, **kwargs)
    Assert.is_containing(data['user_create_record_course']['In']['product_name'], cprc['review_detail_product_name'])
    Assert.is_equal(data['user_create_record_course']['In']['sub_product_name'], cprc['review_detail_sub_product_name'])
    Assert.is_containing(data['user_create_record_course']['In']['price'], cprc['review_detail_price'])
    Assert.is_equal(data['user_create_record_course']['In']['keywords'], cprc['review_detail_keywords'])
    Assert.is_equal(data['user_create_record_course']['In']['first_question'], cprc['review_detail_first_question'])
    Assert.is_equal(data['user_create_record_course']['In']['first_answer'], cprc['review_detail_first_answer'])
    Assert.is_equal(data['user_create_record_course']['In']['first_item_name'], cprc['review_detail_first_item_name'])
    Assert.is_containing(data['user_create_record_course']['In']['first_item_video'].split('/')[-1].split('.')[0], cprc['review_detail_first_item_video'])
    # 创建学友群
    ucrg = user_create_record_group(*args, **kwargs)

