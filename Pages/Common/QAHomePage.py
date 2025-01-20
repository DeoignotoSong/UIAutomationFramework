from Utils.Log import log
from poium import Page, Element


'''
问答首页
com.jinjilie.daxuezhang.functions.MainActivity
'''


class QAHomePage:
    def __init__(self, project):
        self.Android = project
        # region Fields
        # 提问按钮
        self._question_ask_button_tag = "//*[@resource-id='com.jinjilie.daxuezhang.debug:id/questionAsk_tv']"
        # endregion Fields

    # region Properties
    @property
    def question_ask_button(self):
        """
        属性: 提问按钮
        :return: 提问按钮
        """
        element = None
        try:
            element = self.Android.get_element(self._question_ask_button_tag)
        except AttributeError as error:
            log(error)
        return element

    # endregion Properties

    # region Actions
    def click_question_ask_button_action(self):
        """
        动作：点击提问按钮
        :return: 点击'提问按钮'按钮后的页面
        """
        self.Android.click(self.question_ask_button)
        return self.Android.get_current_page_source()

    # endregion Actions
