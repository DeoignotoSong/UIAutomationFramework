from Utils.Log import log

"""
后台首页-审核中心-审核管理-文章管理
console_url/audit_manage/article
"""


class ConsoleAuditManageArticlePage:
    def __init__(self, project):
        self.project = project
        self.url = 'console_url/audit_manage/article'
        # region Fields
        # 消息提示
        self._message_content_text_tag = '/html/body/div[last()]/div/div[1]/p'
        # 下拉菜单
        self._drop_down_list_select_tag = '/html/body/div[@x-placement="bottom-start"]/div[1]/div[1]/ul'
        # 搜索文章ID输入框
        self._search_article_id_input_tag = '//*[@id="tableSearch"]/form/div/div[1]/div/div/input'
        # 搜索文章标题输入框
        self._search_article_title_input_tag = '//*[@id="tableSearch"]/form/div/div[2]/div/div/input'
        # 查询按钮
        self._search_button_tag = '//*[@id="tableSearch"]/form/div/div[last()-1]/div/button'
        # 清楚按钮
        self._clear_button_tag = '//*[@id="tableSearch"]/form/div/div[last()]/div/button'
        # 列表-第一行-第一个按钮
        self._list_first_exe_first_button_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div[1]/div[4]/div[2]/table/tbody/tr[1]/td[last()]/div/a[1]'
        # 列表-第一行-审核状态
        self._list_first_examine_state_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[10]/div'
        # 文章详情-文章标题
        self._article_detail_article_title_text_tag = '//*[@id="app"]/div/section/main/div/section/main/div[1]/div[1]'
        # 文章详情-文章ID
        self._article_detail_article_id_text_tag = '//*[@id="app"]/div/section/main/div/section/main/div[1]/div[2]'
        # 文章详情-文章审核状态
        self._article_detail_review_state_text_tag = '//*[@id="app"]/div/section/main/div/section/main/div[1]/div[3]'
        # 文章详情-简述
        self._article_detail_description_text_tag = '//*[@id="app"]/div/section/main/div/section/main/div[2]/div[1]'
        # 文章详情-正文
        self._article_detail_main_content_text_tag = '//*[@id="app"]/div/section/main/div/section/main/div[2]/div[3]'
        # 文章详情-发布人
        self._article_detail_publisher_text_tag = '//*[@id="app"]/div/section/main/div/section/aside/div[1]/div[2]/p[1]'
        # 文章详情-发布时间
        self._article_detail_created_at_tag = '//*[@id="app"]/div/section/main/div/section/aside/div[2]'
        # 文章详情-标签-第一个
        self._article_detail_label_first_text_tag = '//*[@id="app"]/div/section/main/div/section/aside/div[3]/div[1]/div'
        # 文章详情-标签-第二个
        self._article_detail_label_second_text_tag = '//*[@id="app"]/div/section/main/div/section/aside/div[3]/div[2]/div'
        # 文章详情-标签-第三个
        self._article_detail_label_third_text_tag = '//*[@id="app"]/div/section/main/div/section/aside/div[3]/div[3]/div'
        # 文章详情-标签-第四个
        self._article_detail_label_fourth_text_tag = '//*[@id="app"]/div/section/main/div/section/aside/div[3]/div[4]/div'
        # 文章详情-标签-最后一个
        self._article_detail_label_last_text_tag = '//*[@id="app"]/div/section/main/div/section/aside/div[3]/div[last()]/div'
        # 文章详情-驳回理由-类型-文字
        self._article_detail_no_pass_reason_type_words_button_tag = '//*[@id="app"]/div/section/main/div/section/aside/div[4]/div[2]/label[1]'
        # 文章详情-驳回理由-类型-图片
        self._article_detail_no_pass_reason_type_image_button_tag = '//*[@id="app"]/div/section/main/div/section/aside/div[4]/div[2]/label[2]'
        # 文章详情-驳回理由-类型-视频
        self._article_detail_no_pass_reason_type_video_button_tag = '//*[@id="app"]/div/section/main/div/section/aside/div[4]/div[2]/label[3]'
        # 文章详情-驳回理由-列表-第一个
        self._article_detail_no_pass_reason_list_first_button_tag = '//*[@id="app"]/div/section/main/div/section/aside/div[4]/div[3]/div/label[@style=""][1]'
        # 文章详情-驳回理由-列表-第二个
        self._article_detail_no_pass_reason_list_second_button_tag = '//*[@id="app"]/div/section/main/div/section/aside/div[4]/div[3]/div/label[@style=""][2]'
        # 文章详情-通过理由-列表-第一个
        self._article_detail_pass_reason_list_first_button_tag = '//*[@id="app"]/div/section/main/div/section/aside/div[5]/label'
        # 文章详情=提交
        self._article_detail_commit_button_tag = '/html/body/div/div/section/main/div/section/aside/div[6]/div[2]/button'
        # 文章详情-提交确认弹窗-标题
        self._article_detail_commit_popup_title_text_tag = '/html/body/div[@role="dialog"]/div/div[1]/div/span'
        # 文章详情-提交确认弹窗-提示
        self._article_detail_commit_popup_tip_text_tag = '/html/body/div[@role="dialog"]/div/div[2]/div[1]/div[2]/p'
        # 文章详情-提交确认弹窗-确认
        self._article_detail_commit_popup_confirm_button_tag = '/html/body/div[@role="dialog"]/div/div[3]/button[2]'
        # 文章详情-提交确认弹窗-取消
        self._article_detail_commit_popup_cancel_button_tag = '/html/body/div[@role="dialog"]/div/div[3]/button[1]'
        # 文章详情-提交确认弹窗-关闭
        self._article_detail_commit_popup_close_button_tag = '/html/body/div[@role="dialog"]/div/div[1]/button'
        # endregion Fields

    # region Properties
    @property
    def message_content_text(self):
        """
        属性: 消息提示
        :return: 消息提示
        """
        element = None
        try:
            element = self.project.get_element(self._message_content_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def drop_down_list_select(self):
        """
        属性: 下拉菜单
        :return: 下拉菜单
        """
        element = None
        try:
            element = self.project.get_element(self._drop_down_list_select_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def search_article_id_input(self):
        """
        属性: 搜索文章ID输入框
        :return: 搜索文章ID输入框
        """
        element = None
        try:
            element = self.project.get_element(self._search_article_id_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def search_article_title_input(self):
        """
        属性: 搜索文章标题输入框
        :return: 搜索文章标题输入框
        """
        element = None
        try:
            element = self.project.get_element(self._search_article_title_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def search_button(self):
        """
        属性: 查询按钮
        :return: 查询按钮
        """
        element = None
        try:
            element = self.project.get_element(self._search_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def clear_button(self):
        """
        属性: 清楚按钮
        :return: 清楚按钮
        """
        element = None
        try:
            element = self.project.get_element(self._clear_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def list_first_exe_first_button(self):
        """
        属性: 列表-第一行-第一个按钮
        :return: 列表-第一行-第一个按钮
        """
        element = None
        try:
            element = self.project.get_element(self._list_first_exe_first_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def list_first_examine_state_text(self):
        """
        属性: 列表-第一行-审核状态
        :return: 列表-第一行-审核状态
        """
        element = None
        try:
            element = self.project.get_element(self._list_first_examine_state_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def article_detail_article_title_text(self):
        """
        属性: 文章详情-文章标题
        :return: 文章详情-文章标题
        """
        element = None
        try:
            element = self.project.get_element(self._article_detail_article_title_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def article_detail_article_id_text(self):
        """
        属性: 文章详情-文章ID
        :return: 文章详情-文章ID
        """
        element = None
        try:
            element = self.project.get_element(self._article_detail_article_id_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def article_detail_review_state_text(self):
        """
        属性: 文章详情-文章审核状态
        :return: 文章详情-文章审核状态
        """
        element = None
        try:
            element = self.project.get_element(self._article_detail_review_state_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def article_detail_description_text(self):
        """
        属性: 文章详情-简述
        :return: 文章详情-简述
        """
        element = None
        try:
            element = self.project.get_element(self._article_detail_description_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def article_detail_main_content_text(self):
        """
        属性: 文章详情-正文
        :return: 文章详情-正文
        """
        element = None
        try:
            element = self.project.get_element(self._article_detail_main_content_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def article_detail_publisher_text(self):
        """
        属性: 文章详情-发布人
        :return: 文章详情-发布人
        """
        element = None
        try:
            element = self.project.get_element(self._article_detail_publisher_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def article_detail_created_at(self):
        """
        属性: 文章详情-发布时间
        :return: 文章详情-发布时间
        """
        element = None
        try:
            element = self.project.get_element(self._article_detail_created_at_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def article_detail_label_first_text(self):
        """
        属性: 文章详情-标签-第一个
        :return: 文章详情-标签-第一个
        """
        element = None
        try:
            element = self.project.get_element(self._article_detail_label_first_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def article_detail_label_second_text(self):
        """
        属性: 文章详情-标签-第二个
        :return: 文章详情-标签-第二个
        """
        element = None
        try:
            element = self.project.get_element(self._article_detail_label_second_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def article_detail_label_third_text(self):
        """
        属性: 文章详情-标签-第三个
        :return: 文章详情-标签-第三个
        """
        element = None
        try:
            element = self.project.get_element(self._article_detail_label_third_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def article_detail_label_fourth_text(self):
        """
        属性: 文章详情-标签-第四个
        :return: 文章详情-标签-第四个
        """
        element = None
        try:
            element = self.project.get_element(self._article_detail_label_fourth_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def article_detail_label_last_text(self):
        """
        属性: 文章详情-标签-最后一个
        :return: 文章详情-标签-最后一个
        """
        element = None
        try:
            element = self.project.get_element(self._article_detail_label_last_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def article_detail_no_pass_reason_type_words_button(self):
        """
        属性: 文章详情-驳回理由-类型-文字
        :return: 文章详情-驳回理由-类型-文字
        """
        element = None
        try:
            element = self.project.get_element(self._article_detail_no_pass_reason_type_words_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def article_detail_no_pass_reason_type_image_button(self):
        """
        属性: 文章详情-驳回理由-类型-图片
        :return: 文章详情-驳回理由-类型-图片
        """
        element = None
        try:
            element = self.project.get_element(self._article_detail_no_pass_reason_type_image_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def article_detail_no_pass_reason_type_video_button(self):
        """
        属性: 文章详情-驳回理由-类型-视频
        :return: 文章详情-驳回理由-类型-视频
        """
        element = None
        try:
            element = self.project.get_element(self._article_detail_no_pass_reason_type_video_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def article_detail_no_pass_reason_list_first_button(self):
        """
        属性: 文章详情-驳回理由-列表-第一个
        :return: 文章详情-驳回理由-列表-第一个
        """
        element = None
        try:
            element = self.project.get_element(self._article_detail_no_pass_reason_list_first_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def article_detail_no_pass_reason_list_second_button(self):
        """
        属性: 文章详情-驳回理由-列表-第二个
        :return: 文章详情-驳回理由-列表-第二个
        """
        element = None
        try:
            element = self.project.get_element(self._article_detail_no_pass_reason_list_second_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def article_detail_pass_reason_list_first_button(self):
        """
        属性: 文章详情-通过理由-列表-第一个
        :return: 文章详情-通过理由-列表-第一个
        """
        element = None
        try:
            element = self.project.get_element(self._article_detail_pass_reason_list_first_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def article_detail_commit_button(self):
        """
        属性: 文章详情=提交
        :return: 文章详情=提交
        """
        element = None
        try:
            element = self.project.get_element(self._article_detail_commit_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def article_detail_commit_popup_title_text(self):
        """
        属性: 文章详情-提交确认弹窗-标题
        :return: 文章详情-提交确认弹窗-标题
        """
        element = None
        try:
            element = self.project.get_element(self._article_detail_commit_popup_title_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def article_detail_commit_popup_tip_text(self):
        """
        属性: 文章详情-提交确认弹窗-提示
        :return: 文章详情-提交确认弹窗-提示
        """
        element = None
        try:
            element = self.project.get_element(self._article_detail_commit_popup_tip_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def article_detail_commit_popup_confirm_button(self):
        """
        属性: 文章详情-提交确认弹窗-确认
        :return: 文章详情-提交确认弹窗-确认
        """
        element = None
        try:
            element = self.project.get_element(self._article_detail_commit_popup_confirm_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def article_detail_commit_popup_cancel_button(self):
        """
        属性: 文章详情-提交确认弹窗-取消
        :return: 文章详情-提交确认弹窗-取消
        """
        element = None
        try:
            element = self.project.get_element(self._article_detail_commit_popup_cancel_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def article_detail_commit_popup_close_button(self):
        """
        属性: 文章详情-提交确认弹窗-关闭
        :return: 文章详情-提交确认弹窗-关闭
        """
        element = None
        try:
            element = self.project.get_element(self._article_detail_commit_popup_close_button_tag)
        except AttributeError as error:
            log(error)
        return element

    # endregion Properties

    # region Actions
    def get_message_content_text_action(self):
        """
        动作：获取消息提示的文本
        :return: '消息提示'的文本
        """
        control_content = self.project.get_element_text(self.message_content_text)
        return control_content

    def get_select_drop_down_list_action(self, drop_down_list_select):
        """
        动作：获取下拉菜单列表选中的文本
        :param drop_down_list_select: 下拉菜单列表索引或文本
        :return: '下拉菜单'的文本
        """
        control_content = self.project.get_select_content(self.drop_down_list_select, drop_down_list_select)
        return control_content

    def select_drop_down_list_action(self, drop_down_list_select):
        """
        动作：选择下拉菜单
        :param drop_down_list_select: 下拉菜单列表索引或文本
        :return: 选择'下拉菜单'选择器后的页面
        """
        self.project.select_control(self.drop_down_list_select, drop_down_list_select)
        return self.project.get_current_page_source()

    def set_search_article_id_input_action(self, search_article_id_input):
        """
        动作：设置搜索文章ID输入框
        :param search_article_id_input: 搜索文章ID输入框
        :return: 设置'搜索文章ID输入框'文本后的页面
        """
        self.project.clear_and_send_keys(self.search_article_id_input, search_article_id_input)
        return self.project.get_current_page_source()

    def set_search_article_title_input_action(self, search_article_title_input):
        """
        动作：设置搜索文章标题输入框
        :param search_article_title_input: 搜索文章标题输入框
        :return: 设置'搜索文章标题输入框'文本后的页面
        """
        self.project.clear_and_send_keys(self.search_article_title_input, search_article_title_input)
        return self.project.get_current_page_source()

    def click_search_button_action(self):
        """
        动作：点击查询按钮
        :return: 点击'查询按钮'按钮后的页面
        """
        self.project.click(self.search_button)
        return self.project.get_current_page_source()

    def click_clear_button_action(self):
        """
        动作：点击清楚按钮
        :return: 点击'清楚按钮'按钮后的页面
        """
        self.project.click(self.clear_button)
        return self.project.get_current_page_source()

    def click_list_first_exe_first_button_action(self):
        """
        动作：点击列表-第一行-第一个按钮
        :return: 点击'列表-第一行-第一个按钮'按钮后的页面
        """
        self.project.click(self.list_first_exe_first_button)
        return self.project.get_current_page_source()

    def get_list_first_examine_state_text_action(self):
        """
        动作：获取列表-第一行-审核状态的文本
        :return: '列表-第一行-审核状态'的文本
        """
        control_content = self.project.get_element_text(self.list_first_examine_state_text)
        return control_content

    def get_article_detail_article_title_text_action(self):
        """
        动作：获取文章详情-文章标题的文本
        :return: '文章详情-文章标题'的文本
        """
        control_content = self.project.get_element_text(self.article_detail_article_title_text)
        return control_content

    def get_article_detail_article_id_text_action(self):
        """
        动作：获取文章详情-文章ID的文本
        :return: '文章详情-文章ID'的文本
        """
        control_content = self.project.get_element_text(self.article_detail_article_id_text)
        return control_content

    def get_article_detail_review_state_text_action(self):
        """
        动作：获取文章详情-文章审核状态的文本
        :return: '文章详情-文章审核状态'的文本
        """
        control_content = self.project.get_element_text(self.article_detail_review_state_text)
        return control_content

    def get_article_detail_description_text_action(self):
        """
        动作：获取文章详情-简述的文本
        :return: '文章详情-简述'的文本
        """
        control_content = self.project.get_element_text(self.article_detail_description_text)
        return control_content

    def get_article_detail_main_content_text_action(self):
        """
        动作：获取文章详情-正文的文本
        :return: '文章详情-正文'的文本
        """
        control_content = self.project.get_element_text(self.article_detail_main_content_text)
        return control_content

    def get_article_detail_publisher_text_action(self):
        """
        动作：获取文章详情-发布人的文本
        :return: '文章详情-发布人'的文本
        """
        control_content = self.project.get_element_text(self.article_detail_publisher_text)
        return control_content

    def get_article_detail_label_first_text_action(self):
        """
        动作：获取文章详情-标签-第一个的文本
        :return: '文章详情-标签-第一个'的文本
        """
        control_content = self.project.get_element_text(self.article_detail_label_first_text)
        return control_content

    def get_article_detail_label_second_text_action(self):
        """
        动作：获取文章详情-标签-第二个的文本
        :return: '文章详情-标签-第二个'的文本
        """
        control_content = self.project.get_element_text(self.article_detail_label_second_text)
        return control_content

    def get_article_detail_label_third_text_action(self):
        """
        动作：获取文章详情-标签-第三个的文本
        :return: '文章详情-标签-第三个'的文本
        """
        control_content = self.project.get_element_text(self.article_detail_label_third_text)
        return control_content

    def get_article_detail_label_fourth_text_action(self):
        """
        动作：获取文章详情-标签-第四个的文本
        :return: '文章详情-标签-第四个'的文本
        """
        control_content = self.project.get_element_text(self.article_detail_label_fourth_text)
        return control_content

    def get_article_detail_label_last_text_action(self):
        """
        动作：获取文章详情-标签-最后一个的文本
        :return: '文章详情-标签-最后一个'的文本
        """
        control_content = self.project.get_element_text(self.article_detail_label_last_text)
        return control_content

    def click_article_detail_no_pass_reason_type_words_button_action(self):
        """
        动作：点击文章详情-驳回理由-类型-文字
        :return: 点击'文章详情-驳回理由-类型-文字'按钮后的页面
        """
        self.project.click(self.article_detail_no_pass_reason_type_words_button)
        return self.project.get_current_page_source()

    def click_article_detail_no_pass_reason_type_image_button_action(self):
        """
        动作：点击文章详情-驳回理由-类型-图片
        :return: 点击'文章详情-驳回理由-类型-图片'按钮后的页面
        """
        self.project.click(self.article_detail_no_pass_reason_type_image_button)
        return self.project.get_current_page_source()

    def click_article_detail_no_pass_reason_type_video_button_action(self):
        """
        动作：点击文章详情-驳回理由-类型-视频
        :return: 点击'文章详情-驳回理由-类型-视频'按钮后的页面
        """
        self.project.click(self.article_detail_no_pass_reason_type_video_button)
        return self.project.get_current_page_source()

    def click_article_detail_no_pass_reason_list_first_button_action(self):
        """
        动作：点击文章详情-驳回理由-列表-第一个
        :return: 点击'文章详情-驳回理由-列表-第一个'按钮后的页面
        """
        self.project.click(self.article_detail_no_pass_reason_list_first_button)
        return self.project.get_current_page_source()

    def click_article_detail_no_pass_reason_list_second_button_action(self):
        """
        动作：点击文章详情-驳回理由-列表-第二个
        :return: 点击'文章详情-驳回理由-列表-第二个'按钮后的页面
        """
        self.project.click(self.article_detail_no_pass_reason_list_second_button)
        return self.project.get_current_page_source()

    def click_article_detail_pass_reason_list_first_button_action(self):
        """
        动作：点击文章详情-通过理由-列表-第一个
        :return: 点击'文章详情-通过理由-列表-第一个'按钮后的页面
        """
        self.project.click(self.article_detail_pass_reason_list_first_button)
        return self.project.get_current_page_source()

    def click_article_detail_commit_button_action(self):
        """
        动作：点击文章详情=提交
        :return: 点击'文章详情=提交'按钮后的页面
        """
        self.project.click(self.article_detail_commit_button)
        return self.project.get_current_page_source()

    def get_article_detail_commit_popup_title_text_action(self):
        """
        动作：获取文章详情-提交确认弹窗-标题的文本
        :return: '文章详情-提交确认弹窗-标题'的文本
        """
        control_content = self.project.get_element_text(self.article_detail_commit_popup_title_text)
        return control_content

    def get_article_detail_commit_popup_tip_text_action(self):
        """
        动作：获取文章详情-提交确认弹窗-提示的文本
        :return: '文章详情-提交确认弹窗-提示'的文本
        """
        control_content = self.project.get_element_text(self.article_detail_commit_popup_tip_text)
        return control_content

    def click_article_detail_commit_popup_confirm_button_action(self):
        """
        动作：点击文章详情-提交确认弹窗-确认
        :return: 点击'文章详情-提交确认弹窗-确认'按钮后的页面
        """
        self.project.click(self.article_detail_commit_popup_confirm_button)
        return self.project.get_current_page_source()

    def click_article_detail_commit_popup_cancel_button_action(self):
        """
        动作：点击文章详情-提交确认弹窗-取消
        :return: 点击'文章详情-提交确认弹窗-取消'按钮后的页面
        """
        self.project.click(self.article_detail_commit_popup_cancel_button)
        return self.project.get_current_page_source()

    def click_article_detail_commit_popup_close_button_action(self):
        """
        动作：点击文章详情-提交确认弹窗-关闭
        :return: 点击'文章详情-提交确认弹窗-关闭'按钮后的页面
        """
        self.project.click(self.article_detail_commit_popup_close_button)
        return self.project.get_current_page_source()

    # endregion Actions
