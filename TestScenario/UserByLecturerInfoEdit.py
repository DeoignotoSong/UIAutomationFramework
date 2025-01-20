from Core.Decorator import test_scenario
from ..TestCases.enter_home import enter_home
from ..TestCases.my_info_edit import my_info_edit
from ..TestCases.user_logout import user_logout
from ..TestCases.user_login import user_login
from ..TestCases.my_sign import my_sign
from ..TestCases.if_login_then_user_logout import if_login_then_user_logout
from ..TestCases.search_teacher import search_teacher


@test_scenario()
def UserByLecturerInfoEdit(*args, **kwargs):
    """
    用户（讲师）资料编辑
    :param args:
    :param kwargs:
    :return:
    """
    # 进入首页
    enter_home(*args, **kwargs)
    # 登录则退出
    if_login_then_user_logout(*args, **kwargs)
    # 用户登录
    user_login(*args, **kwargs)
    # 签到
    my_sign(*args, **kwargs)
    # 我的页面-编辑
    my_info_edit(*args, **kwargs)
    # 退出登录
    user_logout(*args, **kwargs)
    # 再次登录
    user_login(*args, **kwargs)
    search = 'Jenny Tam'
    kwargs['lecturer_name'] = search
    # 主页进入
    search_teacher(*args, **kwargs)
