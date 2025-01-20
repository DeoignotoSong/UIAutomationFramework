from Utils.Log import log
from poium import Page, Element


'''
选择标签页面
com.jinjilie.daxuezhang.functions.MainActivity
'''


class SettingRewardQuestionPage:
    def __init__(self, project):
        self.Android = project
        # region Fields
        # 不悬赏直接提问
        self._show_question_button_tag = "//*[@resource-id='com.jinjilie.daxuezhang.debug:id/show_question_tv']"
        # endregion Fields

    # region Properties
    @property
    def show_question_button(self):
        """
        属性: 不悬赏直接提问
        :return: 不悬赏直接提问
        """
        element = None
        try:
            element = self.Android.get_element(self._show_question_button_tag)
        except AttributeError as error:
            log(error)
        return element

    # endregion Properties

    # region Actions
    def click_show_question_button_action(self):
        """
        动作：点击不悬赏直接提问
        :return: 点击'不悬赏直接提问'按钮后的页面
        """
        self.Android.click(self.show_question_button)
        return self.Android.get_current_page_source()

    # endregion Actions
