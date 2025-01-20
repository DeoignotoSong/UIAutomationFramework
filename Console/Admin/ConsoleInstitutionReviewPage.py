from Utils.Log import log

"""
后台-用户中心-机构院校管理-机构院校审核
console_url/university/apply
"""


class ConsoleInstitutionReviewPage:
    def __init__(self, project):
        self.project = project
        self.url = 'console_url/university/apply'
        # region Fields
        # 提交成功提示信息
        self._message_content_text_tag = '/html/body/div[last()]/div/div[1]/p'
        # 下拉菜单
        self._drop_down_list_select_tag = '/html/body/div[@class="el-select-dropdown el-popper" and @x-placement="bottom-start"]/div[1]/div[1]/ul'
        # 用户中心导航
        self._console_user_center_top_button_tag = '//*[@id="app"]/div/header/div[2]/ul/li[3]'
        # 机构院校管理左侧导航
        self._console_institution_manage_left_button_tag = '//*[@id="app"]/div/section/aside/ul/li[1]/div/span'
        # 机构院校审核列表按钮
        self._console_institution_review_button_tag = '//*[@id="app"]/div/section/aside/ul/li[1]/ul/li[3]/span'
        # 机构院校审核表名
        self._console_institution_review_name_text_tag = '//*[@id="app"]/div/section/main/div/div[1]/div[2]/ul/li'
        # 联系人电话输入
        self._console_contact_mobile_input_tag = '//*[@id="tableSearch"]/form/div/div[1]/div/div/input'
        # 所属国家
        self._console_at_country_button_tag = '//*[@id="tableSearch"]/form/div/div[2]/div/div/div[1]/input'
        # 状态
        self._console_status_button_tag = '//*[@id="tableSearch"]/form/div/div[3]/div/div/div/input'
        # 状态(正常)
        self._console_status_on_button_tag = '/html/body/div[2]/div[1]/div[1]/ul/li[2]'
        # 状态(禁用)
        self._console_status_off_button_tag = '/html/body/div[2]/div[1]/div[1]/ul/li[3]'
        # 联系人姓名输入
        self._console_contact_name_input_tag = '//*[@id="tableSearch"]/form/div/div[4]/div/div/input'
        # 类型
        self._console_category_button_tag = '//*[@id="tableSearch"]/form/div/div[6]/div/div/div/input'
        # 类别(机构)
        self._console_category_institution_button_tag = '/html/body/div[3]/div[1]/div[1]/ul/li[2]'
        # 类别(院校)
        self._console_category_school_button_tag = '/html/body/div[3]/div[1]/div[1]/ul/li[3]'
        # 机构院校名称输入
        self._console_institution_school_name_input_tag = '//*[@id="tableSearch"]/form/div/div[last()-2]/div/div/input'
        # 查询按钮
        self._console_inquiry_button_tag = '//*[@id="tableSearch"]/form/div/div[last()-1]/div/button'
        # 清除按钮
        self._console_clean_button_tag = '//*[@id="tableSearch"]/form/div/div[last()]/div/button/span'
        # 查询数据名称
        self._console_inquiry_value_name_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div[1]/div[3]/table/tbody/tr/td[2]/div'
        # 审核操作按钮
        self._console_inquiry_value_review_button_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div[1]/div[4]/div[2]/table/tbody/tr/td[11]/div/a/span'
        # 审核页面表单名称
        self._console_review_form_name_text_tag = '//*[@id="app"]/div/section/main/div/div[1]/div[2]/ul/li'
        # 不通过原因输入
        self._console_review_not_pass_input_tag = '//*[@id="app"]/div/section/main/div/div[2]/div/div[2]/form/div[last()-1]/div/div/div/div/textarea'
        # 不通过按钮
        self._console_review_no_pass_button_tag = '//*[@id="app"]/div/section/main/div/div[2]/div/div[2]/form/div[last()]/div[1]/div/div/button[2]/span'
        # 通过按钮
        self._console_review_pass_button_tag = '//*[@id="app"]/div/section/main/div/div[2]/div/div[2]/form/div[last()]/div[1]/div/div/button[1]/span'
        # 审核后数据状态
        self._console_review_value_status_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div[1]/div[3]/table/tbody/tr/td[8]/div'
        # endregion Fields

    # region Properties
    @property
    def message_content_text(self):
        """
        属性: 提交成功提示信息
        :return: 提交成功提示信息
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
    def console_user_center_top_button(self):
        """
        属性: 用户中心导航
        :return: 用户中心导航
        """
        element = None
        try:
            element = self.project.get_element(self._console_user_center_top_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def console_institution_manage_left_button(self):
        """
        属性: 机构院校管理左侧导航
        :return: 机构院校管理左侧导航
        """
        element = None
        try:
            element = self.project.get_element(self._console_institution_manage_left_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def console_institution_review_button(self):
        """
        属性: 机构院校审核列表按钮
        :return: 机构院校审核列表按钮
        """
        element = None
        try:
            element = self.project.get_element(self._console_institution_review_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def console_institution_review_name_text(self):
        """
        属性: 机构院校审核表名
        :return: 机构院校审核表名
        """
        element = None
        try:
            element = self.project.get_element(self._console_institution_review_name_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def console_contact_mobile_input(self):
        """
        属性: 联系人电话输入
        :return: 联系人电话输入
        """
        element = None
        try:
            element = self.project.get_element(self._console_contact_mobile_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def console_at_country_button(self):
        """
        属性: 所属国家
        :return: 所属国家
        """
        element = None
        try:
            element = self.project.get_element(self._console_at_country_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def console_status_button(self):
        """
        属性: 状态
        :return: 状态
        """
        element = None
        try:
            element = self.project.get_element(self._console_status_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def console_status_on_button(self):
        """
        属性: 状态(正常)
        :return: 状态(正常)
        """
        element = None
        try:
            element = self.project.get_element(self._console_status_on_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def console_status_off_button(self):
        """
        属性: 状态(禁用)
        :return: 状态(禁用)
        """
        element = None
        try:
            element = self.project.get_element(self._console_status_off_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def console_contact_name_input(self):
        """
        属性: 联系人姓名输入
        :return: 联系人姓名输入
        """
        element = None
        try:
            element = self.project.get_element(self._console_contact_name_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def console_category_button(self):
        """
        属性: 类型
        :return: 类型
        """
        element = None
        try:
            element = self.project.get_element(self._console_category_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def console_category_institution_button(self):
        """
        属性: 类别(机构)
        :return: 类别(机构)
        """
        element = None
        try:
            element = self.project.get_element(self._console_category_institution_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def console_category_school_button(self):
        """
        属性: 类别(院校)
        :return: 类别(院校)
        """
        element = None
        try:
            element = self.project.get_element(self._console_category_school_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def console_institution_school_name_input(self):
        """
        属性: 机构院校名称输入
        :return: 机构院校名称输入
        """
        element = None
        try:
            element = self.project.get_element(self._console_institution_school_name_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def console_inquiry_button(self):
        """
        属性: 查询按钮
        :return: 查询按钮
        """
        element = None
        try:
            element = self.project.get_element(self._console_inquiry_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def console_clean_button(self):
        """
        属性: 清除按钮
        :return: 清除按钮
        """
        element = None
        try:
            element = self.project.get_element(self._console_clean_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def console_inquiry_value_name_text(self):
        """
        属性: 查询数据名称
        :return: 查询数据名称
        """
        element = None
        try:
            element = self.project.get_element(self._console_inquiry_value_name_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def console_inquiry_value_review_button(self):
        """
        属性: 审核操作按钮
        :return: 审核操作按钮
        """
        element = None
        try:
            element = self.project.get_element(self._console_inquiry_value_review_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def console_review_form_name_text(self):
        """
        属性: 审核页面表单名称
        :return: 审核页面表单名称
        """
        element = None
        try:
            element = self.project.get_element(self._console_review_form_name_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def console_review_not_pass_input(self):
        """
        属性: 不通过原因输入
        :return: 不通过原因输入
        """
        element = None
        try:
            element = self.project.get_element(self._console_review_not_pass_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def console_review_no_pass_button(self):
        """
        属性: 不通过按钮
        :return: 不通过按钮
        """
        element = None
        try:
            element = self.project.get_element(self._console_review_no_pass_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def console_review_pass_button(self):
        """
        属性: 通过按钮
        :return: 通过按钮
        """
        element = None
        try:
            element = self.project.get_element(self._console_review_pass_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def console_review_value_status_text(self):
        """
        属性: 审核后数据状态
        :return: 审核后数据状态
        """
        element = None
        try:
            element = self.project.get_element(self._console_review_value_status_text_tag)
        except AttributeError as error:
            log(error)
        return element

    # endregion Properties

    # region Actions
    def get_message_content_text_action(self):
        """
        动作：获取提交成功提示信息的文本
        :return: '提交成功提示信息'的文本
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

    def click_console_user_center_top_button_action(self):
        """
        动作：点击用户中心导航
        :return: 点击'用户中心导航'按钮后的页面
        """
        self.project.click(self.console_user_center_top_button)
        return self.project.get_current_page_source()

    def click_console_institution_manage_left_button_action(self):
        """
        动作：点击机构院校管理左侧导航
        :return: 点击'机构院校管理左侧导航'按钮后的页面
        """
        self.project.click(self.console_institution_manage_left_button)
        return self.project.get_current_page_source()

    def click_console_institution_review_button_action(self):
        """
        动作：点击机构院校审核列表按钮
        :return: 点击'机构院校审核列表按钮'按钮后的页面
        """
        self.project.click(self.console_institution_review_button)
        return self.project.get_current_page_source()

    def get_console_institution_review_name_text_action(self):
        """
        动作：获取机构院校审核表名的文本
        :return: '机构院校审核表名'的文本
        """
        control_content = self.project.get_element_text(self.console_institution_review_name_text)
        return control_content

    def set_console_contact_mobile_input_action(self, console_contact_mobile_input):
        """
        动作：设置联系人电话输入
        :param console_contact_mobile_input: 联系人电话输入
        :return: 设置'联系人电话输入'文本后的页面
        """
        self.project.clear_and_send_keys(self.console_contact_mobile_input, console_contact_mobile_input)
        return self.project.get_current_page_source()

    def click_console_at_country_button_action(self):
        """
        动作：点击所属国家
        :return: 点击'所属国家'按钮后的页面
        """
        self.project.click(self.console_at_country_button)
        return self.project.get_current_page_source()

    def click_console_status_button_action(self):
        """
        动作：点击状态
        :return: 点击'状态'按钮后的页面
        """
        self.project.click(self.console_status_button)
        return self.project.get_current_page_source()

    def click_console_status_on_button_action(self):
        """
        动作：点击状态(正常)
        :return: 点击'状态(正常)'按钮后的页面
        """
        self.project.click(self.console_status_on_button)
        return self.project.get_current_page_source()

    def click_console_status_off_button_action(self):
        """
        动作：点击状态(禁用)
        :return: 点击'状态(禁用)'按钮后的页面
        """
        self.project.click(self.console_status_off_button)
        return self.project.get_current_page_source()

    def set_console_contact_name_input_action(self, console_contact_name_input):
        """
        动作：设置联系人姓名输入
        :param console_contact_name_input: 联系人姓名输入
        :return: 设置'联系人姓名输入'文本后的页面
        """
        self.project.clear_and_send_keys(self.console_contact_name_input, console_contact_name_input)
        return self.project.get_current_page_source()

    def click_console_category_button_action(self):
        """
        动作：点击类型
        :return: 点击'类型'按钮后的页面
        """
        self.project.click(self.console_category_button)
        return self.project.get_current_page_source()

    def click_console_category_institution_button_action(self):
        """
        动作：点击类别(机构)
        :return: 点击'类别(机构)'按钮后的页面
        """
        self.project.click(self.console_category_institution_button)
        return self.project.get_current_page_source()

    def click_console_category_school_button_action(self):
        """
        动作：点击类别(院校)
        :return: 点击'类别(院校)'按钮后的页面
        """
        self.project.click(self.console_category_school_button)
        return self.project.get_current_page_source()

    def set_console_institution_school_name_input_action(self, console_institution_school_name_input):
        """
        动作：设置机构院校名称输入
        :param console_institution_school_name_input: 机构院校名称输入
        :return: 设置'机构院校名称输入'文本后的页面
        """
        self.project.clear_and_send_keys(self.console_institution_school_name_input, console_institution_school_name_input)
        return self.project.get_current_page_source()

    def click_console_inquiry_button_action(self):
        """
        动作：点击查询按钮
        :return: 点击'查询按钮'按钮后的页面
        """
        self.project.click(self.console_inquiry_button)
        return self.project.get_current_page_source()

    def click_console_clean_button_action(self):
        """
        动作：点击清除按钮
        :return: 点击'清除按钮'按钮后的页面
        """
        self.project.click(self.console_clean_button)
        return self.project.get_current_page_source()

    def get_console_inquiry_value_name_text_action(self):
        """
        动作：获取查询数据名称的文本
        :return: '查询数据名称'的文本
        """
        control_content = self.project.get_element_text(self.console_inquiry_value_name_text)
        return control_content

    def click_console_inquiry_value_review_button_action(self):
        """
        动作：点击审核操作按钮
        :return: 点击'审核操作按钮'按钮后的页面
        """
        self.project.click(self.console_inquiry_value_review_button)
        return self.project.get_current_page_source()

    def get_console_review_form_name_text_action(self):
        """
        动作：获取审核页面表单名称的文本
        :return: '审核页面表单名称'的文本
        """
        control_content = self.project.get_element_text(self.console_review_form_name_text)
        return control_content

    def set_console_review_not_pass_input_action(self, console_review_not_pass_input):
        """
        动作：设置不通过原因输入
        :param console_review_not_pass_input: 不通过原因输入
        :return: 设置'不通过原因输入'文本后的页面
        """
        self.project.clear_and_send_keys(self.console_review_not_pass_input, console_review_not_pass_input)
        return self.project.get_current_page_source()

    def click_console_review_no_pass_button_action(self):
        """
        动作：点击不通过按钮
        :return: 点击'不通过按钮'按钮后的页面
        """
        self.project.click(self.console_review_no_pass_button)
        return self.project.get_current_page_source()

    def click_console_review_pass_button_action(self):
        """
        动作：点击通过按钮
        :return: 点击'通过按钮'按钮后的页面
        """
        self.project.click(self.console_review_pass_button)
        return self.project.get_current_page_source()

    def get_console_review_value_status_text_action(self):
        """
        动作：获取审核后数据状态的文本
        :return: '审核后数据状态'的文本
        """
        control_content = self.project.get_element_text(self.console_review_value_status_text)
        return control_content

    # endregion Actions
