from Utils.Log import log
from poium import Page, Element


'''
首次启动-温馨提示页面
com.jinjilie.daxuezhang.functions.MainActivity
'''


class ImmediatelyExperiencePage:
    def __init__(self, project):
        self.Android = project
        # region Fields
        # 立即体验按钮
        self._immediately_experience_button_tag = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout[2]/android.widget.TextView[1]"
        # endregion Fields

    # region Properties
    @property
    def immediately_experience_button(self):
        """
        属性: 立即体验按钮
        :return: 立即体验按钮
        """
        element = None
        try:
            element = self.Android.get_element(self._immediately_experience_button_tag)
        except AttributeError as error:
            log(error)
        return element

    # endregion Properties

    # region Actions
    def click_immediately_experience_button_action(self):
        """
        动作：点击立即体验按钮
        :return: 点击'立即体验按钮'按钮后的页面
        """
        self.Android.click(self.immediately_experience_button)
        return self.Android.get_current_page_source()

    # endregion Actions
