# -*- encoding: utf-8 -*-
from Core.Decorator import test_scenario
from Core.Assert import Assert
from Core.Global import Data, DataBaseName
from Projects.PC.Base.ProjectHandler import *
from Projects.PC.TestCases.User.Common.go_to_user_center import go_to_user_center
from Projects.PC.TestCases.User.Common.user_login import user_login
from Projects.PC.TestCases.User.Teacher.user_create_activity_course import user_create_activity_course
from Projects.PC.TestCases.Console.Common.console_login import console_login
from Projects.PC.TestCases.Console.Admin.console_pass_activity_course import console_pass_activity_course
from Projects.PC.TestCases.User.Teacher.show_main_page_activity_course import show_main_page_activity_course
from Projects.PC.TestCases.User.User.get_user_main_page_url import get_user_main_page_url
from Projects.PC.TestCases.User.Common.check_main_page_activity import check_main_page_activity

from DB.MysqlDB import MysqlDB
from DB.MongoDB import MongoDB


@test_scenario()
def MainPageCheckActivity(*args, **kwargs):
    """
    讲师登录-发布直播讲座-后台审核通过直播讲座-主页设置展示直播讲座-查看讲师主页直播讲座
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
    data = Data.TEST_DATA['MainPageCheckActivity']
    # 用户登录
    ul = user_login(*args, **kwargs)
    try:
        # 进入我的中心页
        gtuc = go_to_user_center(*args, **kwargs)
        # 用户发布直播讲座
        ucac = user_create_activity_course(*args, **kwargs)
        # 后台登录
        cl = console_login(*args, **kwargs)
        # 直播讲座审核通过
        cpac = console_pass_activity_course(*args, **kwargs)
        Assert.is_equal(data['user_create_activity_course']['In']['product_name'], cpac['review_detail_product_name'])
        Assert.is_equal(data['user_create_activity_course']['In']['sub_product_name'], cpac['review_detail_sub_product_name'])
        Assert.is_equal(data['user_create_activity_course']['In']['first_item_name'], cpac['review_detail_first_item_name'])
        Assert.is_equal(data['user_create_activity_course']['In']['first_question'], cpac['review_detail_first_question'])
        Assert.is_equal(data['user_create_activity_course']['In']['first_answer'], cpac['review_detail_first_answer'])
        # 主页设置展示直播讲座导航
        smpac = show_main_page_activity_course(*args, **kwargs)
        # 获取主页地址
        gumpr = get_user_main_page_url(*args, **kwargs)
        project.wait(120)
        # 查看讲师主页直播讲座课程
        cmpa = check_main_page_activity(*args, **kwargs)
        Assert.is_equal(data['user_create_activity_course']['In']['product_name'], cmpa['first_activity_project_name'])
    finally:
        # 重置讲师日历表信息
        user_id = reset_calendar(mysql, data['user_login']['In']['mobile'])
        #  重置主页设置
        reset_page_settings_sql = 'UPDATE '+DataBaseName.DATABASE_NAME['dxz_lan']+'.dxz_user_homepage_column SET is_deleted = 1 WHERE user_id = "{user_id}" AND column_code = "c_freelive"'.format(user_id=user_id)

        log(reset_page_settings_sql)
        mysql.execute_modify_sql(reset_page_settings_sql)
