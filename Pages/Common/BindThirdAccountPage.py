from Utils.Log import log
from poium import Page, Element


'''
身份验证页面
com.jinjilie.daxuezhang.functions.MainActivity
'''


class BindThirdAccountPage:

    def __init__(self, project):
        self.Android = project
        # region Fields
        # 后退按钮
        self._back_button_tag = '//*[@resource-id="com.jinjilie.daxuezhang.debug:id/header_left_iv"]'
        # 手机号
        self._phone_button_tag = "//*[@text='手机号']"
        # 邮箱
        self._mail_button_tag = "//*[@text='邮箱']"
        # endregion Fields

    # region Properties
    @property
    def back_button(self):
        """
        属性: 后退按钮
        :return: 后退按钮
        """
        element = None
        try:
            element = self.Android.get_element(self._back_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def phone_button(self):
        """
        属性: 手机号
        :return: 手机号
        """
        element = None
        try:
            element = self.Android.get_element(self._phone_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def mail_button(self):
        """
        属性: 邮箱
        :return: 邮箱
        """
        element = None
        try:
            element = self.Android.get_element(self._mail_button_tag)
        except AttributeError as error:
            log(error)
        return element

    # endregion Properties

    # region Actions
    def click_back_button_action(self):
        """
        动作：点击后退按钮
        :return: 点击'后退按钮'按钮后的页面
        """
        self.Android.click(self.back_button)
        return self.Android.get_current_page_source()

    def click_phone_button_action(self):
        """
        动作：点击手机号
        :return: 点击'手机号'按钮后的页面
        """
        self.Android.click(self.phone_button)
        return self.Android.get_current_page_source()

    def click_mail_button_action(self):
        """
        动作：点击邮箱
        :return: 点击'邮箱'按钮后的页面
        """
        self.Android.click(self.mail_button)
        return self.Android.get_current_page_source()

    # endregion Actions
