from Utils.Log import log


'''
首页综合搜索结果页面
com.jinjilie.daxuezhang.functions.MainActivity
'''


class SearchResultPage:

    def __init__(self, project):
        self.Android = project
        # region Fields
        # 搜索按钮
        self._search_button_tag = "//*[@resource-id='com.jinjilie.daxuezhang.debug:id/search_tv']"
        # 搜索栏
        self._search_bar_button_tag = "//*[@resource-id='com.jinjilie.daxuezhang.debug:id/search_et']"
        # 找文章
        self._search_result_article_button_tag = "//*[@text='找文章']"
        # 找课程
        self._search_result_class_button_tag = "//*[@text='找课程']"
        # 找讲座
        self._search_result_lecture_button_tag = "//*[@text='找讲座']"
        # 找学校
        self._search_result_college_button_tag = "//*[@text='找学校']"
        # 找问答
        self._search_result_question_button_tag = "//*[@text='找问答']"
        # 找老师
        self._search_result_teacher_button_tag = "//*[@text='找老师']"
        # 找问答-第一条结果
        self._search_result_question_first_item_tag = "//*[@resource-id='com.jinjilie.daxuezhang.debug:id/rv']/android.widget.LinearLayout[1]/android.widget.TextView"
        # 找老师-第一条结果
        self._search_result_teacher_first_item_tag = "//*[@resource-id='com.jinjilie.daxuezhang.debug:id/rv']/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]/android.widget.TextView[1]"
        # 搜索文章标题id
        self._search_result_title_text_tag = "//*[@resource-id='com.jinjilie.daxuezhang.debug:id/item_article_title_rl']"
        # 搜索结果-课程标题
        self._search_result_course_title_text_tag = "//*[@resource-id='com.jinjilie.daxuezhang.debug:id/item_course_title_tv']"
        # 搜索结果-讲座标题
        self._search_result_lecture_title_text_tag = "//*[@resource-id='com.jinjilie.daxuezhang.debug:id/item_lecture_title_tv']"
        # 搜索结果-学校标题
        self._search_result_college_title_text_tag = "//*[@resource-id='com.jinjilie.daxuezhang.debug:id/item_college_name_tv']"
        # 搜索结果-找老师
        self._search_result_teacher_title_text_tag = "//*[@resource-id='com.jinjilie.daxuezhang.debug:id/item_export_name_tv']"
        # 筛选按钮
        self._search_result_search_sort_button_tag = "//*[@resource-id='com.jinjilie.daxuezhang.debug:id/search_border_right_sort_ll']"
        # 确定按钮
        self._search_result_submit_button_tag = "//*[@resource-id='com.jinjilie.daxuezhang.debug:id/btn_ensure']"
        # 价格标签
        self._price_button_tag = "//*[@text='价格']"
        # 开播时间
        self._begin_time_button_tag = "//*[@text='开播时间']"
        # endregion Fields

    # region Properties
    @property
    def search_button(self):
        """
        属性: 搜索按钮
        :return: 搜索按钮
        """
        element = None
        try:
            element = self.Android.get_element(self._search_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def search_bar_button(self):
        """
        属性: 搜索栏
        :return: 搜索栏
        """
        element = None
        try:
            element = self.Android.get_element(self._search_bar_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def search_result_article_button(self):
        """
        属性: 找文章
        :return: 找文章
        """
        element = None
        try:
            element = self.Android.get_element(self._search_result_article_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def search_result_class_button(self):
        """
        属性: 找课程
        :return: 找课程
        """
        element = None
        try:
            element = self.Android.get_element(self._search_result_class_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def search_result_lecture_button(self):
        """
        属性: 找讲座
        :return: 找讲座
        """
        element = None
        try:
            element = self.Android.get_element(self._search_result_lecture_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def search_result_college_button(self):
        """
        属性: 找学校
        :return: 找学校
        """
        element = None
        try:
            element = self.Android.get_element(self._search_result_college_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def search_result_question_button(self):
        """
        属性: 找问答
        :return: 找问答
        """
        element = None
        try:
            element = self.Android.get_element(self._search_result_question_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def search_result_teacher_button(self):
        """
        属性: 找老师
        :return: 找老师
        """
        element = None
        try:
            element = self.Android.get_element(self._search_result_teacher_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def search_result_question_first_item(self):
        """
        属性: 找问答-第一条结果
        :return: 找问答-第一条结果
        """
        element = None
        try:
            element = self.Android.get_element(self._search_result_question_first_item_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def search_result_teacher_first_item(self):
        """
        属性: 找老师-第一条结果
        :return: 找老师-第一条结果
        """
        element = None
        try:
            element = self.Android.get_element(self._search_result_teacher_first_item_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def search_result_title_text(self):
        """
        属性: 搜索文章标题id
        :return: 搜索文章标题id
        """
        element = None
        try:
            element = self.Android.get_element(self._search_result_title_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def search_result_course_title_text(self):
        """
        属性: 搜索结果-课程标题
        :return: 搜索结果-课程标题
        """
        element = None
        try:
            element = self.Android.get_element(self._search_result_course_title_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def search_result_lecture_title_text(self):
        """
        属性: 搜索结果-讲座标题
        :return: 搜索结果-讲座标题
        """
        element = None
        try:
            element = self.Android.get_element(self._search_result_lecture_title_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def search_result_college_title_text(self):
        """
        属性: 搜索结果-学校标题
        :return: 搜索结果-学校标题
        """
        element = None
        try:
            element = self.Android.get_element(self._search_result_college_title_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def search_result_teacher_title_text(self):
        """
        属性: 搜索结果-找老师
        :return: 搜索结果-找老师
        """
        element = None
        try:
            element = self.Android.get_element(self._search_result_teacher_title_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def search_result_search_sort_button(self):
        """
        属性: 筛选按钮
        :return: 筛选按钮
        """
        element = None
        try:
            element = self.Android.get_element(self._search_result_search_sort_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def search_result_submit_button(self):
        """
        属性: 确定按钮
        :return: 确定按钮
        """
        element = None
        try:
            element = self.Android.get_element(self._search_result_submit_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def price_button(self):
        """
        属性: 价格标签
        :return: 价格标签
        """
        element = None
        try:
            element = self.Android.get_element(self._price_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def begin_time_button(self):
        """
        属性: 开播时间
        :return: 开播时间
        """
        element = None
        try:
            element = self.Android.get_element(self._begin_time_button_tag)
        except AttributeError as error:
            log(error)
        return element

    # endregion Properties

    # region Actions
    def click_search_button_action(self):
        """
        动作：点击搜索按钮
        :return: 点击'搜索按钮'按钮后的页面
        """
        self.Android.click(self.search_button)
        return self.Android.get_current_page_source()

    def click_search_bar_button_action(self):
        """
        动作：点击搜索栏
        :return: 点击'搜索栏'按钮后的页面
        """
        self.Android.click(self.search_bar_button)
        return self.Android.get_current_page_source()

    def click_search_result_article_button_action(self):
        """
        动作：点击找文章
        :return: 点击'找文章'按钮后的页面
        """
        self.Android.click(self.search_result_article_button)
        return self.Android.get_current_page_source()

    def click_search_result_class_button_action(self):
        """
        动作：点击找课程
        :return: 点击'找课程'按钮后的页面
        """
        self.Android.click(self.search_result_class_button)
        return self.Android.get_current_page_source()

    def click_search_result_lecture_button_action(self):
        """
        动作：点击找讲座
        :return: 点击'找讲座'按钮后的页面
        """
        self.Android.click(self.search_result_lecture_button)
        return self.Android.get_current_page_source()

    def click_search_result_college_button_action(self):
        """
        动作：点击找学校
        :return: 点击'找学校'按钮后的页面
        """
        self.Android.click(self.search_result_college_button)
        return self.Android.get_current_page_source()

    def click_search_result_question_button_action(self):
        """
        动作：点击找问答
        :return: 点击'找问答'按钮后的页面
        """
        self.Android.click(self.search_result_question_button)
        return self.Android.get_current_page_source()

    def click_search_result_teacher_button_action(self):
        """
        动作：点击找老师
        :return: 点击'找老师'按钮后的页面
        """
        self.Android.click(self.search_result_teacher_button)
        return self.Android.get_current_page_source()

    def get_search_result_title_text_action(self):
        """
        动作：获取搜索文章标题id的文本
        :return: '搜索文章标题id'的文本
        """
        control_content = self.search_result_title_text.text.strip()
        return control_content

    def get_search_result_course_title_text_action(self):
        """
        动作：获取搜索结果-课程标题的文本
        :return: '搜索结果-课程标题'的文本
        """
        control_content = self.search_result_course_title_text.text.strip()
        return control_content

    def get_search_result_lecture_title_text_action(self):
        """
        动作：获取搜索结果-讲座标题的文本
        :return: '搜索结果-讲座标题'的文本
        """
        control_content = self.search_result_lecture_title_text.text.strip()
        return control_content

    def get_search_result_college_title_text_action(self):
        """
        动作：获取搜索结果-学校标题的文本
        :return: '搜索结果-学校标题'的文本
        """
        control_content = self.search_result_college_title_text.text.strip()
        return control_content

    def get_search_result_teacher_title_text_action(self):
        """
        动作：获取搜索结果-找老师的文本
        :return: '搜索结果-找老师'的文本
        """
        control_content = self.search_result_teacher_title_text.text.strip()
        return control_content

    def click_search_result_search_sort_button_action(self):
        """
        动作：点击筛选按钮
        :return: 点击'筛选按钮'按钮后的页面
        """
        self.Android.click(self.search_result_search_sort_button)
        return self.Android.get_current_page_source()

    def click_search_result_submit_button_action(self):
        """
        动作：点击确定按钮
        :return: 点击'确定按钮'按钮后的页面
        """
        self.Android.click(self.search_result_submit_button)
        return self.Android.get_current_page_source()

    def click_price_button_action(self):
        """
        动作：点击价格标签
        :return: 点击'价格标签'按钮后的页面
        """
        self.Android.click(self.price_button)
        return self.Android.get_current_page_source()

    def click_begin_time_button_action(self):
        """
        动作：点击开播时间
        :return: 点击'开播时间'按钮后的页面
        """
        self.Android.click(self.begin_time_button)
        return self.Android.get_current_page_source()

    # endregion Actions
