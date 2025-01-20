from Core.Decorator import test_scenario
from ..TestCases.enter_home import enter_home
from ..TestCases.put_forward_question import put_forward_question
from ..TestCases.user_logout import user_logout
from ..TestCases.user_logout import back_home_page
from ..TestCases.search_question import search_question
from ..TestCases.user_login import user_login
from ..TestCases.question_reply import question_reply
from ..TestCases.question_reply_focus_praise import question_reply_focus_praise
from ..TestCases.question_answers_reply import question_answers_reply
from ..TestCases.if_login_then_user_logout import if_login_then_user_logout


@test_scenario()
def QuestionAndAnswers(*args, **kwargs):
    """
    用户问答操作
    :param args:
    :param kwargs:
    :return:
    """
    # 进入首页
    enter_home(*args, **kwargs)
    # 如果登录则退出
    if_login_then_user_logout(*args, **kwargs)
    # 普通用户登录
    user_login(*args, **kwargs)
    # 进入问答并提出问题
    result = put_forward_question(*args, **kwargs)
    question_title = result['question_title']
    kwargs['question_title'] = question_title
    # 退出登录
    user_logout(*args, **kwargs)
    # 讲师登录
    user_login(*args, **kwargs)
    # 搜索上一步提出的问答
    search_question(*args, **kwargs)
    # 问答回复
    qr_result =question_reply(*args, **kwargs)
    reply_content = qr_result['reply_content']
    kwargs['reply_content'] = reply_content
    # 问答回复-点赞收藏
    question_reply_focus_praise(*args, **kwargs)
    # 返回到首页
    # 退出登录
    user_logout(*args, **kwargs)
    # 用户登录
    user_login(*args, **kwargs)
    # 搜索上一步提出的问答
    search_question(*args, **kwargs)
    # 回复回答内容
    question_answers_reply(*args, **kwargs)
