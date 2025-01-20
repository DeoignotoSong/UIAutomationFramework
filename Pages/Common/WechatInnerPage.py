from Utils.Log import log
from poium import Page, Element


'''
微聊内容页面
com.jinjilie.daxuezhang.functions.MainActivity
'''


class WechatInnerPage:

    def __init__(self, project):
        self.Android = project
        # region Fields
        # 头像icon
        self._header_icon_button_tag = "//*[@resource-id='com.jinjilie.daxuezhang.debug:id/bytedesk_message_item_header']"
        # 右上角分享option
        self._header_right_button_tag = "//*[@resource-id='com.jinjilie.daxuezhang.debug:id/iv_header_right']"
        # 微聊信息输入框
        self._chat_fragment_input_tag = "//*[@resource-id='com.jinjilie.daxuezhang.debug:id/bytedesk_chat_fragment_input']"
        # 发送按钮
        self._send_button_tag = "//*[@resource-id='com.jinjilie.daxuezhang.debug:id/bytedesk_chat_input_send_button']"
        # 头部标题
        self._header_center_title_tag = "//*[@resource-id='com.jinjilie.daxuezhang.debug:id/header_center_tv']"
        # 群组人员数量
        self._group_num_tag = "//*[@resource-id='com.jinjilie.daxuezhang.debug:id/group_num_tv']"
        # 群类型
        self._session_type_tag = "//*[@resource-id='com.jinjilie.daxuezhang.debug:id/session_type_tv']"
       # endregion Fields

    # region Properties
    @property
    def header_icon_button(self):
        """
        属性: 头像icon
        :return: 头像icon
        """
        element = None
        try:
            element = self.Android.get_element(self._header_icon_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def header_right_button(self):
        """
        属性: 右上角分享option
        :return: 右上角分享option
        """
        element = None
        try:
            element = self.Android.get_element(self._header_right_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def chat_fragment_input(self):
        """
        属性: 微聊信息输入框
        :return: 微聊信息输入框
        """
        element = None
        try:
            element = self.Android.get_element(self._chat_fragment_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def send_button(self):
        """
        属性: 发送按钮
        :return: 发送按钮
        """
        element = None
        try:
            element = self.Android.get_element(self._send_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def header_center_title(self):
        """
        属性: 头部标题
        :return: 头部标题
        """
        element = None
        try:
            element = self.Android.get_element(self._header_center_title_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def group_num(self):
        """
        属性: 群组人员数量
        :return: 群组人员数量
        """
        element = None
        try:
            element = self.Android.get_element(self._group_num_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def session_type(self):
        """
        属性: 群类型
        :return: 群类型
        """
        element = None
        try:
            element = self.Android.get_element(self._session_type_tag)
        except AttributeError as error:
            log(error)
        return element

    # endregion Properties

    # region Actions
    def click_header_icon_button_action(self):
        """
        动作：点击头像icon
        :return: 点击'头像icon'按钮后的页面
        """
        self.Android.click(self.header_icon_button)
        return self.Android.get_current_page_source()

    def click_header_right_button_action(self):
        """
        动作：点击右上角分享option
        :return: 点击'右上角分享option'按钮后的页面
        """
        self.Android.click(self.header_right_button)
        return self.Android.get_current_page_source()

    def set_chat_fragment_input_action(self, chat_fragment_input):
        """
        动作：设置微聊信息输入框
        :param chat_fragment_input: 微聊信息输入框
        :return: 设置'微聊信息输入框'文本后的页面
        """
        self.Android.clear_and_send_keys(self.chat_fragment_input, chat_fragment_input)
        return self.Android.get_current_page_source()

    def click_send_button_action(self):
        """
        动作：点击发送按钮
        :return: 点击'发送按钮'按钮后的页面
        """
        self.Android.click(self.send_button)
        return self.Android.get_current_page_source()

    # endregion Actions
