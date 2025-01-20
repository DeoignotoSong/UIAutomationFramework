from Utils.Log import log
from poium import Page, Element


'''
讲师主页
com.jinjilie.daxuezhang.functions.MainActivity
'''


class LecturerHomePage:

    def __init__(self, project):
        self.Android = project
        # region Fields
        # 关注按钮
        self._add_follow_button_tag = "//*[@resource-id='com.jinjilie.daxuezhang.debug:id/add_follow_bt']"
        # 微聊按钮
        self._wechat_button_tag = "//*[@resource-id='com.jinjilie.daxuezhang.debug:id/chat_ll']"
        # 发送按钮
        self._chat_input_send_button_tag = "//*[@resource-id='com.jinjilie.daxuezhang.debug:id/bytedesk_chat_input_send_button']"
       # endregion Fields

    # region Properties
    @property
    def add_follow_button(self):
        """
        属性: 关注按钮
        :return: 关注按钮
        """
        element = None
        try:
            element = self.Android.get_element(self._add_follow_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def wechat_button(self):
        """
        属性: 微聊按钮
        :return: 微聊按钮
        """
        element = None
        try:
            element = self.Android.get_element(self._wechat_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def chat_input_send_button(self):
        """
        属性: 发送按钮
        :return: 发送按钮
        """
        element = None
        try:
            element = self.Android.get_element(self._chat_input_send_button_tag)
        except AttributeError as error:
            log(error)
        return element

    # endregion Properties

    # region Actions
    def click_add_follow_button_action(self):
        """
        动作：点击关注按钮
        :return: 点击'关注按钮'按钮后的页面
        """
        self.Android.click(self.add_follow_button)
        return self.Android.get_current_page_source()

    def click_wechat_button_action(self):
        """
        动作：点击微聊按钮
        :return: 点击'微聊按钮'按钮后的页面
        """
        self.Android.click(self.wechat_button)
        return self.Android.get_current_page_source()

    def click_chat_input_send_button_action(self):
        """
        动作：点击发送按钮
        :return: 点击'发送按钮'按钮后的页面
        """
        self.Android.click(self.chat_input_send_button)
        return self.Android.get_current_page_source()

    # endregion Actions
