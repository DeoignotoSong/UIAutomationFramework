from Utils.Log import log
from poium import Page, Element


'''
App设置页面
com.jinjilie.daxuezhang.functions.MainActivity
'''


class AppSettingPage:

    def __init__(self, project):
        self.Android = project
        # region Fields
        # 退出登录按钮
        self._logout_button_tag = "//*[@resource-id='com.jinjilie.daxuezhang.debug:id/logout_bt']"
        # endregion Fields

    # region Properties
    @property
    def logout_button(self):
        """
        属性: 退出登录按钮
        :return: 退出登录按钮
        """
        element = None
        try:
            element = self.Android.get_element(self._logout_button_tag)
        except AttributeError as error:
            log(error)
        return element

    # endregion Properties

    # region Actions
    def click_logout_button_action(self):
        """
        动作：点击退出登录按钮
        :return: 点击'退出登录按钮'按钮后的页面
        """
        self.Android.click(self.logout_button)
        return self.Android.get_current_page_source()

    # endregion Actions
