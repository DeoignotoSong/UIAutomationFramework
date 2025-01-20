from Core.Decorator import test_case
from Core.Base import Base
from Projects.Android.Pages.Common.QuestionDetailPage import QuestionDetailPage
from Projects.Android.Pages.Common.QuestionReplyingPage import QuestionReplyingPage
from Projects.Android.Pages.Common.AppCommonDialogPage import AppCommonDialogPage


@test_case
def question_reply(*args, **kwargs):
    """
    问答详细页面-问答回复
    :param args:
    :param kwargs:
    :return:
    """
    project = args[0]  # type: Base
    question_detail = QuestionDetailPage(project)
    # 立即回答
    question_detail.click_answer_question_now_button_action()
    question_replying = QuestionReplyingPage(project)
    reply_content = '自动化测试自动回复！！！！'
    # 输入回答内容
    question_replying.answer_input.send_keys(reply_content)
    # 点击发布
    question_replying.click_next_button_action()
    # 进入回复详情页
    reply_content_xpath = "//*[@text='{}']".format(reply_content)
    # 等待loading对话框消失
    app_common_dialog = AppCommonDialogPage(project)
    # 等待元素出现
    project.wait_until(reply_content_xpath)
    project.driver.find_element_by_xpath(reply_content_xpath).click()
    return {
        'reply_content': reply_content
    }
