# -*- encoding: utf-8 -*-

from Core.Decorator import test_scenario
from Core.Global import Data
from Core.Assert import Assert
from Projects.PC.TestCases.User.Common.user_register import user_register
from Projects.PC.TestCases.User.Common.go_to_user_center import go_to_user_center
from Projects.PC.TestCases.User.User.user_modify_info import user_modify_info
from Projects.PC.TestCases.User.User.get_user_main_page_url import get_user_main_page_url
from Projects.PC.TestCases.User.Common.user_logout import user_logout
from Projects.PC.TestCases.User.Common.user_main_page_focus_user import user_main_page_focus_user
from Projects.PC.TestCases.User.Common.check_my_focus import check_my_focus

from DB.MysqlDB import MysqlDB
from DB.MongoDB import MongoDB


@test_scenario()
def UserFocusAndCheckInfo(*args, **kwargs):
    """
    用户1注册-修改个人信息-获取个人主页地址-用户1登出-用户2注册-查看用户2主页信息-关注用户2-查看我的关注
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
    data = Data.TEST_DATA['UserFocusAndCheckInfo']
    # 用户1注册
    ur = user_register(*args, **kwargs)
    # 进入我的中心页
    gtuc = go_to_user_center(*args, **kwargs)
    # 用户修改个人信息
    umi = user_modify_info(*args, **kwargs)
    # 获取个人主页地址
    gumpu = get_user_main_page_url(*args, **kwargs)
    Assert.is_containing(gumpu['user_name'][0:-3], data['user_modify_info']['In']['nick'])
    # 用户1登出
    ulo = user_logout(*args, **kwargs)
    # 用户2注册
    ur2 = user_register(*args, **kwargs)
    # 用户主页关注用户
    umpfu = user_main_page_focus_user(*args, **kwargs)
    Assert.is_containing(data['user_modify_info']['In']['nick'], umpfu['user_name'])
    # 查看我的关注
    cyf = check_my_focus(*args, **kwargs)
    Assert.is_equal(data['user_modify_info']['In']['nick'], cyf['focus_first_user_name'])
    Assert.is_containing(umpfu['fans_number_after'], cyf['focus_first_fans_number'])

