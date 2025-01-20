from Utils.Log import log
from poium import Page, Element


'''
绑定邮箱页面
com.jinjilie.daxuezhang.functions.MainActivity
'''


class BindThirdAccountByMailPage:

    def __init__(self, project):
        self.Android = project
        # region Fields
        # 后退按钮
        self._back_button_tag = '//*[@resource-id="com.jinjilie.daxuezhang.debug:id/header_left_iv"]'
        # 输入邮箱
        self._input_mail_tag = '//*[@resource-id="com.jinjilie.daxuezhang.debug:id/bind_phone_et"]'
        # 绑定
        self._submit_button_tag = '//*[@resource-id="com.jinjilie.daxuezhang.debug:id/bind_next_tv"]'
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
    def input_mail(self):
        """
        属性: 输入邮箱
        :return: 输入邮箱
        """
        element = None
        try:
            element = self.Android.get_element(self._input_mail_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def submit_button(self):
        """
        属性: 绑定
        :return: 绑定
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

    def click_submit_button_action(self):
        """
        动作：点击绑定
        :return: 点击'绑定'按钮后的页面
        """
        self.Android.click(self.submit_button)
        return self.Android.get_current_page_source()

    # endregion Actions
