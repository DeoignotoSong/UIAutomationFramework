# -*- encoding: utf-8 -*-

from Core.Decorator import test_scenario
from Core.Global import Data
from Core.Assert import Assert
from Projects.PC.TestCases.User.Common.user_register import user_register
from Projects.PC.TestCases.User.Common.go_to_user_center import go_to_user_center
from Projects.PC.TestCases.User.User.get_user_main_page_url import get_user_main_page_url
from Projects.PC.TestCases.User.Common.user_logout import user_logout
from Projects.PC.TestCases.User.Common.user_main_page_focus_user import user_main_page_focus_user
from Projects.PC.TestCases.User.Common.user_call_off_focus import user_call_off_focus

from DB.MysqlDB import MysqlDB
from DB.MongoDB import MongoDB


@test_scenario()
def UserFocusAndCallOffFocus(*args, **kwargs):
    """
    用户1注册-获取个人主页地址-用户1登出-用户2注册-关注用户2-取消关注
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
    data = Data.TEST_DATA['UserFocusAndCallOffFocus']
    # 用户1注册
    ur = user_register(*args, **kwargs)
    # 进入我的中心页
    gtuc = go_to_user_center(*args, **kwargs)
    # 获取个人主页地址
    gumpu = get_user_main_page_url(*args, **kwargs)
    # 用户1登出
    ulo = user_logout(*args, **kwargs)
    # 用户2注册
    ur2 = user_register(*args, **kwargs)
    # 用户主页关注用户
    umpfu = user_main_page_focus_user(*args, **kwargs)
    Assert.is_equal(gumpu['user_name'], umpfu['user_name'][0:6]+'...')
    # 查看我的关注
    ucof = user_call_off_focus(*args, **kwargs)
    Assert.is_equal(gumpu['user_name'], ucof['focus_first_user_name'][0:6]+'...')
    Assert.is_containing(umpfu['fans_number_after'], ucof['focus_first_fans_number'])


