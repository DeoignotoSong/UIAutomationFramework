from Core.Decorator import test_scenario
from ..TestCases.enter_home import enter_home
from ..TestCases.my_info_edit import my_info_edit
from ..TestCases.user_login import user_login
from ..TestCases.my_sign import my_sign
from ..TestCases.if_login_then_user_logout import if_login_then_user_logout
from ..TestCases.my_info_password_update import my_info_password_update
from ..TestCases.my_info_email_update import my_info_email_update


@test_scenario()
def UserInfoEdit(*args, **kwargs):
    """
    用户资料编辑
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
    # 签到
    my_sign(*args, **kwargs)
    # 我的页面-编辑
    my_info_edit(*args, **kwargs)
    # 邮箱变更
    # my_info_email_update(*args, **kwargs)
    # 修改密码
    # my_info_password_update(*args, **kwargs)
    # 次登录
    # user_login(*args, **kwargs)
