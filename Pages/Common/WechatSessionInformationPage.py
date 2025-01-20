from Utils.Log import log


'''
微聊内容-会话信息页面
com.jinjilie.daxuezhang.functions.detail.activity.ArticleActivity
'''


class WechatSessionInformationPage:
    def __init__(self, project):
        self.Android = project

        # region Fields
        # 好友头像
        self._charts_icon_button_tag = '//*[@resource-id="com.jinjilie.daxuezhang.debug:id/bytedesk_message_item_header"]'

        # endregion Fields

    # region Properties
    @property
    def charts_icon_button(self):
        """
        属性: 好友头像
        :return: 好友头像
        """
        element = None
        try:
            element = self.Android.get_element(self._charts_icon_button_tag)
        except AttributeError as error:
            log(error)
        return element

    # endregion Properties

    # region Actions
    def click_charts_icon_button_action(self):
        """
        动作：点击好友头像
        :return: 点击'好友头像'按钮后的页面
        """
        self.Android.click(self.charts_icon_button)
        return self.Android.get_current_page_source()

    # endregion Actions
