from Utils.Log import log
from poium import Page, Element


'''
微聊首页
com.jinjilie.daxuezhang.functions.MainActivity
'''


class WechatHomePage:

    def __init__(self, project):
        self.Android = project
        # region Fields
        # 好友列表
        self._header_right_book_button_tag = "//*[@resource-id='com.jinjilie.daxuezhang.debug:id/iv_header_right_book']"
        # 右上角order +
        self._header_right_order_button_tag = "//*[@resource-id='com.jinjilie.daxuezhang.debug:id/iv_header_right_order']"
        # 发起群聊
        self._grouper_button_tag = "//*[@resource-id='com.jinjilie.daxuezhang.debug:id/grouper_tv']"
       # endregion Fields

    # region Properties
    @property
    def header_right_book_button(self):
        """
        属性: 好友列表
        :return: 好友列表
        """
        element = None
        try:
            element = self.Android.get_element(self._header_right_book_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def header_right_order_button(self):
        """
        属性: 右上角order +
        :return: 右上角order +
        """
        element = None
        try:
            element = self.Android.get_element(self._header_right_order_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def grouper_button(self):
        """
        属性: 发起群聊
        :return: 发起群聊
        """
        element = None
        try:
            element = self.Android.get_element(self._grouper_button_tag)
        except AttributeError as error:
            log(error)
        return element

    # endregion Properties

    # region Actions
    def click_header_right_book_button_action(self):
        """
        动作：点击好友列表
        :return: 点击'好友列表'按钮后的页面
        """
        self.Android.click(self.header_right_book_button)
        return self.Android.get_current_page_source()

    def click_header_right_order_button_action(self):
        """
        动作：点击右上角order
        :return: 点击'右上角order'按钮后的页面
        """
        self.Android.click(self.header_right_order_button)
        return self.Android.get_current_page_source()

    def click_grouper_button_action(self):
        """
        动作：点击发起群聊
        :return: 点击'发起群聊'按钮后的页面
        """
        self.Android.click(self.grouper_button)
        return self.Android.get_current_page_source()

    # endregion Actions
