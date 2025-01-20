from Utils.Log import log
from poium import Page, Element


'''
位置选择页面
com.jinjilie.daxuezhang.functions.MainActivity
'''


class QuestionDetailPage:

    def __init__(self, project):
        self.Android = project
        # region Fields
        # 立即回答
        self._answer_question_now_button_tag = "//*[@resource-id='com.jinjilie.daxuezhang.debug:id/answer_question_now_tv']"
        # 回复问答回复button
        self._answer_questtion_reply_button_tag = "//*[@text='安静安静安静安静安静安静就安静安静']/preceding-sibling::android.widget.RelativeLayout[1]/android.widget.ImageView[2]"
        # endregion Fields

    # region Properties
    @property
    def answer_question_now_button(self):
        """
        属性: 立即回答
        :return: 立即回答
        """
        element = None
        try:
            element = self.Android.get_element(self._answer_question_now_button_tag)
        except AttributeError as error:
            log(error)
        return element

    # endregion Properties

    # region Actions
    def click_answer_question_now_button_action(self):
        """
        动作：点击立即回答
        :return: 点击'立即回答'按钮后的页面
        """
        self.Android.click(self.answer_question_now_button)
        return self.Android.get_current_page_source()

    # endregion Actions
