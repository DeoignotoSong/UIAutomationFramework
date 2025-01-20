from Utils.Log import log
from poium import Page, Element


'''
用户主页
com.jinjilie.daxuezhang.functions.MainActivity
'''


class UserHomePage:

    def __init__(self, project):
        self.Android = project
        # region Fields
        # 关注按钮
        self._user_focus_button_tag = "//*[@resource-id='com.jinjilie.daxuezhang.debug:id/user_focus_iv']"
        # 微聊按钮
        self._user_chat_button_tag = "//*[@resource-id='com.jinjilie.daxuezhang.debug:id/user_chat_iv']"
        # 粉丝数量
        self._user_fans_count_tag = "//*[@resource-id='com.jinjilie.daxuezhang.debug:id/user_fans_ll']/android.widget.TextView[1]"
       # endregion Fields

    # region Properties
    @property
    def user_focus_button(self):
        """
        属性: 关注按钮
        :return: 关注按钮
        """
        element = None
        try:
            element = self.Android.get_element(self._user_focus_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def user_chat_button(self):
        """
        属性: 微聊按钮
        :return: 微聊按钮
        """
        element = None
        try:
            element = self.Android.get_element(self._user_chat_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def user_fans_count(self):
        """
        属性: 粉丝数量
        :return: 粉丝数量
        """
        element = None
        try:
            element = self.Android.get_element(self._user_fans_count_tag)
        except AttributeError as error:
            log(error)
        return element

    # endregion Properties

    # region Actions
    def click_user_focus_button_action(self):
        """
        动作：点击关注按钮
        :return: 点击'关注按钮'按钮后的页面
        """
        self.Android.click(self.user_focus_button)
        return self.Android.get_current_page_source()

    def click_user_chat_button_action(self):
        """
        动作：点击微聊按钮
        :return: 点击'微聊按钮'按钮后的页面
        """
        self.Android.click(self.user_chat_button)
        return self.Android.get_current_page_source()

    # endregion Actions
