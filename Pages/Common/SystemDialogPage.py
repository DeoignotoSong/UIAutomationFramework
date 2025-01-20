from Utils.Log import log
from poium import Page, Element


'''
通用Dialog弹出框页面
com.jinjilie.daxuezhang.functions.MainActivity
'''


class SystemDialogPage:
    def __init__(self, project):
        self.Android = project
        # region Fields
        # 禁止button
        self._forbidden_button_tag = "//*[@text='禁止']"
        # 仅使用期间允许button
        self._duration_allow_button_tag = "//*[@text='仅使用期间允许']"
        # 始终允许button
        self._all_allow_button_tag = "//*[@text='始终允许']"
        # endregion Fields

    # region Properties
    @property
    def forbidden_button(self):
        """
        属性: 禁止button
        :return: 禁止button
        """
        element = None
        try:
            element = self.Android.get_element(self._forbidden_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def duration_allow_button(self):
        """
        属性: 仅使用期间允许button
        :return: 仅使用期间允许button
        """
        element = None
        try:
            element = self.Android.get_element(self._duration_allow_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def all_allow_button(self):
        """
        属性: 始终允许button
        :return: 始终允许button
        """
        element = None
        try:
            element = self.Android.get_element(self._all_allow_button_tag)
        except AttributeError as error:
            log(error)
        return element

    # endregion Properties

    # region Actions
    def click_forbidden_button_action(self):
        """
        动作：点击禁止button
        :return: 点击'禁止button'按钮后的页面
        """
        self.Android.click(self.forbidden_button)
        return self.Android.get_current_page_source()

    def click_duration_allow_button_action(self):
        """
        动作：点击仅使用期间允许button
        :return: 点击'仅使用期间允许button'按钮后的页面
        """
        self.Android.click(self.duration_allow_button)
        return self.Android.get_current_page_source()

    def click_all_allow_button_action(self):
        """
        动作：点击始终允许button
        :return: 点击'始终允许button'按钮后的页面
        """
        self.Android.click(self.all_allow_button)
        return self.Android.get_current_page_source()

    # endregion Actions
