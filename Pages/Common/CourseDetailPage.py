from Utils.Log import log


'''
课程详情页面
com.jinjilie.daxuezhang.functions.detail.activity.ArticleActivity
'''


class CourseDetailPage:
    def __init__(self, project):
        self.Android = project

        # region Fields
        # 后退按钮
        # self._course_detail_back_button_tag = '//*[@resource-id="com.jinjilie.daxuezhang.debug:id/header_left_iv"]'
        self._course_detail_back_button_tag = '//*[@resource-id="com.jinjilie.daxuezhang.debug:id/back_iv"]'
        # 右上角分享按钮
        self._course_shared_button_tag = '//*[@resource-id="com.jinjilie.daxuezhang.debug:id/shared_iv"]'
        # 分享默认第一个user
        self._recent_charts_button_tag = '//*[@resource-id="com.jinjilie.daxuezhang.debug:id/rvRecentChats"]/android.widget.LinearLayout[1]'
        # 购买按钮
        self._course_detail_goods_buy_button_tag = '//*[@resource-id="com.jinjilie.daxuezhang.debug:id/goods_buy_ll"]'
        # 直播讲座-立即购买
        self._course_detail_dialog_goods_buy_button_tag = '//*[@resource-id="com.jinjilie.daxuezhang.debug:id/dialog_class_yes_bt"]'
        # 课程标题
        self._course_detail_title_text_tag = '//*[@resource-id="app"]/android.view.View/android.view.View[1]/android.view.View[1]'

        # endregion Fields

    # region Properties
    @property
    def course_detail_back_button(self):
        """
        属性: 后退按钮
        :return: 后退按钮
        """
        element = None
        try:
            element = self.Android.get_element(self._course_detail_back_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def course_shared_button(self):
        """
        属性: 右上角分享按钮
        :return: 右上角分享按钮
        """
        element = None
        try:
            element = self.Android.get_element(self._course_shared_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def recent_charts_button(self):
        """
        属性: 分享默认第一个user
        :return: 分享默认第一个user
        """
        element = None
        try:
            element = self.Android.get_element(self._recent_charts_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def course_detail_goods_buy_button(self):
        """
        属性: 购买按钮
        :return: 购买按钮
        """
        element = None
        try:
            element = self.Android.get_element(self._course_detail_goods_buy_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def course_detail_dialog_goods_buy_button(self):
        """
        属性: 直播讲座-立即购买
        :return: 直播讲座-立即购买
        """
        element = None
        try:
            element = self.Android.get_element(self._course_detail_dialog_goods_buy_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def course_detail_title_text(self):
        """
        属性: 课程标题
        :return: 课程标题
        """
        element = None
        try:
            element = self.Android.get_element(self._course_detail_title_text_tag)
        except AttributeError as error:
            log(error)
        return element

    # endregion Properties

    # region Actions
    def click_course_detail_back_button_action(self):
        """
        动作：点击后退按钮
        :return: 点击'后退按钮'按钮后的页面
        """
        self.Android.click(self.course_detail_back_button)
        return self.Android.get_current_page_source()

    def click_course_shared_button_action(self):
        """
        动作：点击右上角分享按钮
        :return: 点击'右上角分享按钮'按钮后的页面
        """
        self.Android.click(self.course_shared_button)
        return self.Android.get_current_page_source()

    def click_recent_charts_button_action(self):
        """
        动作：点击分享默认第一个user
        :return: 点击'分享默认第一个user'按钮后的页面
        """
        self.Android.click(self.recent_charts_button)
        return self.Android.get_current_page_source()

    def click_course_detail_goods_buy_button_action(self):
        """
        动作：点击购买按钮
        :return: 点击'购买按钮'按钮后的页面
        """
        self.Android.click(self.course_detail_goods_buy_button)
        return self.Android.get_current_page_source()

    def click_course_detail_dialog_goods_buy_button_action(self):
        """
        动作：点击直播讲座-立即购买
        :return: 点击'直播讲座-立即购买'按钮后的页面
        """
        self.Android.click(self.course_detail_dialog_goods_buy_button)
        return self.Android.get_current_page_source()

    def get_course_detail_title_text_action(self):
        """
        动作：获取课程标题的文本
        :return: '课程标题'的文本
        """
        control_content = self.course_detail_title_text.text.strip()
        return control_content

    # endregion Actions
