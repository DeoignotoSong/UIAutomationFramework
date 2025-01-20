from Utils.Log import log
from poium import Page, Element


'''
身份验证页面
com.jinjilie.daxuezhang.functions.MainActivity
'''


class IdentityVerifyPage:

    def __init__(self, project):
        self.Android = project
        # region Fields
        # 后退按钮
        self._back_button_tag = '//*[@resource-id="com.jinjilie.daxuezhang.debug:id/header_left_iv"]'
        # 输入验证码
        self._psw_change_code_tag = "//*[@resource-id='com.jinjilie.daxuezhang.debug:id/bind_code_or_psw_et']"
        # 获取验证码按钮
        self._get_code_button_tag = "//*[@resource-id='com.jinjilie.daxuezhang.debug:id/bind_get_code_tv']"
        # 提交按钮
        self._submit_button_tag = "//*[@resource-id='com.jinjilie.daxuezhang.debug:id/bind_next_tv']"
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
    def psw_change_code(self):
        """
        属性: 输入验证码
        :return: 输入验证码
        """
        element = None
        try:
            element = self.Android.get_element(self._psw_change_code_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def get_code_button(self):
        """
        属性: 获取验证码按钮
        :return: 获取验证码按钮
        """
        element = None
        try:
            element = self.Android.get_element(self._get_code_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def submit_button(self):
        """
        属性: 提交按钮
        :return: 提交按钮
        """
        element = None
        try:
            element = self.Android.get_element(self._submit_button_tag)
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

    def click_get_code_button_action(self):
        """
        动作：点击获取验证码按钮
        :return: 点击'获取验证码按钮'按钮后的页面
        """
        self.Android.click(self.get_code_button)
        return self.Android.get_current_page_source()

    def click_submit_button_action(self):
        """
        动作：点击提交按钮
        :return: 点击'提交按钮'按钮后的页面
        """
        self.Android.click(self.submit_button)
        return self.Android.get_current_page_source()

    # endregion Actions
