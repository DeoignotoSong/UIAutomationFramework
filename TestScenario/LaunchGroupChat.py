from Core.Decorator import test_scenario
from ..TestCases.enter_home import enter_home
from ..TestCases.search_user_phone import search_user_phone
from ..TestCases.user_attention import user_attention
from ..TestCases.user_login import user_login
from ..TestCases.user_logout import user_logout
from ..TestCases.launcher_group_chat import launcher_group_chat
from ..TestCases.if_login_then_user_logout import if_login_then_user_logout


@test_scenario()
def LaunchGroupChat(*args, **kwargs):
    """
    发起群聊
    :param args:
    :param kwargs:
    :return:
    """
    # 进入首页
    enter_home(*args, **kwargs)
    # 如果登录则退出
    if_login_then_user_logout(*args, **kwargs)
    # 用户登录
    user_login(*args, **kwargs)
    # 搜索关注指定用户
    search_user_phone(*args, **kwargs)
    # 关注用户
    user_attention(*args, **kwargs)
    # 返回MainActivity
    project = args[0]  # type: ProjectBase
    # 返回微聊首页
    project.back_main_activity_page()
    # 搜索关注指定用户
    search_user_phone(*args, **kwargs)
    # 返回微聊首页
    project.back_main_activity_page()
    # 退出登录
    user_logout(*args, **kwargs)
    # 登录 18129130408
    user_login(*args, **kwargs)
    # 搜索关注指定用户
    search_user_phone(*args, **kwargs)
    # 关注用户
    user_attention(*args, **kwargs)
    # 返回微聊首页
    project.back_main_activity_page()
    # 退出登录
    user_logout(*args, **kwargs)
    # 登录 18118130511
    user_login(*args, **kwargs)
    # 搜索关注指定用户
    search_user_phone(*args, **kwargs)
    # 关注用户
    user_attention(*args, **kwargs)
    # 返回微聊首页
    project.back_main_activity_page()
    # 退出登录
    user_logout(*args, **kwargs)
    # 登录 13610949905
    user_login(*args, **kwargs)
    # 发起群聊
    # launcher_group_chat(*args, **kwargs)
