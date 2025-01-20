from Utils.Log import log


'''
学校详情页面
com.jinjilie.daxuezhang.functions.detail.activity.ArticleActivity
'''


class CollegeDetailPage:
    def __init__(self, project):
        self.Android = project

        # region Fields
        # 后退按钮
        self._college_detail_back_button_tag = '//*[@resource-id="com.jinjilie.daxuezhang.debug:id/header_left_iv"]'
        # 文章标题
        self._college_detail_title_text_tag = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.TextView[1]'
        # endregion Fields

    # region Properties
    @property
    def college_detail_back_button(self):
        """
        属性: 后退按钮
        :return: 后退按钮
        """
        element = None
        try:
            element = self.Android.get_element(self._college_detail_back_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def college_detail_title_text(self):
        """
        属性: 文章标题
        :return: 文章标题
        """
        element = None
        try:
            element = self.Android.get_element(self._college_detail_title_text_tag)
        except AttributeError as error:
            log(error)
        return element

    # endregion Properties

    # region Actions
    def click_college_detail_back_button_action(self):
        """
        动作：点击后退按钮
        :return: 点击'后退按钮'按钮后的页面
        """
        self.Android.click(self.college_detail_back_button)
        return self.Android.get_current_page_source()

    def get_college_detail_title_text_action(self):
        """
        动作：获取文章标题的文本
        :return: '文章标题'的文本
        """
        control_content = self.college_detail_title_text.text.strip()
        return control_content

    # endregion Actions
