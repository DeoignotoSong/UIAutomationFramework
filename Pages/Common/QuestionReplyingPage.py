from Utils.Log import log
from poium import Page, Element


'''
发起提问页面
com.jinjilie.daxuezhang.functions.MainActivity
'''


class QuestionReplyingPage:
    def __init__(self, project):
        self.Android = project
        # region Fields
        # 回复内容
        self._answer_input_tag = "//*[@resource-id='com.jinjilie.daxuezhang.debug:id/answer_input_et']"
        # 发布按钮
        self._next_button_tag = "//*[@resource-id='com.jinjilie.daxuezhang.debug:id/header_right_tv']"
        # endregion Fields

    # region Properties
    @property
    def answer_input(self):
        """
        属性: 回复内容
        :return: 回复内容
        """
        element = None
        try:
            element = self.Android.get_element(self._answer_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def next_button(self):
        """
        属性: 发布按钮
        :return: 发布按钮
        """
        element = None
        try:
            element = self.Android.get_element(self._next_button_tag)
        except AttributeError as error:
            log(error)
        return element

    # endregion Properties

    # region Actions
    def set_answer_input_action(self, answer_input):
        """
        动作：设置回复内容
        :param answer_input: 回复内容
        :return: 设置'回复内容'文本后的页面
        """
        self.Android.clear_and_send_keys(self.answer_input, answer_input)
        return self.Android.get_current_page_source()

    def click_next_button_action(self):
        """
        动作：点击发布按钮
        :return: 点击'发布按钮'按钮后的页面
        """
        self.Android.click(self.next_button)
        return self.Android.get_current_page_source()

    # endregion Actions
