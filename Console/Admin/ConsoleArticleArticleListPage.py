from Utils.Log import log

"""
后台首页-运营中心-文章管理-文章列表
console_url/article/article_list
"""


class ConsoleArticleArticleListPage:
    def __init__(self, project):
        self.project = project
        self.url = 'console_url/article/article_list'
        # region Fields
        # 消息提示
        self._message_content_text_tag = '/html/body/div[last()]/div/div[1]/p'
        # 搜索-文章标题
        self._search_article_title_input_tag = '//*[@id="tableSearch"]/form/div/div[1]/div/div/input'
        # 搜索-查询按钮
        self._search_query_button_tag = '//*[@id="tableSearch"]/form/div/div[12]/div/button'
        # 列表-第一个-文章id
        self._list_first_article_id_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[2]/div'
        # 列表-第一个-文章标题按钮
        self._list_first_article_title_button_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[3]/div/a'
        # 列表-第一个-文章标题文本
        self._list_first_article_title_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[3]/div/a/span'
        # 列表-第一个-用户姓名
        self._list_first_user_name_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[4]/div'
        # 列表-第一个-频道
        self._list_first_channel_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[5]/div'
        # 列表-第一个-一级类目标签
        self._list_first_first_label_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[6]/div'
        # 列表-第一个-二级类目标签
        self._list_first_second_label_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[7]/div'
        # 列表-第一个-内容主题
        self._list_first_sub_content_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[8]/div'
        # 列表-第一个-用户昵称
        self._list_first_user_nick_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[9]/div'
        # 列表-第一个-发布时间
        self._list_first_create_time_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[10]/div'
        # 列表-第一个-用户角色
        self._list_first_user_role_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[11]/div'
        # 列表-第一个-当前状态
        self._list_first_state_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[12]/div'
        # 列表-第一个-操作日志按钮
        self._list_first_exe_log_button_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div[1]/div[4]/div[2]/table/tbody/tr[1]/td[13]/div/a[1]'
        # 列表-第一个-禁用按钮
        self._list_first_disable_button_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div[1]/div[4]/div[2]/table/tbody/tr[1]/td[13]/div/a[2]'
        # 确认禁用-禁用理由下拉框
        self._disable_reason_button_tag = '//*[@id="app"]/div/section/main/div/div[4]/div/div/div[2]/form/div[1]/div/div'
        # 确认禁用-禁用理由列表
        self._disable_reason_select_tag = '/html/body/div[last()]/div[1]/div[1]/ul'
        # 确认禁用-自定义理由输入框
        self._disable_custom_reason_input_tag = '//*[@id="app"]/div/section/main/div/div[4]/div/div/div[2]/form/div[2]/div/div/textarea'
        # 确认禁用-确定按钮
        self._disable_confirm_button_tag = '//*[@id="app"]/div/section/main/div/div[4]/div/div/div[3]/span/button[2]'
        # 确认禁用-取消按钮
        self._disable_cancel_button_tag = '//*[@id="app"]/div/section/main/div/div[4]/div/div/div[3]/span/button[1]'
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
    def search_article_title_input(self):
        """
        属性: 搜索-文章标题
        :return: 搜索-文章标题
        """
        element = None
        try:
            element = self.project.get_element(self._search_article_title_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def search_query_button(self):
        """
        属性: 搜索-查询按钮
        :return: 搜索-查询按钮
        """
        element = None
        try:
            element = self.project.get_element(self._search_query_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def list_first_article_id_text(self):
        """
        属性: 列表-第一个-文章id
        :return: 列表-第一个-文章id
        """
        element = None
        try:
            element = self.project.get_element(self._list_first_article_id_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def list_first_article_title_button(self):
        """
        属性: 列表-第一个-文章标题按钮
        :return: 列表-第一个-文章标题按钮
        """
        element = None
        try:
            element = self.project.get_element(self._list_first_article_title_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def list_first_article_title_text(self):
        """
        属性: 列表-第一个-文章标题文本
        :return: 列表-第一个-文章标题文本
        """
        element = None
        try:
            element = self.project.get_element(self._list_first_article_title_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def list_first_user_name_text(self):
        """
        属性: 列表-第一个-用户姓名
        :return: 列表-第一个-用户姓名
        """
        element = None
        try:
            element = self.project.get_element(self._list_first_user_name_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def list_first_channel_text(self):
        """
        属性: 列表-第一个-频道
        :return: 列表-第一个-频道
        """
        element = None
        try:
            element = self.project.get_element(self._list_first_channel_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def list_first_first_label_text(self):
        """
        属性: 列表-第一个-一级类目标签
        :return: 列表-第一个-一级类目标签
        """
        element = None
        try:
            element = self.project.get_element(self._list_first_first_label_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def list_first_second_label_text(self):
        """
        属性: 列表-第一个-二级类目标签
        :return: 列表-第一个-二级类目标签
        """
        element = None
        try:
            element = self.project.get_element(self._list_first_second_label_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def list_first_sub_content_text(self):
        """
        属性: 列表-第一个-内容主题
        :return: 列表-第一个-内容主题
        """
        element = None
        try:
            element = self.project.get_element(self._list_first_sub_content_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def list_first_user_nick_text(self):
        """
        属性: 列表-第一个-用户昵称
        :return: 列表-第一个-用户昵称
        """
        element = None
        try:
            element = self.project.get_element(self._list_first_user_nick_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def list_first_create_time_text(self):
        """
        属性: 列表-第一个-发布时间
        :return: 列表-第一个-发布时间
        """
        element = None
        try:
            element = self.project.get_element(self._list_first_create_time_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def list_first_user_role_text(self):
        """
        属性: 列表-第一个-用户角色
        :return: 列表-第一个-用户角色
        """
        element = None
        try:
            element = self.project.get_element(self._list_first_user_role_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def list_first_state_text(self):
        """
        属性: 列表-第一个-当前状态
        :return: 列表-第一个-当前状态
        """
        element = None
        try:
            element = self.project.get_element(self._list_first_state_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def list_first_exe_log_button(self):
        """
        属性: 列表-第一个-操作日志按钮
        :return: 列表-第一个-操作日志按钮
        """
        element = None
        try:
            element = self.project.get_element(self._list_first_exe_log_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def list_first_disable_button(self):
        """
        属性: 列表-第一个-禁用按钮
        :return: 列表-第一个-禁用按钮
        """
        element = None
        try:
            element = self.project.get_element(self._list_first_disable_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def disable_reason_button(self):
        """
        属性: 确认禁用-禁用理由下拉框
        :return: 确认禁用-禁用理由下拉框
        """
        element = None
        try:
            element = self.project.get_element(self._disable_reason_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def disable_reason_select(self):
        """
        属性: 确认禁用-禁用理由列表
        :return: 确认禁用-禁用理由列表
        """
        element = None
        try:
            element = self.project.get_element(self._disable_reason_select_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def disable_custom_reason_input(self):
        """
        属性: 确认禁用-自定义理由输入框
        :return: 确认禁用-自定义理由输入框
        """
        element = None
        try:
            element = self.project.get_element(self._disable_custom_reason_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def disable_confirm_button(self):
        """
        属性: 确认禁用-确定按钮
        :return: 确认禁用-确定按钮
        """
        element = None
        try:
            element = self.project.get_element(self._disable_confirm_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def disable_cancel_button(self):
        """
        属性: 确认禁用-取消按钮
        :return: 确认禁用-取消按钮
        """
        element = None
        try:
            element = self.project.get_element(self._disable_cancel_button_tag)
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

    def set_search_article_title_input_action(self, search_article_title_input):
        """
        动作：设置搜索-文章标题
        :param search_article_title_input: 搜索-文章标题
        :return: 设置'搜索-文章标题'文本后的页面
        """
        self.project.clear_and_send_keys(self.search_article_title_input, search_article_title_input)
        return self.project.get_current_page_source()

    def click_search_query_button_action(self):
        """
        动作：点击搜索-查询按钮
        :return: 点击'搜索-查询按钮'按钮后的页面
        """
        self.project.click(self.search_query_button)
        return self.project.get_current_page_source()

    def get_list_first_article_id_text_action(self):
        """
        动作：获取列表-第一个-文章id的文本
        :return: '列表-第一个-文章id'的文本
        """
        control_content = self.project.get_element_text(self.list_first_article_id_text)
        return control_content

    def click_list_first_article_title_button_action(self):
        """
        动作：点击列表-第一个-文章标题按钮
        :return: 点击'列表-第一个-文章标题按钮'按钮后的页面
        """
        self.project.click(self.list_first_article_title_button)
        return self.project.get_current_page_source()

    def get_list_first_article_title_text_action(self):
        """
        动作：获取列表-第一个-文章标题文本的文本
        :return: '列表-第一个-文章标题文本'的文本
        """
        control_content = self.project.get_element_text(self.list_first_article_title_text)
        return control_content

    def get_list_first_user_name_text_action(self):
        """
        动作：获取列表-第一个-用户姓名的文本
        :return: '列表-第一个-用户姓名'的文本
        """
        control_content = self.project.get_element_text(self.list_first_user_name_text)
        return control_content

    def get_list_first_channel_text_action(self):
        """
        动作：获取列表-第一个-频道的文本
        :return: '列表-第一个-频道'的文本
        """
        control_content = self.project.get_element_text(self.list_first_channel_text)
        return control_content

    def get_list_first_first_label_text_action(self):
        """
        动作：获取列表-第一个-一级类目标签的文本
        :return: '列表-第一个-一级类目标签'的文本
        """
        control_content = self.project.get_element_text(self.list_first_first_label_text)
        return control_content

    def get_list_first_second_label_text_action(self):
        """
        动作：获取列表-第一个-二级类目标签的文本
        :return: '列表-第一个-二级类目标签'的文本
        """
        control_content = self.project.get_element_text(self.list_first_second_label_text)
        return control_content

    def get_list_first_sub_content_text_action(self):
        """
        动作：获取列表-第一个-内容主题的文本
        :return: '列表-第一个-内容主题'的文本
        """
        control_content = self.project.get_element_text(self.list_first_sub_content_text)
        return control_content

    def get_list_first_user_nick_text_action(self):
        """
        动作：获取列表-第一个-用户昵称的文本
        :return: '列表-第一个-用户昵称'的文本
        """
        control_content = self.project.get_element_text(self.list_first_user_nick_text)
        return control_content

    def get_list_first_create_time_text_action(self):
        """
        动作：获取列表-第一个-发布时间的文本
        :return: '列表-第一个-发布时间'的文本
        """
        control_content = self.project.get_element_text(self.list_first_create_time_text)
        return control_content

    def get_list_first_user_role_text_action(self):
        """
        动作：获取列表-第一个-用户角色的文本
        :return: '列表-第一个-用户角色'的文本
        """
        control_content = self.project.get_element_text(self.list_first_user_role_text)
        return control_content

    def get_list_first_state_text_action(self):
        """
        动作：获取列表-第一个-当前状态的文本
        :return: '列表-第一个-当前状态'的文本
        """
        control_content = self.project.get_element_text(self.list_first_state_text)
        return control_content

    def click_list_first_exe_log_button_action(self):
        """
        动作：点击列表-第一个-操作日志按钮
        :return: 点击'列表-第一个-操作日志按钮'按钮后的页面
        """
        self.project.click(self.list_first_exe_log_button)
        return self.project.get_current_page_source()

    def click_list_first_disable_button_action(self):
        """
        动作：点击列表-第一个-禁用按钮
        :return: 点击'列表-第一个-禁用按钮'按钮后的页面
        """
        self.project.click(self.list_first_disable_button)
        return self.project.get_current_page_source()

    def click_disable_reason_button_action(self):
        """
        动作：点击确认禁用-禁用理由下拉框
        :return: 点击'确认禁用-禁用理由下拉框'按钮后的页面
        """
        self.project.click(self.disable_reason_button)
        return self.project.get_current_page_source()

    def get_select_disable_reason_action(self, disable_reason_select):
        """
        动作：获取确认禁用-禁用理由列表列表选中的文本
        :param disable_reason_select: 确认禁用-禁用理由列表列表索引或文本
        :return: '确认禁用-禁用理由列表'的文本
        """
        control_content = self.project.get_select_content(self.disable_reason_select, disable_reason_select)
        return control_content

    def select_disable_reason_action(self, disable_reason_select):
        """
        动作：选择确认禁用-禁用理由列表
        :param disable_reason_select: 确认禁用-禁用理由列表列表索引或文本
        :return: 选择'确认禁用-禁用理由列表'选择器后的页面
        """
        self.project.select_control(self.disable_reason_select, disable_reason_select)
        return self.project.get_current_page_source()

    def set_disable_custom_reason_input_action(self, disable_custom_reason_input):
        """
        动作：设置确认禁用-自定义理由输入框
        :param disable_custom_reason_input: 确认禁用-自定义理由输入框
        :return: 设置'确认禁用-自定义理由输入框'文本后的页面
        """
        self.project.clear_and_send_keys(self.disable_custom_reason_input, disable_custom_reason_input)
        return self.project.get_current_page_source()

    def click_disable_confirm_button_action(self):
        """
        动作：点击确认禁用-确定按钮
        :return: 点击'确认禁用-确定按钮'按钮后的页面
        """
        self.project.click(self.disable_confirm_button)
        return self.project.get_current_page_source()

    def click_disable_cancel_button_action(self):
        """
        动作：点击确认禁用-取消按钮
        :return: 点击'确认禁用-取消按钮'按钮后的页面
        """
        self.project.click(self.disable_cancel_button)
        return self.project.get_current_page_source()

    # endregion Actions
