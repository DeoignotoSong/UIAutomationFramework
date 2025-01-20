from Utils.Log import log
from poium import Page, Element


'''
位置选择页面
com.jinjilie.daxuezhang.functions.MainActivity
'''


class QuestionReplyDetailPage:

    def __init__(self, project):
        self.Android = project
        # region Fields
        # 收藏
        self._reply_comment_focus_button_tag = "//*[@resource-id='com.jinjilie.daxuezhang.debug:id/comment_focus_iv']"
        # 点赞
        self._reply_comment_praise_button_tag = "//*[@resource-id='com.jinjilie.daxuezhang.debug:id/comment_praise_iv']"
        # 回复
        self._reply_comment_button_tag = "//*[@resource-id='com.jinjilie.daxuezhang.debug:id/comment_iv']"
        # 回复输入内容
        self._reply_comment_input_tag = "//*[@resource-id='com.jinjilie.daxuezhang.debug:id/et_content']"
        # 回复发送button
        self._reply_comment_send_button_tag = "//*[@resource-id='com.jinjilie.daxuezhang.debug:id/btn_send']"
        # endregion Fields

    # region Properties
    @property
    def reply_comment_focus_button(self):
        """
        属性: 收藏
        :return: 收藏
        """
        element = None
        try:
            element = self.Android.get_element(self._reply_comment_focus_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def reply_comment_praise_button(self):
        """
        属性: 点赞
        :return: 点赞
        """
        element = None
        try:
            element = self.Android.get_element(self._reply_comment_praise_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def reply_comment_button(self):
        """
        属性: 回复
        :return: 回复
        """
        element = None
        try:
            element = self.Android.get_element(self._reply_comment_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def reply_comment_input(self):
        """
        属性: 回复输入内容
        :return: 回复输入内容
        """
        element = None
        try:
            element = self.Android.get_element(self._reply_comment_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def reply_comment_send_button(self):
        """
        属性: 回复发送button
        :return: 回复发送button
        """
        element = None
        try:
            element = self.Android.get_element(self._reply_comment_send_button_tag)
        except AttributeError as error:
            log(error)
        return element

    # endregion Properties

    # region Actions
    def click_reply_comment_focus_button_action(self):
        """
        动作：点击收藏
        :return: 点击'收藏'按钮后的页面
        """
        self.Android.click(self.reply_comment_focus_button)
        return self.Android.get_current_page_source()

    def click_reply_comment_praise_button_action(self):
        """
        动作：点击点赞
        :return: 点击'点赞'按钮后的页面
        """
        self.Android.click(self.reply_comment_praise_button)
        return self.Android.get_current_page_source()

    def click_reply_comment_button_action(self):
        """
        动作：点击回复
        :return: 点击'回复'按钮后的页面
        """
        self.Android.click(self.reply_comment_button)
        return self.Android.get_current_page_source()

    def set_reply_comment_input_action(self, reply_comment_input):
        """
        动作：设置回复输入内容
        :param reply_comment_input: 回复输入内容
        :return: 设置'回复输入内容'文本后的页面
        """
        self.Android.clear_and_send_keys(self.reply_comment_input, reply_comment_input)
        return self.Android.get_current_page_source()

    def click_reply_comment_send_button_action(self):
        """
        动作：点击回复发送button
        :return: 点击'回复发送button'按钮后的页面
        """
        self.Android.click(self.reply_comment_send_button)
        return self.Android.get_current_page_source()

    # endregion Actions
