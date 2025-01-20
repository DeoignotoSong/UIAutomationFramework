from Utils.Log import log


'''
推荐：学长头条-文章详情
com.jinjilie.daxuezhang.functions.detail.activity.ArticleActivity
'''


class ArticleDetailPage:
    def __init__(self, project):
        self.Android = project

        # region Fields
        # 后退按钮
        self._article_detail_back_button_tag = '//*[@resource-id="com.jinjilie.daxuezhang.debug:id/header_left_iv"]'
        # 右上角option
        self._article_detail_right_option_button_tag = '//*[@resource-id="com.jinjilie.daxuezhang.debug:id/header_right_iv"]'
        # 文章标题
        self._article_detail_title_text_tag = '//*[@resource-id="default"]/android.view.View/android.view.View/android.view.View[1]/android.view.View[1]'
        # 学长头条
        self.__article_detail_stu_headlines_text_tag = "//*[@text='学长头条']"
        # 关注按钮
        self._article_detail_follow_text_tag = "//*[@text='关注']"
        # 在线咨询按钮
        self._article_detail_wechat_button_tag = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View[5]'
        # 描述文本
        self._article_detail_describe_text_tag = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View[6]'
        # 文章内容文本
        self._article_detail_content_text_tag = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View[7]/android.view.View'
        # 发表评论输入框
        self._article_detail_comment_input_tag = "//*[@text='发表评论...']"
        # 输入状态的评论输入框
        self._article_detail_comment_input_content_tag = "//*[@resource-id='com.jinjilie.daxuezhang.debug:id/et_content']"
        # 发送按钮
        self._article_detail_comment_send_button_tag = "//*[@resource-id='com.jinjilie.daxuezhang.debug:id/btn_send']"
        # 评论按钮
        self._article_detail_comment_button_tag =  '//*[@resource-id="com.jinjilie.daxuezhang.debug:id/detail_article_comment_iv"]'
        # 收藏按钮
        self._article_detail_collection_button_tag = '//*[@resource-id="com.jinjilie.daxuezhang.debug:id/detail_article_like_iv"]'
        # 文章点赞按钮
        self._article_detail_like_button_tag = '//*[@resource-id="com.jinjilie.daxuezhang.debug:id/detail_article_collection_iv"]'
        # 分享按钮
        self._article_detail_share_button_tag = '//*[@resource-id="com.jinjilie.daxuezhang.debug:id/detail_article_share_iv"]'
        # 分享微聊好友默认第一个人
        self._recent_charts_button_tag = '//*[@resource-id="com.jinjilie.daxuezhang.debug:id/rvRecentChats"]/android.widget.LinearLayout[1]'

        # endregion Fields

    # region Properties
    @property
    def article_detail_back_button(self):
        """
        属性: 后退按钮
        :return: 后退按钮
        """
        element = None
        try:
            element = self.Android.get_element(self._article_detail_back_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def article_detail_right_option_button(self):
        """
        属性: 右上角option
        :return: 右上角option
        """
        element = None
        try:
            element = self.Android.get_element(self._article_detail_right_option_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def article_detail_title_text(self):
        """
        属性: 文章标题
        :return: 文章标题
        """
        element = None
        try:
            element = self.Android.get_element(self._article_detail_title_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def _article_detail_stu_headlines_text(self):
        """
        属性: 学长头条
        :return: 学长头条
        """
        element = None
        try:
            element = self.Android.get_element(self.__article_detail_stu_headlines_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def article_detail_follow_text(self):
        """
        属性: 关注按钮
        :return: 关注按钮
        """
        element = None
        try:
            element = self.Android.get_element(self._article_detail_follow_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def article_detail_wechat_button(self):
        """
        属性: 在线咨询按钮
        :return: 在线咨询按钮
        """
        element = None
        try:
            element = self.Android.get_element(self._article_detail_wechat_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def article_detail_describe_text(self):
        """
        属性: 描述文本
        :return: 描述文本
        """
        element = None
        try:
            element = self.Android.get_element(self._article_detail_describe_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def article_detail_content_text(self):
        """
        属性: 文章内容文本
        :return: 文章内容文本
        """
        element = None
        try:
            element = self.Android.get_element(self._article_detail_content_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def article_detail_comment_input(self):
        """
        属性: 发表评论输入框
        :return: 发表评论输入框
        """
        element = None
        try:
            element = self.Android.get_element(self._article_detail_comment_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def article_detail_comment_input_content(self):
        """
        属性: 输入状态的评论输入框
        :return: 输入状态的评论输入框
        """
        element = None
        try:
            element = self.Android.get_element(self._article_detail_comment_input_content_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def article_detail_comment_send_button(self):
        """
        属性: 发送按钮
        :return: 发送按钮
        """
        element = None
        try:
            element = self.Android.get_element(self._article_detail_comment_send_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def article_detail_comment_button(self):
        """
        属性: 评论按钮
        :return: 评论按钮
        """
        element = None
        try:
            element = self.Android.get_element(self._article_detail_comment_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def article_detail_collection_button(self):
        """
        属性: 收藏按钮
        :return: 收藏按钮
        """
        element = None
        try:
            element = self.Android.get_element(self._article_detail_collection_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def article_detail_like_button(self):
        """
        属性: 文章点赞按钮
        :return: 文章点赞按钮
        """
        element = None
        try:
            element = self.Android.get_element(self._article_detail_like_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def article_detail_share_button(self):
        """
        属性: 分享按钮
        :return: 分享按钮
        """
        element = None
        try:
            element = self.Android.get_element(self._article_detail_share_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def recent_charts_button(self):
        """
        属性: 分享微聊好友默认第一个人
        :return: 分享微聊好友默认第一个人
        """
        element = None
        try:
            element = self.Android.get_element(self._recent_charts_button_tag)
        except AttributeError as error:
            log(error)
        return element

    # endregion Properties

    # region Actions
    def click_article_detail_back_button_action(self):
        """
        动作：点击后退按钮
        :return: 点击'后退按钮'按钮后的页面
        """
        self.Android.click(self.article_detail_back_button)
        return self.Android.get_current_page_source()

    def click_article_detail_right_option_button_action(self):
        """
        动作：点击右上角option
        :return: 点击'右上角option'按钮后的页面
        """
        self.Android.click(self.article_detail_right_option_button)
        return self.Android.get_current_page_source()

    def get_article_detail_title_text_action(self):
        """
        动作：获取文章标题的文本
        :return: '文章标题'的文本
        """
        control_content = self.article_detail_title_text.text.strip()
        return control_content

    def get__article_detail_stu_headlines_text_action(self):
        """
        动作：获取学长头条的文本
        :return: '学长头条'的文本
        """
        control_content = self._article_detail_stu_headlines_text.text.strip()
        return control_content

    def get_article_detail_follow_text_action(self):
        """
        动作：获取关注按钮的文本
        :return: '关注按钮'的文本
        """
        control_content = self.article_detail_follow_text.text.strip()
        return control_content

    def click_article_detail_wechat_button_action(self):
        """
        动作：点击在线咨询按钮
        :return: 点击'在线咨询按钮'按钮后的页面
        """
        self.Android.click(self.article_detail_wechat_button)
        return self.Android.get_current_page_source()

    def get_article_detail_describe_text_action(self):
        """
        动作：获取描述文本的文本
        :return: '描述文本'的文本
        """
        control_content = self.article_detail_describe_text.text.strip()
        return control_content

    def get_article_detail_content_text_action(self):
        """
        动作：获取文章内容文本的文本
        :return: '文章内容文本'的文本
        """
        control_content = self.article_detail_content_text.text.strip()
        return control_content

    def set_article_detail_comment_input_action(self, article_detail_comment_input):
        """
        动作：设置发表评论输入框
        :param article_detail_comment_input: 发表评论输入框
        :return: 设置'发表评论输入框'文本后的页面
        """
        self.Android.clear_and_send_keys(self.article_detail_comment_input, article_detail_comment_input)
        return self.Android.get_current_page_source()

    def click_article_detail_comment_send_button_action(self):
        """
        动作：点击发送按钮
        :return: 点击'发送按钮'按钮后的页面
        """
        self.Android.click(self.article_detail_comment_send_button)
        return self.Android.get_current_page_source()

    def click_article_detail_comment_button_action(self):
        """
        动作：点击评论按钮
        :return: 点击'评论按钮'按钮后的页面
        """
        self.Android.click(self.article_detail_comment_button)
        return self.Android.get_current_page_source()

    def click_article_detail_collection_button_action(self):
        """
        动作：点击收藏按钮
        :return: 点击'收藏按钮'按钮后的页面
        """
        self.Android.click(self.article_detail_collection_button)
        return self.Android.get_current_page_source()

    def click_article_detail_like_button_action(self):
        """
        动作：点击文章点赞按钮
        :return: 点击'文章点赞按钮'按钮后的页面
        """
        self.Android.click(self.article_detail_like_button)
        return self.Android.get_current_page_source()

    def click_article_detail_share_button_action(self):
        """
        动作：点击分享按钮
        :return: 点击'分享按钮'按钮后的页面
        """
        self.Android.click(self.article_detail_share_button)
        return self.Android.get_current_page_source()

    def click_recent_charts_button_action(self):
        """
        动作：点击分享微聊好友默认第一个人
        :return: 点击'分享微聊好友默认第一个人'按钮后的页面
        """
        self.Android.click(self.recent_charts_button)
        return self.Android.get_current_page_source()

    # endregion Actions
