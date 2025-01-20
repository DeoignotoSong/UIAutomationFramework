from Core.Decorator import test_scenario
from ..TestCases.enter_home import enter_home
from ..TestCases.open_class_course import open_class_course
from ..TestCases.my_learning_center import my_learning_center
from ..TestCases.my_evaluate import my_evaluate
from ..TestCases.my_order import my_order
from ..TestCases.user_login import user_login
from ..TestCases.if_login_then_user_logout import if_login_then_user_logout


@test_scenario()
def OpenClassIssueAbout(*args, **kwargs):
    """
    公开课发布与相关操作
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
    # 公开课程购买
    result = open_class_course(*args, **kwargs)
    kwargs['course_name'] = result['course_name']
    # 我的订单
    my_order(*args, **kwargs)
    # 学习中心
    my_learning_center(*args, **kwargs)
    # 我的评价
    my_evaluate(*args, **kwargs)
