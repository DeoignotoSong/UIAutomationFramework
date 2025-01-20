from Core.Decorator import test_scenario
from ..TestCases.enter_home import enter_home
from ..TestCases.tearcher_homepage_attention_wechat import tearcher_homepage_attention_wechat
from ..TestCases.user_homepage_attention_wechat import user_homepage_attention_wechat
from ..TestCases.user_logout import user_logout
from ..TestCases.user_login import user_login
from ..TestCases.if_login_then_user_logout import if_login_then_user_logout


@test_scenario()
def UserTearcherWechatAndShare(*args, **kwargs):
    """
    普通用户讲师微聊&分享
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
    nick = '耿裕明'
    kwargs['nick'] = nick
    # 关注讲师并发送微聊
    tearcher_homepage_attention_wechat(*args, **kwargs)
    # 退出登录
    user_logout(*args, **kwargs)
    # 讲师登录
    user_login(*args, **kwargs)
    nick = 'Helloworld'
    kwargs['nick'] = nick
    # 关注普通用户发送微聊
    user_homepage_attention_wechat(*args, **kwargs)
