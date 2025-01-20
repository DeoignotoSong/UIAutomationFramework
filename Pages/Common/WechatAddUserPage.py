from Utils.Log import log
from poium import Page, Element


'''
微聊通讯录-添加学友页面
com.jinjilie.daxuezhang.functions.MainActivity
'''


class WechatAddUserPage:

    def __init__(self, project):
        self.Android = project
        # region Fields
        # 搜索栏
        self._search_edit_tag = "//*[@resource-id='com.jinjilie.daxuezhang.debug:id/et_search']"
        # 搜索显示文字
        self._search_text_tag = "//*[@resource-id='com.jinjilie.daxuezhang.debug:id/searchText_tv']"
       # endregion Fields

    # region Properties
    @property
    def search_edit(self):
        """
        属性: 搜索栏
        :return: 搜索栏
        """
        element = None
        try:
            element = self.Android.get_element(self._search_edit_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def search_text(self):
        """
        属性: 搜索显示文字
        :return: 搜索显示文字
        """
        element = None
        try:
            element = self.Android.get_element(self._search_text_tag)
        except AttributeError as error:
            log(error)
        return element

    # endregion Properties

    # region Actions
    def get_search_text_action(self):
        """
        动作：获取搜索显示文字的文本
        :return: '搜索显示文字'的文本
        """
        control_content = self.search_text.text.strip()
        return control_content

    # endregion Actions
