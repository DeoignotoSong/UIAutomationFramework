# -*- encoding: utf-8 -*-
from Core.Decorator import test_scenario
from Core.Global import Data
from Core.Assert import Assert
from Projects.PC.Base.ProjectHandler import *
from Projects.PC.TestCases.User.Common.user_login import user_login
from Projects.PC.TestCases.User.Common.go_to_user_center import go_to_user_center
from Projects.PC.TestCases.User.Teacher.teacher_modify_info import teacher_modify_info
from Projects.PC.TestCases.Console.Common.console_login import console_login
from Projects.PC.TestCases.Console.Admin.console_check_teacher_info import console_check_teacher_info
from DB.MysqlDB import MysqlDB
from DB.MongoDB import MongoDB


@test_scenario()
def TeacherModifyInfo(*args, **kwargs):
    """
    讲师登录-进入我的中心页-修改个人信息-后台登录-后台查看用户信息
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
    data = Data.TEST_DATA['TeacherModifyInfo']
    # 用户登录
    ul = user_login(*args, **kwargs)
    try:
        # 进入我的中心页
        gtuc = go_to_user_center(*args, **kwargs)
        # 用户修改个人信息
        umi = teacher_modify_info(*args, **kwargs)
        # 后台登录
        cl = console_login(*args, **kwargs)
        # 后台查看用户信息
        ccui = console_check_teacher_info(*args, **kwargs)
        Assert.is_containing(data['teacher_modify_info']['In']['nick'], ccui['nick'])
    finally:
        # 重置用户信息DB
        mobile_cipher = parse_encrypt_base64(mysql, data['user_login']['In']['mobile'])
        reset_sql = 'UPDATE '+DataBaseName.DATABASE_NAME['dxz_lan']+'.dxz_user SET nick = "我是讲师", avatar = "http://dxz-prod-1252753627.cos.ap-beijing.myqcloud.com/resource/img/sys/base/defaulthead/88add77ff9431d2c8d1710cbfb8ed16f.png", address = "", ' \
                    'country_code = "-1", country_name = "", country_name_en = "", city_id = "-1", city_name = "", region_id = "-1", region_name = "", school = "", profession = "", labels = "", main_field_labels = "[' \
                    '70562]", description = "", label_lv1 = "-1" WHERE mobile_cipher = "{}"'.format(mobile_cipher)
        log(reset_sql)
        mysql.execute_modify_sql(reset_sql)
