from Utils.Log import log


'''
APP内部通用对话框
com.jinjilie.daxuezhang.functions.MainActivity
'''


class AppCommonDialogPage:

    def __init__(self, project):
        self.Android = project
        # region Fields
        # 版本关闭按钮
        self._version_close_button_tag = "//*[@resource-id='com.jinjilie.daxuezhang.debug:id/version_close_iv']"
        # 广告关闭按钮
        self._ad_close_button_tag = "//*[@resource-id='com.jinjilie.daxuezhang.debug:id/ad_close_iv']"
        # 签到成功分享卡片closed按钮
        self._share_close_button_tag = "//*[@resource-id='com.jinjilie.daxuezhang.debug:id/share_close_iv']"
        # 立即签到button
        self._signed_button_tag = "//*[@resource-id='com.jinjilie.daxuezhang.debug:id/sign_to_signed_tv']"
        # 签到成功卡片
        self._signed_success_card_tag = "//*[@resource-id='com.jinjilie.daxuezhang.debug:id/signed_card_rl']"
        # 分享发送按钮
        self._shared_send_button_tag = "//*[@resource-id='com.jinjilie.daxuezhang.debug:id/btnSend']"
        # loading对话框
        self._loading_tag = "//*[@text='加载中...']"
        # 退出登录-对话框-退出
        self._logout_closed_button_tag = "//*[@text='狠心离开']"
        # 点赞提示对话框
        self._dian_zan_tag = "//*[@text='点赞成功']"
        # 文章收藏、点赞对话框-提示文案
        self._article_dialog_prompt_describe_tag = "//*[@resource-id='com.jinjilie.daxuezhang.debug:id/integral_title_tv']"
        # 防沉迷对话框
        self._i_know_text_tag = "//*[@text='我知道了']"
        # endregion Fields

    # region Properties
    @property
    def version_close_button(self):
        """
        属性: 版本关闭按钮
        :return: 版本关闭按钮
        """
        element = None
        try:
            element = self.Android.get_element(self._version_close_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def ad_close_button(self):
        """
        属性: 广告关闭按钮
        :return: 广告关闭按钮
        """
        element = None
        try:
            element = self.Android.get_element(self._ad_close_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def share_close_button(self):
        """
        属性: 签到成功分享卡片closed按钮
        :return: 签到成功分享卡片closed按钮
        """
        element = None
        try:
            element = self.Android.get_element(self._share_close_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def signed_button(self):
        """
        属性: 立即签到button
        :return: 立即签到button
        """
        element = None
        try:
            element = self.Android.get_element(self._signed_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def signed_success_card(self):
        """
        属性: 签到成功卡片
        :return: 签到成功卡片
        """
        element = None
        try:
            element = self.Android.get_element(self._signed_success_card_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def shared_send_button(self):
        """
        属性: 分享发送按钮
        :return: 分享发送按钮
        """
        element = None
        try:
            element = self.Android.get_element(self._shared_send_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def loading(self):
        """
        属性: loading对话框
        :return: loading对话框
        """
        element = None
        try:
            element = self.Android.get_element(self._loading_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def logout_closed_button(self):
        """
        属性: 退出登录-对话框-退出
        :return: 退出登录-对话框-退出
        """
        element = None
        try:
            element = self.Android.get_element(self._logout_closed_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def dian_zan(self):
        """
        属性: 点赞提示对话框
        :return: 点赞提示对话框
        """
        element = None
        try:
            element = self.Android.get_element(self._dian_zan_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def article_dialog_prompt_describe(self):
        """
        属性: 文章收藏、点赞对话框-提示文案
        :return: 文章收藏、点赞对话框-提示文案
        """
        element = None
        try:
            element = self.Android.get_element(self._article_dialog_prompt_describe_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def i_know_text(self):
        """
        属性: 防沉迷对话框
        :return: 防沉迷对话框
        """
        element = None
        try:
            element = self.Android.get_element(self._i_know_text_tag)
        except AttributeError as error:
            log(error)
        return element

    # endregion Properties

    # region Actions
    def click_version_close_button_action(self):
        """
        动作：点击版本关闭按钮
        :return: 点击'版本关闭按钮'按钮后的页面
        """
        self.Android.click(self.version_close_button)
        return self.Android.get_current_page_source()

    def click_ad_close_button_action(self):
        """
        动作：点击广告关闭按钮
        :return: 点击'广告关闭按钮'按钮后的页面
        """
        self.Android.click(self.ad_close_button)
        return self.Android.get_current_page_source()

    def click_share_close_button_action(self):
        """
        动作：点击签到成功分享卡片closed按钮
        :return: 点击'签到成功分享卡片closed按钮'按钮后的页面
        """
        self.Android.click(self.share_close_button)
        return self.Android.get_current_page_source()

    def click_signed_button_action(self):
        """
        动作：点击立即签到button
        :return: 点击'立即签到button'按钮后的页面
        """
        self.Android.click(self.signed_button)
        return self.Android.get_current_page_source()

    def click_shared_send_button_action(self):
        """
        动作：点击分享发送按钮
        :return: 点击'分享发送按钮'按钮后的页面
        """
        self.Android.click(self.shared_send_button)
        return self.Android.get_current_page_source()

    def click_logout_closed_button_action(self):
        """
        动作：点击退出登录-对话框-退出
        :return: 点击'退出登录-对话框-退出'按钮后的页面
        """
        self.Android.click(self.logout_closed_button)
        return self.Android.get_current_page_source()

    def get_i_know_text_action(self):
        """
        动作：获取防沉迷对话框的文本
        :return: '防沉迷对话框'的文本
        """
        control_content = self.i_know_text.text.strip()
        return control_content

    # endregion Actions
