from Core.Decorator import test_case
from Core.Base import Base
from Projects.Android.Pages.Common.QuestionReplyDetailPage import QuestionReplyDetailPage


@test_case
def question_answers_reply(*args, **kwargs):
    """
    问答详细页面-问答回复之回复
    :param args:
    :param kwargs:
    :return:
    """
    project = args[0]  # type: Base
    reply_content = kwargs['reply_content']
    reply_icon_xpath = "//*[@text='{}']".format(reply_content)
    project.wait_until_not(reply_icon_xpath)
    project.driver.find_element_by_xpath(reply_icon_xpath).click()
    # 点击回复icon
    question_reply_detail = QuestionReplyDetailPage(project)
    project.wait_until_not(question_reply_detail._reply_comment_button_tag)
    question_reply_detail.click_reply_comment_button_action()
    question_reply_detail.reply_comment_input.send_keys('自动化测试-普通用户-回复')
    # 点击发送
    question_reply_detail.click_reply_comment_send_button_action()
    project.wait_until_not(question_reply_detail._reply_comment_button_tag)
