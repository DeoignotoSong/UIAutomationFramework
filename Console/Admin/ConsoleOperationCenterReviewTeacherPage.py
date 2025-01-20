from Utils.Log import log

"""
后台首页-运营中心-审核管理-达人主页审核
console_url/review/teacher
"""


class ConsoleOperationCenterReviewTeacherPage:
    def __init__(self, project):
        self.project = project
        self.url = 'console_url/review/teacher'
        # region Fields
        # 消息通知
        self._message_content_text_tag = '/html/body/div[last()]/div/div/p'
        # 下拉列表
        self._drop_down_list_select_tag = '/html/body/div[@class="el-select-dropdown el-popper"]/div[1]/div[1]/ul[@class="el-scrollbar__view el-select-dropdown__list"]'
        # 搜索-用户id
        self._search_user_id_input_tag = '//*[@id="tableSearch"]/form/div/div[1]/div/div/input'
        # 搜索-类型
        self._search_type_button_tag = '//*[@id="tableSearch"]/form/div/div[6]/div/div'
        # 搜索-审核状态
        self._search_audit_status_button_tag = '//*[@id="tableSearch"]/form/div/div[7]/div/div'
        # 搜索-查询
        self._search_query_button_tag = '//*[@id="tableSearch"]/form/div/div[last()-1]/div/button'
        # 搜索-清除
        self._search_clear_button_tag = '//*[@id="tableSearch"]/form/div/div[last()]/div/button'
        # 列表-第一行-用户ID
        self._list_first_user_id_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[1]/div'
        # 列表-第一行-真实姓名
        self._list_first_real_name_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[2]/div'
        # 列表-第一行-角色
        self._list_first_role_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[3]/div'
        # 列表-第一行-频道
        self._list_first_channel_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[4]/div'
        # 列表-第一行-类型
        self._list_first_type_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[5]/div'
        # 列表-第一行-更新时间
        self._list_first_update_time_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[6]/div'
        # 列表-第一行-审核状态
        self._list_first_audit_status_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[7]/div'
        # 列表-第一行-操作-第一个
        self._list_first_execute_first_button_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div[1]/div[4]/div[2]/table/tbody/tr[1]/td[8]/div/a[1]'
        # 审核详情-返回
        self._audit_detail_return_button_tag = '//*[@id="app"]/div/section/main/div/div[1]/div[1]/div[1]/div'
        # 审核详情-审核通过
        self._audit_detail_audit_pass_button_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[@class="page-st"]/div[1]/button[1]'
        # 审核详情-审核未通过
        self._audit_detail_audit_no_pass_button_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[@class="page-st"]/div[1]/button[2]'
        # 审核详情-审核通过-取消
        self._audit_detail_audit_pass_cancel_button_tag = '/html/body/div[@aria-label="审核通过提示"]/div/div[3]/button[1]'
        # 审核详情-审核通过-确定
        self._audit_detail_audit_pass_confirm_button_tag = '/html/body/div[@aria-label="审核通过提示"]/div/div[3]/button[2]'
        # endregion Fields

    # region Properties
    @property
    def message_content_text(self):
        """
        属性: 消息通知
        :return: 消息通知
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
        属性: 下拉列表
        :return: 下拉列表
        """
        element = None
        try:
            element = self.project.get_element(self._drop_down_list_select_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def search_user_id_input(self):
        """
        属性: 搜索-用户id
        :return: 搜索-用户id
        """
        element = None
        try:
            element = self.project.get_element(self._search_user_id_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def search_type_button(self):
        """
        属性: 搜索-类型
        :return: 搜索-类型
        """
        element = None
        try:
            element = self.project.get_element(self._search_type_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def search_audit_status_button(self):
        """
        属性: 搜索-审核状态
        :return: 搜索-审核状态
        """
        element = None
        try:
            element = self.project.get_element(self._search_audit_status_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def search_query_button(self):
        """
        属性: 搜索-查询
        :return: 搜索-查询
        """
        element = None
        try:
            element = self.project.get_element(self._search_query_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def search_clear_button(self):
        """
        属性: 搜索-清除
        :return: 搜索-清除
        """
        element = None
        try:
            element = self.project.get_element(self._search_clear_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def list_first_user_id_text(self):
        """
        属性: 列表-第一行-用户ID
        :return: 列表-第一行-用户ID
        """
        element = None
        try:
            element = self.project.get_element(self._list_first_user_id_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def list_first_real_name_text(self):
        """
        属性: 列表-第一行-真实姓名
        :return: 列表-第一行-真实姓名
        """
        element = None
        try:
            element = self.project.get_element(self._list_first_real_name_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def list_first_role_text(self):
        """
        属性: 列表-第一行-角色
        :return: 列表-第一行-角色
        """
        element = None
        try:
            element = self.project.get_element(self._list_first_role_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def list_first_channel_text(self):
        """
        属性: 列表-第一行-频道
        :return: 列表-第一行-频道
        """
        element = None
        try:
            element = self.project.get_element(self._list_first_channel_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def list_first_type_text(self):
        """
        属性: 列表-第一行-类型
        :return: 列表-第一行-类型
        """
        element = None
        try:
            element = self.project.get_element(self._list_first_type_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def list_first_update_time_text(self):
        """
        属性: 列表-第一行-更新时间
        :return: 列表-第一行-更新时间
        """
        element = None
        try:
            element = self.project.get_element(self._list_first_update_time_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def list_first_audit_status_text(self):
        """
        属性: 列表-第一行-审核状态
        :return: 列表-第一行-审核状态
        """
        element = None
        try:
            element = self.project.get_element(self._list_first_audit_status_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def list_first_execute_first_button(self):
        """
        属性: 列表-第一行-操作-第一个
        :return: 列表-第一行-操作-第一个
        """
        element = None
        try:
            element = self.project.get_element(self._list_first_execute_first_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def audit_detail_return_button(self):
        """
        属性: 审核详情-返回
        :return: 审核详情-返回
        """
        element = None
        try:
            element = self.project.get_element(self._audit_detail_return_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def audit_detail_audit_pass_button(self):
        """
        属性: 审核详情-审核通过
        :return: 审核详情-审核通过
        """
        element = None
        try:
            element = self.project.get_element(self._audit_detail_audit_pass_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def audit_detail_audit_no_pass_button(self):
        """
        属性: 审核详情-审核未通过
        :return: 审核详情-审核未通过
        """
        element = None
        try:
            element = self.project.get_element(self._audit_detail_audit_no_pass_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def audit_detail_audit_pass_cancel_button(self):
        """
        属性: 审核详情-审核通过-取消
        :return: 审核详情-审核通过-取消
        """
        element = None
        try:
            element = self.project.get_element(self._audit_detail_audit_pass_cancel_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def audit_detail_audit_pass_confirm_button(self):
        """
        属性: 审核详情-审核通过-确定
        :return: 审核详情-审核通过-确定
        """
        element = None
        try:
            element = self.project.get_element(self._audit_detail_audit_pass_confirm_button_tag)
        except AttributeError as error:
            log(error)
        return element

    # endregion Properties

    # region Actions
    def get_message_content_text_action(self):
        """
        动作：获取消息通知的文本
        :return: '消息通知'的文本
        """
        control_content = self.project.get_element_text(self.message_content_text)
        return control_content

    def get_select_drop_down_list_action(self, drop_down_list_select):
        """
        动作：获取下拉列表列表选中的文本
        :param drop_down_list_select: 下拉列表列表索引或文本
        :return: '下拉列表'的文本
        """
        control_content = self.project.get_select_content(self.drop_down_list_select, drop_down_list_select)
        return control_content

    def select_drop_down_list_action(self, drop_down_list_select):
        """
        动作：选择下拉列表
        :param drop_down_list_select: 下拉列表列表索引或文本
        :return: 选择'下拉列表'选择器后的页面
        """
        self.project.select_control(self.drop_down_list_select, drop_down_list_select)
        return self.project.get_current_page_source()

    def set_search_user_id_input_action(self, search_user_id_input):
        """
        动作：设置搜索-用户id
        :param search_user_id_input: 搜索-用户id
        :return: 设置'搜索-用户id'文本后的页面
        """
        self.project.clear_and_send_keys(self.search_user_id_input, search_user_id_input)
        return self.project.get_current_page_source()

    def click_search_type_button_action(self):
        """
        动作：点击搜索-类型
        :return: 点击'搜索-类型'按钮后的页面
        """
        self.project.click(self.search_type_button)
        return self.project.get_current_page_source()

    def click_search_audit_status_button_action(self):
        """
        动作：点击搜索-审核状态
        :return: 点击'搜索-审核状态'按钮后的页面
        """
        self.project.click(self.search_audit_status_button)
        return self.project.get_current_page_source()

    def click_search_query_button_action(self):
        """
        动作：点击搜索-查询
        :return: 点击'搜索-查询'按钮后的页面
        """
        self.project.click(self.search_query_button)
        return self.project.get_current_page_source()

    def click_search_clear_button_action(self):
        """
        动作：点击搜索-清除
        :return: 点击'搜索-清除'按钮后的页面
        """
        self.project.click(self.search_clear_button)
        return self.project.get_current_page_source()

    def get_list_first_user_id_text_action(self):
        """
        动作：获取列表-第一行-用户ID的文本
        :return: '列表-第一行-用户ID'的文本
        """
        control_content = self.project.get_element_text(self.list_first_user_id_text)
        return control_content

    def get_list_first_real_name_text_action(self):
        """
        动作：获取列表-第一行-真实姓名的文本
        :return: '列表-第一行-真实姓名'的文本
        """
        control_content = self.project.get_element_text(self.list_first_real_name_text)
        return control_content

    def get_list_first_role_text_action(self):
        """
        动作：获取列表-第一行-角色的文本
        :return: '列表-第一行-角色'的文本
        """
        control_content = self.project.get_element_text(self.list_first_role_text)
        return control_content

    def get_list_first_channel_text_action(self):
        """
        动作：获取列表-第一行-频道的文本
        :return: '列表-第一行-频道'的文本
        """
        control_content = self.project.get_element_text(self.list_first_channel_text)
        return control_content

    def get_list_first_type_text_action(self):
        """
        动作：获取列表-第一行-类型的文本
        :return: '列表-第一行-类型'的文本
        """
        control_content = self.project.get_element_text(self.list_first_type_text)
        return control_content

    def get_list_first_update_time_text_action(self):
        """
        动作：获取列表-第一行-更新时间的文本
        :return: '列表-第一行-更新时间'的文本
        """
        control_content = self.project.get_element_text(self.list_first_update_time_text)
        return control_content

    def get_list_first_audit_status_text_action(self):
        """
        动作：获取列表-第一行-审核状态的文本
        :return: '列表-第一行-审核状态'的文本
        """
        control_content = self.project.get_element_text(self.list_first_audit_status_text)
        return control_content

    def click_list_first_execute_first_button_action(self):
        """
        动作：点击列表-第一行-操作-第一个
        :return: 点击'列表-第一行-操作-第一个'按钮后的页面
        """
        self.project.click(self.list_first_execute_first_button)
        return self.project.get_current_page_source()

    def click_audit_detail_return_button_action(self):
        """
        动作：点击审核详情-返回
        :return: 点击'审核详情-返回'按钮后的页面
        """
        self.project.click(self.audit_detail_return_button)
        return self.project.get_current_page_source()

    def click_audit_detail_audit_pass_button_action(self):
        """
        动作：点击审核详情-审核通过
        :return: 点击'审核详情-审核通过'按钮后的页面
        """
        self.project.click(self.audit_detail_audit_pass_button)
        return self.project.get_current_page_source()

    def click_audit_detail_audit_no_pass_button_action(self):
        """
        动作：点击审核详情-审核未通过
        :return: 点击'审核详情-审核未通过'按钮后的页面
        """
        self.project.click(self.audit_detail_audit_no_pass_button)
        return self.project.get_current_page_source()

    def click_audit_detail_audit_pass_cancel_button_action(self):
        """
        动作：点击审核详情-审核通过-取消
        :return: 点击'审核详情-审核通过-取消'按钮后的页面
        """
        self.project.click(self.audit_detail_audit_pass_cancel_button)
        return self.project.get_current_page_source()

    def click_audit_detail_audit_pass_confirm_button_action(self):
        """
        动作：点击审核详情-审核通过-确定
        :return: 点击'审核详情-审核通过-确定'按钮后的页面
        """
        self.project.click(self.audit_detail_audit_pass_confirm_button)
        return self.project.get_current_page_source()

    # endregion Actions
