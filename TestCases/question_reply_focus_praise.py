from Core.Decorator import test_case
from Core.Base import Base
from Projects.Android.Pages.Common.QuestionReplyDetailPage import QuestionReplyDetailPage


@test_case
def question_reply_focus_praise(*args, **kwargs):
    """
    问答详细页面-问答回复-收藏和点赞
    :param args:
    :param kwargs:
    :return:
    """
    project = args[0]  # type: Base
    question_reply_detail = QuestionReplyDetailPage(project)
    project.wait_until(question_reply_detail._reply_comment_focus_button_tag)
    # 点击收藏
    question_reply_detail.click_reply_comment_focus_button_action()
    project.wait_until(question_reply_detail._reply_comment_praise_button_tag)
    # 点赞
    question_reply_detail.click_reply_comment_praise_button_action()
