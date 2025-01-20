from Utils.Log import log


'''
无效资源页面
com.jinjilie.daxuezhang.functions.MainActivity
'''


class App404InvalidateResourcePage:

    def __init__(self, project):
        self.Android = project
        # region Fields
        # 返回前一页面
        self._back_button_tag = "//*[@resource-id='com.jinjilie.daxuezhang.debug:id/back_iv2']"
        # 提示内容
        self._prompt_error_info_tag = "//*[@resource-id='com.jinjilie.daxuezhang.debug:id/tv_error']"
        # endregion Fields

    # region Properties
    @property
    def back_button(self):
        """
        属性: 返回前一页面
        :return: 返回前一页面
        """
        element = None
        try:
            element = self.Android.get_element(self._back_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def prompt_error_info(self):
        """
        属性: 提示内容
        :return: 提示内容
        """
        element = None
        try:
            element = self.Android.get_element(self._prompt_error_info_tag)
        except AttributeError as error:
            log(error)
        return element

    # endregion Properties

    # region Actions
    def click_back_button_action(self):
        """
        动作：点击返回前一页面
        :return: 点击'返回前一页面'按钮后的页面
        """
        self.Android.click(self.back_button)
        return self.Android.get_current_page_source()

    # endregion Actions
