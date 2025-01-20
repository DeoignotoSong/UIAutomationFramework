# -*- encoding: utf-8 -*-

from Core.Decorator import test_scenario
from Core.Global import Data
from Projects.PC.TestCases.User.Common.go_to_user_center import go_to_user_center
from Projects.PC.TestCases.User.Common.user_login import user_login
from Projects.PC.TestCases.User.Teacher.teacher_create_1v1_course import teacher_create_1v1_course
from Projects.PC.Base.ProjectHandler import *
from DB.MysqlDB import MysqlDB
from DB.MongoDB import MongoDB


@test_scenario()
def TeacherCreate1v1Course(*args, **kwargs):
    """
    讲师登录-发布1对1直播课
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
    data = Data.TEST_DATA['TeacherCreate1v1Course']
    # 用户登录
    ul = user_login(*args, **kwargs)
    try:
        # 进入我的中心页
        gtuc = go_to_user_center(*args, **kwargs)
        # 用户发布直播课
        ucvc = teacher_create_1v1_course(*args, **kwargs)
    finally:
        # 重置讲师日历表信息
        reset_calendar(mysql, data['user_login']['In']['mobile'])
