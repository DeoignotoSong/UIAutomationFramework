from Utils.Log import log
from poium import Page, Element


'''
微聊通讯录
com.jinjilie.daxuezhang.functions.MainActivity
'''


class WechatAdressBookPage:

    def __init__(self, project):
        self.Android = project
        # region Fields
        # 添加学友Icon
        self._add_user_icon_button_tag = "//*[@resource-id='com.jinjilie.daxuezhang.debug:id/qun_iv']"
       # endregion Fields

    # region Properties
    @property
    def add_user_icon_button(self):
        """
        属性: 添加学友Icon
        :return: 添加学友Icon
        """
        element = None
        try:
            element = self.Android.get_element(self._add_user_icon_button_tag)
        except AttributeError as error:
            log(error)
        return element

    # endregion Properties

    # region Actions
    def click_add_user_icon_button_action(self):
        """
        动作：点击添加学友Icon
        :return: 点击'添加学友Icon'按钮后的页面
        """
        self.Android.click(self.add_user_icon_button)
        return self.Android.get_current_page_source()

    # endregion Actions
