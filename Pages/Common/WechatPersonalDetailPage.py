from Utils.Log import log
from poium import Page, Element


'''
微聊内容-个人详情页面
com.jinjilie.daxuezhang.functions.MainActivity
'''


class WechatPersonalDetailPage:

    def __init__(self, project):
        self.Android = project
        # region Fields
        # 主页
        self._homepage_button_tag = "//*[@resource-id='com.jinjilie.daxuezhang.debug:id/homepage_rl']"
       # endregion Fields

    # region Properties
    @property
    def homepage_button(self):
        """
        属性: 主页
        :return: 主页
        """
        element = None
        try:
            element = self.Android.get_element(self._homepage_button_tag)
        except AttributeError as error:
            log(error)
        return element

    # endregion Properties

    # region Actions
    def click_homepage_button_action(self):
        """
        动作：点击主页
        :return: 点击'主页'按钮后的页面
        """
        self.Android.click(self.homepage_button)
        return self.Android.get_current_page_source()

    # endregion Actions
