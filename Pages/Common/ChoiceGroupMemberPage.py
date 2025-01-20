from Utils.Log import log
from poium import Page, Element


'''
选择群成员页面
com.jinjilie.daxuezhang.functions.MainActivity
'''


class ChoiceGroupMemberPage:

    def __init__(self, project):
        self.Android = project
        # region Fields
        # 完成按钮
        self._header_right_button_tag = "//*[@resource-id='com.jinjilie.daxuezhang.debug:id/tv_header_right']"
       # endregion Fields

    # region Properties
    @property
    def header_right_button(self):
        """
        属性: 完成按钮
        :return: 完成按钮
        """
        element = None
        try:
            element = self.Android.get_element(self._header_right_button_tag)
        except AttributeError as error:
            log(error)
        return element

    # endregion Properties

    # region Actions
    def click_header_right_button_action(self):
        """
        动作：点击完成按钮
        :return: 点击'完成按钮'按钮后的页面
        """
        self.Android.click(self.header_right_button)
        return self.Android.get_current_page_source()

    # endregion Actions
