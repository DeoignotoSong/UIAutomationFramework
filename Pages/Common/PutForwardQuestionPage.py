from Utils.Log import log
from poium import Page, Element


'''
发起提问页面
com.jinjilie.daxuezhang.functions.MainActivity
'''


class PutForwardQuestionPage:
    def __init__(self, project):
        self.Android = project
        # region Fields
        # 问题标题
        self._question_title_text_tag = "//*[@resource-id='com.jinjilie.daxuezhang.debug:id/title_et']"
        # 问题内容
        self._question_content_text_tag = "//*[@resource-id='com.jinjilie.daxuezhang.debug:id/content_et']"
        # 下一步
        self._next_button_tag = "//*[@resource-id='com.jinjilie.daxuezhang.debug:id/header_right_tv']"
        # endregion Fields

    # region Properties
    @property
    def question_title_text(self):
        """
        属性: 问题标题
        :return: 问题标题
        """
        element = None
        try:
            element = self.Android.get_element(self._question_title_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def question_content_text(self):
        """
        属性: 问题内容
        :return: 问题内容
        """
        element = None
        try:
            element = self.Android.get_element(self._question_content_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def next_button(self):
        """
        属性: 下一步
        :return: 下一步
        """
        element = None
        try:
            element = self.Android.get_element(self._next_button_tag)
        except AttributeError as error:
            log(error)
        return element

    # endregion Properties

    # region Actions
    def get_question_title_text_action(self):
        """
        动作：获取问题标题的文本
        :return: '问题标题'的文本
        """
        control_content = self.question_title_text.text.strip()
        return control_content

    def get_question_content_text_action(self):
        """
        动作：获取问题内容的文本
        :return: '问题内容'的文本
        """
        control_content = self.question_content_text.text.strip()
        return control_content

    def click_next_button_action(self):
        """
        动作：点击下一步
        :return: 点击'下一步'按钮后的页面
        """
        self.Android.click(self.next_button)
        return self.Android.get_current_page_source()

    # endregion Actions
