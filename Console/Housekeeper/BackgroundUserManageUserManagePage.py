from Utils.Log import log

"""
后台用户管理页
https://wpc.dxzjjl.com.cn/background-user-manage/user-manage
"""


class BackgroundUserManageUserManagePage:
    def __init__(self, project):
        self.project = project
        self.url = 'housekeeper_url/background-user-manage/user-manage'
        # region Fields
        # 消息提示信息
        self._message_content_text_tag = '/html/body/div[last()]/div/div[1]/p'
        # 下拉列表
        self._drop_down_list_select_tag = '/html/body/div[3]/div[1]/div[1]/ul'
        # 搜索用户账户
        self._search_user_account_input_tag = '/html/body/div/div/div[2]/section/div/div/div[1]/div[1]/form/div/div[1]/div/div/input'
        # 搜索用户姓名
        self._search_user_name_input_tag = '/html/body/div/div/div[2]/section/div/div/div[1]/form/div/div[2]/div/div/input'
        # 搜索手机号
        self._search_user_mobile_input_tag = '/html/body/div/div/div[2]/section/div/div/div[1]/form/div/div[3]/div/div/input'
        # 搜索邮箱账号
        self._search_user_email_input_tag = '/html/body/div/div/div[2]/section/div/div/div[1]/form/div/div[4]/div/div/input'
        # 搜索角色名称
        self._search_user_role_input_tag = '/html/body/div[1]/div/div[2]/section/div/div/div[1]/form/div/div[5]/div/div/div[1]'
        # 搜索查询按钮
        self._search_button_tag = '/html/body/div/div/div[2]/section/div/div/div[1]/div[1]/form/div/div[6]/div/button'
        # 搜索重置按钮
        self._clear_button_tag = '/html/body/div[1]/div/div[2]/section/div/div/div[1]/form/div/div[7]/div/button'
        # 新增用户按钮
        self._add_user_button_tag = '/html/body/div[1]/div/div[2]/section/div/div/div[2]/div[1]/div/button'
        # 新增用户账户
        self._add_user_account_input_tag = '/html/body/div[1]/div/div[2]/section/div/div/div[3]/div/div/div[2]/form/div[1]/div[1]/div/div/div[1]/input'
        # 新增用户姓名
        self._add_user_name_input_tag = '/html/body/div[1]/div/div[2]/section/div/div/div[3]/div/div/div[2]/form/div[1]/div[2]/div/div/div[1]/input'
        # 新增用户邮箱账号
        self._add_user_mail_input_tag = '/html/body/div[1]/div/div[2]/section/div/div/div[3]/div/div/div[2]/form/div[2]/div[1]/div/div/div[1]/input'
        # 新增用户联系电话
        self._add_user_mobile_input_tag = '/html/body/div[1]/div/div[2]/section/div/div/div[3]/div/div/div[2]/form/div[2]/div[2]/div/div/div[1]/input'
        # 新增用户登录密码
        self._add_user_password_input_tag = '/html/body/div[1]/div/div[2]/section/div/div/div[3]/div/div/div[2]/form/div[3]/div[1]/div/div/div[1]/input'
        # 新增用户角色
        self._add_user_role_button_tag = '/html/body/div[1]/div/div[2]/section/div/div/div[3]/div/div/div[2]/form/div[3]/div[2]/div/div/div/div[1]'
        # 新增用户确认按钮
        self._add_user_commit_button_tag = '/html/body/div[1]/div/div[2]/section/div/div/div[3]/div/div/div[3]/span/button[2]'
        # 新增用户取消按钮
        self._add_user_cancle_button_tag = '/html/body/div[1]/div/div[2]/section/div/div/div[3]/div/div/div[3]/span/button[1]'
        # 列表第一条数据用户账户
        self._list_first_user_account_text_tag = '/html/body/div[1]/div/div[2]/section/div/div/div[2]/div[2]/div[3]/table/tbody/tr[1]/td[1]/div/span'
        # 列表第一条数据用户姓名
        self._list_first_user_name_text_tag = '/html/body/div[1]/div/div[2]/section/div/div/div[2]/div[2]/div[3]/table/tbody/tr[1]/td[2]/div/span'
        # 列表手机号
        self._list_first_user_mobile_text_tag = '/html/body/div[1]/div/div[2]/section/div/div/div[2]/div[2]/div[3]/table/tbody/tr[1]/td[3]/div/span'
        # 列表第一条数据用户邮箱账号
        self._list_first_user_mail_text_tag = '/html/body/div[1]/div/div[2]/section/div/div/div[2]/div[2]/div[3]/table/tbody/tr[1]/td[4]/div/span'
        # 列表第一条数据用户创建时间
        self._list_first_user_create_time_text_tag = '/html/body/div[1]/div/div[2]/section/div/div/div[2]/div[2]/div[3]/table/tbody/tr[1]/td[5]/div/span'
        # 列表第一条数据角色
        self._list_first_user_role_text_tag = '/html/body/div[1]/div/div[2]/section/div/div/div[2]/div[2]/div[3]/table/tbody/tr[1]/td[6]/div/span'
        # 列表第一条数据状态
        self._list_first_user_state_text_tag = '/html/body/div[1]/div/div[2]/section/div/div/div[2]/div[2]/div[3]/table/tbody/tr[1]/td[7]/div/span'
        # 列表第一条数据操作编辑按钮
        self._list_first_option_edit_button_tag = '/html/body/div[1]/div/div[2]/section/div/div/div[2]/div[2]/div[4]/div[2]/table/tbody/tr[1]/td[8]/div/button[1]'
        # 列表第一条数据操作禁用按钮
        self._list_first_option_ban_button_tag = '/html/body/div[1]/div/div[2]/section/div/div/div[2]/div[2]/div[4]/div[2]/table/tbody/tr[1]/td[8]/div/button[2]'
        # 列表第一条数据操作禁用确认按钮
        self._list_first_option_ban_confirm_button_tag = '/html/body/div[last()-1]/div/div[3]/button[2]'
        # 重置密码
        self._list_first_option_set_password_button_tag = '/html/body/div[1]/div/div[2]/section/div/div/div[2]/div[2]/div[4]/div[2]/table/tbody/tr[1]/td[8]/div/button[3]'
        # 重置密码输入框
        self._list_first_set_password_input_tag = '/html/body/div[1]/div/div[2]/section/div/div/div[5]/div/div/div[2]/form/div/div/div/div/div[1]/input'
        # 重置密码确定按钮
        self._list_first_set_password_commit_button_tag = '/html/body/div[1]/div/div[2]/section/div/div/div[5]/div/div/div[3]/span/button[2]'
        # 重置密码取消按钮
        self._list_first_set_password_cancle_button_tag = '/html/body/div[1]/div/div[2]/section/div/div/div[5]/div/div/div[3]/span/button[1]'
        # tab 列表
        self._tab_list_button_tag = '/html/body/div[1]/div/div[2]/div/div[1]/div[3]/div[2]/div/i'
        # 退出登录按钮
        self._loginout_button_tag = '/html/body/ul/li/span'
        # 空白
        self._white_button_tag = '/html/body/div[1]/div/div[2]/section/div/div/div[3]/div/div/div[3]'
        # endregion Fields

    # region Properties
    @property
    def message_content_text(self):
        """
        属性: 消息提示信息
        :return: 消息提示信息
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
    def search_user_account_input(self):
        """
        属性: 搜索用户账户
        :return: 搜索用户账户
        """
        element = None
        try:
            element = self.project.get_element(self._search_user_account_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def search_user_name_input(self):
        """
        属性: 搜索用户姓名
        :return: 搜索用户姓名
        """
        element = None
        try:
            element = self.project.get_element(self._search_user_name_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def search_user_mobile_input(self):
        """
        属性: 搜索手机号
        :return: 搜索手机号
        """
        element = None
        try:
            element = self.project.get_element(self._search_user_mobile_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def search_user_email_input(self):
        """
        属性: 搜索邮箱账号
        :return: 搜索邮箱账号
        """
        element = None
        try:
            element = self.project.get_element(self._search_user_email_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def search_user_role_input(self):
        """
        属性: 搜索角色名称
        :return: 搜索角色名称
        """
        element = None
        try:
            element = self.project.get_element(self._search_user_role_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def search_button(self):
        """
        属性: 搜索查询按钮
        :return: 搜索查询按钮
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
        属性: 搜索重置按钮
        :return: 搜索重置按钮
        """
        element = None
        try:
            element = self.project.get_element(self._clear_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def add_user_button(self):
        """
        属性: 新增用户按钮
        :return: 新增用户按钮
        """
        element = None
        try:
            element = self.project.get_element(self._add_user_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def add_user_account_input(self):
        """
        属性: 新增用户账户
        :return: 新增用户账户
        """
        element = None
        try:
            element = self.project.get_element(self._add_user_account_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def add_user_name_input(self):
        """
        属性: 新增用户姓名
        :return: 新增用户姓名
        """
        element = None
        try:
            element = self.project.get_element(self._add_user_name_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def add_user_mail_input(self):
        """
        属性: 新增用户邮箱账号
        :return: 新增用户邮箱账号
        """
        element = None
        try:
            element = self.project.get_element(self._add_user_mail_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def add_user_mobile_input(self):
        """
        属性: 新增用户联系电话
        :return: 新增用户联系电话
        """
        element = None
        try:
            element = self.project.get_element(self._add_user_mobile_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def add_user_password_input(self):
        """
        属性: 新增用户登录密码
        :return: 新增用户登录密码
        """
        element = None
        try:
            element = self.project.get_element(self._add_user_password_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def add_user_role_button(self):
        """
        属性: 新增用户角色
        :return: 新增用户角色
        """
        element = None
        try:
            element = self.project.get_element(self._add_user_role_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def add_user_commit_button(self):
        """
        属性: 新增用户确认按钮
        :return: 新增用户确认按钮
        """
        element = None
        try:
            element = self.project.get_element(self._add_user_commit_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def add_user_cancle_button(self):
        """
        属性: 新增用户取消按钮
        :return: 新增用户取消按钮
        """
        element = None
        try:
            element = self.project.get_element(self._add_user_cancle_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def list_first_user_account_text(self):
        """
        属性: 列表第一条数据用户账户
        :return: 列表第一条数据用户账户
        """
        element = None
        try:
            element = self.project.get_element(self._list_first_user_account_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def list_first_user_name_text(self):
        """
        属性: 列表第一条数据用户姓名
        :return: 列表第一条数据用户姓名
        """
        element = None
        try:
            element = self.project.get_element(self._list_first_user_name_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def list_first_user_mobile_text(self):
        """
        属性: 列表手机号
        :return: 列表手机号
        """
        element = None
        try:
            element = self.project.get_element(self._list_first_user_mobile_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def list_first_user_mail_text(self):
        """
        属性: 列表第一条数据用户邮箱账号
        :return: 列表第一条数据用户邮箱账号
        """
        element = None
        try:
            element = self.project.get_element(self._list_first_user_mail_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def list_first_user_create_time_text(self):
        """
        属性: 列表第一条数据用户创建时间
        :return: 列表第一条数据用户创建时间
        """
        element = None
        try:
            element = self.project.get_element(self._list_first_user_create_time_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def list_first_user_role_text(self):
        """
        属性: 列表第一条数据角色
        :return: 列表第一条数据角色
        """
        element = None
        try:
            element = self.project.get_element(self._list_first_user_role_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def list_first_user_state_text(self):
        """
        属性: 列表第一条数据状态
        :return: 列表第一条数据状态
        """
        element = None
        try:
            element = self.project.get_element(self._list_first_user_state_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def list_first_option_edit_button(self):
        """
        属性: 列表第一条数据操作编辑按钮
        :return: 列表第一条数据操作编辑按钮
        """
        element = None
        try:
            element = self.project.get_element(self._list_first_option_edit_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def list_first_option_ban_button(self):
        """
        属性: 列表第一条数据操作禁用按钮
        :return: 列表第一条数据操作禁用按钮
        """
        element = None
        try:
            element = self.project.get_element(self._list_first_option_ban_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def list_first_option_ban_confirm_button(self):
        """
        属性: 列表第一条数据操作禁用确认按钮
        :return: 列表第一条数据操作禁用确认按钮
        """
        element = None
        try:
            element = self.project.get_element(self._list_first_option_ban_confirm_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def list_first_option_set_password_button(self):
        """
        属性: 重置密码
        :return: 重置密码
        """
        element = None
        try:
            element = self.project.get_element(self._list_first_option_set_password_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def list_first_set_password_input(self):
        """
        属性: 重置密码输入框
        :return: 重置密码输入框
        """
        element = None
        try:
            element = self.project.get_element(self._list_first_set_password_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def list_first_set_password_commit_button(self):
        """
        属性: 重置密码确定按钮
        :return: 重置密码确定按钮
        """
        element = None
        try:
            element = self.project.get_element(self._list_first_set_password_commit_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def list_first_set_password_cancle_button(self):
        """
        属性: 重置密码取消按钮
        :return: 重置密码取消按钮
        """
        element = None
        try:
            element = self.project.get_element(self._list_first_set_password_cancle_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def tab_list_button(self):
        """
        属性: tab 列表
        :return: tab 列表
        """
        element = None
        try:
            element = self.project.get_element(self._tab_list_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def loginout_button(self):
        """
        属性: 退出登录按钮
        :return: 退出登录按钮
        """
        element = None
        try:
            element = self.project.get_element(self._loginout_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def white_button(self):
        """
        属性: 空白
        :return: 空白
        """
        element = None
        try:
            element = self.project.get_element(self._white_button_tag)
        except AttributeError as error:
            log(error)
        return element

    # endregion Properties

    # region Actions
    def get_message_content_text_action(self):
        """
        动作：获取消息提示信息的文本
        :return: '消息提示信息'的文本
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

    def set_search_user_account_input_action(self, search_user_account_input):
        """
        动作：设置搜索用户账户
        :param search_user_account_input: 搜索用户账户
        :return: 设置'搜索用户账户'文本后的页面
        """
        self.project.clear_and_send_keys(self.search_user_account_input, search_user_account_input)
        return self.project.get_current_page_source()

    def set_search_user_name_input_action(self, search_user_name_input):
        """
        动作：设置搜索用户姓名
        :param search_user_name_input: 搜索用户姓名
        :return: 设置'搜索用户姓名'文本后的页面
        """
        self.project.clear_and_send_keys(self.search_user_name_input, search_user_name_input)
        return self.project.get_current_page_source()

    def set_search_user_mobile_input_action(self, search_user_mobile_input):
        """
        动作：设置搜索手机号
        :param search_user_mobile_input: 搜索手机号
        :return: 设置'搜索手机号'文本后的页面
        """
        self.project.clear_and_send_keys(self.search_user_mobile_input, search_user_mobile_input)
        return self.project.get_current_page_source()

    def set_search_user_email_input_action(self, search_user_email_input):
        """
        动作：设置搜索邮箱账号
        :param search_user_email_input: 搜索邮箱账号
        :return: 设置'搜索邮箱账号'文本后的页面
        """
        self.project.clear_and_send_keys(self.search_user_email_input, search_user_email_input)
        return self.project.get_current_page_source()

    def set_search_user_role_input_action(self, search_user_role_input):
        """
        动作：设置搜索角色名称
        :param search_user_role_input: 搜索角色名称
        :return: 设置'搜索角色名称'文本后的页面
        """
        self.project.clear_and_send_keys(self.search_user_role_input, search_user_role_input)
        return self.project.get_current_page_source()

    def click_search_button_action(self):
        """
        动作：点击搜索查询按钮
        :return: 点击'搜索查询按钮'按钮后的页面
        """
        self.project.click(self.search_button)
        return self.project.get_current_page_source()

    def click_clear_button_action(self):
        """
        动作：点击搜索重置按钮
        :return: 点击'搜索重置按钮'按钮后的页面
        """
        self.project.click(self.clear_button)
        return self.project.get_current_page_source()

    def click_add_user_button_action(self):
        """
        动作：点击新增用户按钮
        :return: 点击'新增用户按钮'按钮后的页面
        """
        self.project.click(self.add_user_button)
        return self.project.get_current_page_source()

    def set_add_user_account_input_action(self, add_user_account_input):
        """
        动作：设置新增用户账户
        :param add_user_account_input: 新增用户账户
        :return: 设置'新增用户账户'文本后的页面
        """
        self.project.clear_and_send_keys(self.add_user_account_input, add_user_account_input)
        return self.project.get_current_page_source()

    def set_add_user_name_input_action(self, add_user_name_input):
        """
        动作：设置新增用户姓名
        :param add_user_name_input: 新增用户姓名
        :return: 设置'新增用户姓名'文本后的页面
        """
        self.project.clear_and_send_keys(self.add_user_name_input, add_user_name_input)
        return self.project.get_current_page_source()

    def set_add_user_mail_input_action(self, add_user_mail_input):
        """
        动作：设置新增用户邮箱账号
        :param add_user_mail_input: 新增用户邮箱账号
        :return: 设置'新增用户邮箱账号'文本后的页面
        """
        self.project.clear_and_send_keys(self.add_user_mail_input, add_user_mail_input)
        return self.project.get_current_page_source()

    def set_add_user_mobile_input_action(self, add_user_mobile_input):
        """
        动作：设置新增用户联系电话
        :param add_user_mobile_input: 新增用户联系电话
        :return: 设置'新增用户联系电话'文本后的页面
        """
        self.project.clear_and_send_keys(self.add_user_mobile_input, add_user_mobile_input)
        return self.project.get_current_page_source()

    def set_add_user_password_input_action(self, add_user_password_input):
        """
        动作：设置新增用户登录密码
        :param add_user_password_input: 新增用户登录密码
        :return: 设置'新增用户登录密码'文本后的页面
        """
        self.project.clear_and_send_keys(self.add_user_password_input, add_user_password_input)
        return self.project.get_current_page_source()

    def click_add_user_role_button_action(self):
        """
        动作：点击新增用户角色
        :return: 点击'新增用户角色'按钮后的页面
        """
        self.project.click(self.add_user_role_button)
        return self.project.get_current_page_source()

    def click_add_user_commit_button_action(self):
        """
        动作：点击新增用户确认按钮
        :return: 点击'新增用户确认按钮'按钮后的页面
        """
        self.project.click(self.add_user_commit_button)
        return self.project.get_current_page_source()

    def click_add_user_cancle_button_action(self):
        """
        动作：点击新增用户取消按钮
        :return: 点击'新增用户取消按钮'按钮后的页面
        """
        self.project.click(self.add_user_cancle_button)
        return self.project.get_current_page_source()

    def get_list_first_user_account_text_action(self):
        """
        动作：获取列表第一条数据用户账户的文本
        :return: '列表第一条数据用户账户'的文本
        """
        control_content = self.project.get_element_text(self.list_first_user_account_text)
        return control_content

    def get_list_first_user_name_text_action(self):
        """
        动作：获取列表第一条数据用户姓名的文本
        :return: '列表第一条数据用户姓名'的文本
        """
        control_content = self.project.get_element_text(self.list_first_user_name_text)
        return control_content

    def get_list_first_user_mobile_text_action(self):
        """
        动作：获取列表手机号的文本
        :return: '列表手机号'的文本
        """
        control_content = self.project.get_element_text(self.list_first_user_mobile_text)
        return control_content

    def get_list_first_user_mail_text_action(self):
        """
        动作：获取列表第一条数据用户邮箱账号的文本
        :return: '列表第一条数据用户邮箱账号'的文本
        """
        control_content = self.project.get_element_text(self.list_first_user_mail_text)
        return control_content

    def get_list_first_user_create_time_text_action(self):
        """
        动作：获取列表第一条数据用户创建时间的文本
        :return: '列表第一条数据用户创建时间'的文本
        """
        control_content = self.project.get_element_text(self.list_first_user_create_time_text)
        return control_content

    def get_list_first_user_role_text_action(self):
        """
        动作：获取列表第一条数据角色的文本
        :return: '列表第一条数据角色'的文本
        """
        control_content = self.project.get_element_text(self.list_first_user_role_text)
        return control_content

    def get_list_first_user_state_text_action(self):
        """
        动作：获取列表第一条数据状态的文本
        :return: '列表第一条数据状态'的文本
        """
        control_content = self.project.get_element_text(self.list_first_user_state_text)
        return control_content

    def click_list_first_option_edit_button_action(self):
        """
        动作：点击列表第一条数据操作编辑按钮
        :return: 点击'列表第一条数据操作编辑按钮'按钮后的页面
        """
        self.project.click(self.list_first_option_edit_button)
        return self.project.get_current_page_source()

    def click_list_first_option_ban_button_action(self):
        """
        动作：点击列表第一条数据操作禁用按钮
        :return: 点击'列表第一条数据操作禁用按钮'按钮后的页面
        """
        self.project.click(self.list_first_option_ban_button)
        return self.project.get_current_page_source()

    def click_list_first_option_ban_confirm_button_action(self):
        """
        动作：点击列表第一条数据操作禁用确认按钮
        :return: 点击'列表第一条数据操作禁用确认按钮'按钮后的页面
        """
        self.project.click(self.list_first_option_ban_confirm_button)
        return self.project.get_current_page_source()

    def click_list_first_option_set_password_button_action(self):
        """
        动作：点击重置密码
        :return: 点击'重置密码'按钮后的页面
        """
        self.project.click(self.list_first_option_set_password_button)
        return self.project.get_current_page_source()

    def set_list_first_set_password_input_action(self, list_first_set_password_input):
        """
        动作：设置重置密码输入框
        :param list_first_set_password_input: 重置密码输入框
        :return: 设置'重置密码输入框'文本后的页面
        """
        self.project.clear_and_send_keys(self.list_first_set_password_input, list_first_set_password_input)
        return self.project.get_current_page_source()

    def click_list_first_set_password_commit_button_action(self):
        """
        动作：点击重置密码确定按钮
        :return: 点击'重置密码确定按钮'按钮后的页面
        """
        self.project.click(self.list_first_set_password_commit_button)
        return self.project.get_current_page_source()

    def click_list_first_set_password_cancle_button_action(self):
        """
        动作：点击重置密码取消按钮
        :return: 点击'重置密码取消按钮'按钮后的页面
        """
        self.project.click(self.list_first_set_password_cancle_button)
        return self.project.get_current_page_source()

    def click_tab_list_button_action(self):
        """
        动作：点击tab
        :return: 点击'tab'按钮后的页面
        """
        self.project.click(self.tab_list_button)
        return self.project.get_current_page_source()

    def click_loginout_button_action(self):
        """
        动作：点击退出登录按钮
        :return: 点击'退出登录按钮'按钮后的页面
        """
        self.project.click(self.loginout_button)
        return self.project.get_current_page_source()

    def click_white_button_action(self):
        """
        动作：点击空白
        :return: 点击'空白'按钮后的页面
        """
        self.project.click(self.white_button)
        return self.project.get_current_page_source()

    # endregion Actions
