from Utils.Log import log
from poium import Page, Element


'''
首次启动-温馨提示页面
com.jinjilie.daxuezhang.functions.MainActivity
'''


class FirstStartPromptPage:

    def __init__(self, project):
        self.Android = project
        # region Fields
        # 同意按钮
        self._agree_button_tag = "//*[@text='同意']"
        # 用户注册协议
        self._user_register_agreement_link_button_tag = "//*[@text='《用户注册协议》']"
        # 隐私政策
        self._privacy_link_button_tag = "//*[@text='《隐私政策》']"
        # 提示内容
        self._prompt_content_text_tag = "//*[@resource-id='com.jinjilie.daxuezhang.debug:id/register_protocol_tv']"
        # endregion Fields

    # region Properties
    @property
    def agree_button(self):
        """
        属性: 同意按钮
        :return: 同意按钮
        """
        element = None
        try:
            element = self.Android.get_element(self._agree_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def user_register_agreement_link_button(self):
        """
        属性: 用户注册协议
        :return: 用户注册协议
        """
        element = None
        try:
            element = self.Android.get_element(self._user_register_agreement_link_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def privacy_link_button(self):
        """
        属性: 隐私政策
        :return: 隐私政策
        """
        element = None
        try:
            element = self.Android.get_element(self._privacy_link_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def prompt_content_text(self):
        """
        属性: 提示内容
        :return: 提示内容
        """
        element = None
        try:
            element = self.Android.get_element(self._prompt_content_text_tag)
        except AttributeError as error:
            log(error)
        return element

    # endregion Properties

    # region Actions
    def click_agree_button_action(self):
        """
        动作：点击同意按钮
        :return: 点击'同意按钮'按钮后的页面
        """
        self.Android.click(self.agree_button)
        return self.Android.get_current_page_source()

    def click_user_register_agreement_link_button_action(self):
        """
        动作：点击用户注册协议
        :return: 点击'用户注册协议'按钮后的页面
        """
        self.Android.click(self.user_register_agreement_link_button)
        return self.Android.get_current_page_source()

    def click_privacy_link_button_action(self):
        """
        动作：点击隐私政策
        :return: 点击'隐私政策'按钮后的页面
        """
        self.Android.click(self.privacy_link_button)
        return self.Android.get_current_page_source()

    def get_prompt_content_text_action(self):
        """
        动作：获取提示内容的文本
        :return: '提示内容'的文本
        """
        control_content = self.prompt_content_text.text.strip()
        return control_content

    # endregion Actions
