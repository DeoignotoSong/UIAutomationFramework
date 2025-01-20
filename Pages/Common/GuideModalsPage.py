from Utils.Log import log
from poium import Page, Element


'''
Guide指导模态层
com.jinjilie.daxuezhang.functions.MainActivity
'''


class GuideModalsPage:

    def __init__(self, project):
        self.Android = project
        # region Fields
        # 下一步按钮
        self._next_button_tag = "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout[1]/android.widget.TextView"
        # 我知道了按钮
        self._i_know_button_tag = "//*[@resource-id='com.jinjilie.daxuezhang.debug:id/tv_next']"
        # endregion Fields

    # region Properties
    @property
    def next_button(self):
        """
        属性: 下一步按钮
        :return: 下一步按钮
        """
        element = None
        try:
            element = self.Android.get_element(self._next_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def i_know_button(self):
        """
        属性: 我知道了按钮
        :return: 我知道了按钮
        """
        element = None
        try:
            element = self.Android.get_element(self._i_know_button_tag)
        except AttributeError as error:
            log(error)
        return element

    # endregion Properties

    # region Actions
    def click_next_button_action(self):
        """
        动作：点击下一步按钮
        :return: 点击'下一步按钮'按钮后的页面
        """
        self.Android.click(self.next_button)
        return self.Android.get_current_page_source()

    def click_i_know_button_action(self):
        """
        动作：点击我知道了按钮
        :return: 点击'我知道了按钮'按钮后的页面
        """
        self.Android.click(self.i_know_button)
        return self.Android.get_current_page_source()

    # endregion Actions
