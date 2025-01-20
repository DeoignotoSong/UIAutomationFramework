from Utils.Log import log


"""
后台-留学审核管理-上下架审核
console_url/abroad_center/examine/shelf_list
"""


class ConsoleAbroadCenterExamineShelfListPage:
    def __init__(self, project):
        self.project = project
        self.url = 'console_url/abroad_center/goods_management/relation/PR020100039353'
        # region Fields
        # 消息提示
        self._message_content_text_tag = '/html/body/div[last()]/div/div[1]/p'
        # 搜索商品编码
        self._search_shelf_product_code_input_tag = '/html/body/div/div/section/main/div/div[2]/div[1]/form/div/div[1]/div/div/input'
        # 搜索商品名称
        self._search_shelf_goods_name_input_tag = '/html/body/div/div/section/main/div/div[2]/div[1]/form/div/div[2]/div/div/input'
        # 重置按钮
        self._clear_shelf_button_tag = '/html/body/div[1]/div/section/main/div/div[2]/div[1]/form/div/div[8]/div/button'
        # 查询按钮
        self._search_shelf_button_tag = '/html/body/div[1]/div/section/main/div/div[2]/div[1]/form/div/div[9]/div/button'
        # 列表第一条数据的商品编码
        self._first_shelf_product_code_text_tag = '/html/body/div[1]/div/section/main/div/div[2]/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[1]/div'
        # 列表第一条数据的商品名称
        self._first_shelf_product_name_text_tag = '/html/body/div[1]/div/section/main/div/div[2]/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[2]/div/a/span'
        # 列表第一条数据的商品名称按钮
        self._first_shelf_product_name_button_tag = '/html/body/div[1]/div/section/main/div/div[2]/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[2]/div/a/span'
        # 列表第一条数据的所属国家及地区
        self._first_shelf_country_text_tag = '/html/body/div[1]/div/section/main/div/div[2]/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[3]/div'
        # 列表第一条数据的上架方式
        self._first_shelf_upper_text_tag = '/html/body/div[1]/div/section/main/div/div[2]/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[4]/div'
        # 列表第一条数据的上架时间
        self._first_shelf_upper_time_text_tag = '/html/body/div[1]/div/section/main/div/div[2]/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[5]/div'
        # 列表第一条数据的审核状态
        self._first_shelf_audit_state_text_tag = '/html/body/div[1]/div/section/main/div/div[2]/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[6]/div'
        # 列表第一条数据的操作文案
        self._first_shelf_option_text_tag = '/html/body/div[1]/div/section/main/div/div[2]/div[2]/div[1]/div[4]/div[2]/table/tbody/tr[1]/td[8]/div/a/span'
        # 列表第一条数据的操作审核通过
        self._first_shelf_pass_button_tag = '/html/body/div[1]/div/section/main/div/div[2]/div[2]/div[1]/div[4]/div[2]/table/tbody/tr[1]/td[8]/div/a/span'
        # 列表第一条数据的操作审核通过确认
        self._first_shelf_pass_commit_button_tag = '/html/body/div[2]/div/div[3]/button[2]'
        # 列表第一条数据的操作审核不通过
        self._first_shelf_unpass_button_tag = '/html/body/div[1]/div/section/main/div/div[2]/div[2]/div[1]/div[4]/div[2]/table/tbody/tr/td[8]/div/a[2]/span'
        # 列表第一条数据的操作驳回审核理由
        self._first_shelf_reason_input_tag = '/html/body/div[1]/div/section/main/div/div[3]/div/div[2]/form/div/div/div[1]/textarea'
        # 列表第一条数据的操作审核不通过确认
        self._first_shelf_unpass_commit_button_tag = '/html/body/div[1]/div/section/main/div/div[3]/div/div[3]/div/button[2]'
        # 列表审核记录
        self._first_shelf_audit_his_button_tag = '/html/body/div[1]/div/section/main/div/div[2]/div[2]/div[1]/div[4]/div[2]/table/tbody/tr/td[8]/div/a/span'
        # 列表审核记录关闭按钮
        self._first_shelf_audit_his_close_button_tag = '/html/body/div[1]/div/section/main/div/div[4]/div/div/div[1]/button/i'
        # 列表第一条数据的审核记录
        self._first_shelf_audit_his_result_text_tag = '/html/body/div[1]/div/section/main/div/div[4]/div/div/div[2]/div/div/div[3]/table/tbody/tr/td[3]/div'
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
    def search_shelf_product_code_input(self):
        """
        属性: 搜索商品编码
        :return: 搜索商品编码
        """
        element = None
        try:
            element = self.project.get_element(self._search_shelf_product_code_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def search_shelf_goods_name_input(self):
        """
        属性: 搜索商品名称
        :return: 搜索商品名称
        """
        element = None
        try:
            element = self.project.get_element(self._search_shelf_goods_name_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def clear_shelf_button(self):
        """
        属性: 重置按钮
        :return: 重置按钮
        """
        element = None
        try:
            element = self.project.get_element(self._clear_shelf_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def search_shelf_button(self):
        """
        属性: 查询按钮
        :return: 查询按钮
        """
        element = None
        try:
            element = self.project.get_element(self._search_shelf_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def first_shelf_product_code_text(self):
        """
        属性: 列表第一条数据的商品编码
        :return: 列表第一条数据的商品编码
        """
        element = None
        try:
            element = self.project.get_element(self._first_shelf_product_code_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def first_shelf_product_name_text(self):
        """
        属性: 列表第一条数据的商品名称
        :return: 列表第一条数据的商品名称
        """
        element = None
        try:
            element = self.project.get_element(self._first_shelf_product_name_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def first_shelf_product_name_button(self):
        """
        属性: 列表第一条数据的商品名称按钮
        :return: 列表第一条数据的商品名称按钮
        """
        element = None
        try:
            element = self.project.get_element(self._first_shelf_product_name_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def first_shelf_country_text(self):
        """
        属性: 列表第一条数据的所属国家及地区
        :return: 列表第一条数据的所属国家及地区
        """
        element = None
        try:
            element = self.project.get_element(self._first_shelf_country_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def first_shelf_upper_text(self):
        """
        属性: 列表第一条数据的上架方式
        :return: 列表第一条数据的上架方式
        """
        element = None
        try:
            element = self.project.get_element(self._first_shelf_upper_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def first_shelf_upper_time_text(self):
        """
        属性: 列表第一条数据的上架时间
        :return: 列表第一条数据的上架时间
        """
        element = None
        try:
            element = self.project.get_element(self._first_shelf_upper_time_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def first_shelf_audit_state_text(self):
        """
        属性: 列表第一条数据的审核状态
        :return: 列表第一条数据的审核状态
        """
        element = None
        try:
            element = self.project.get_element(self._first_shelf_audit_state_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def first_shelf_option_text(self):
        """
        属性: 列表第一条数据的操作文案
        :return: 列表第一条数据的操作文案
        """
        element = None
        try:
            element = self.project.get_element(self._first_shelf_option_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def first_shelf_pass_button(self):
        """
        属性: 列表第一条数据的操作审核通过
        :return: 列表第一条数据的操作审核通过
        """
        element = None
        try:
            element = self.project.get_element(self._first_shelf_pass_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def first_shelf_pass_commit_button(self):
        """
        属性: 列表第一条数据的操作审核通过确认
        :return: 列表第一条数据的操作审核通过确认
        """
        element = None
        try:
            element = self.project.get_element(self._first_shelf_pass_commit_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def first_shelf_unpass_button(self):
        """
        属性: 列表第一条数据的操作审核不通过
        :return: 列表第一条数据的操作审核不通过
        """
        element = None
        try:
            element = self.project.get_element(self._first_shelf_unpass_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def first_shelf_reason_input(self):
        """
        属性: 列表第一条数据的操作驳回审核理由
        :return: 列表第一条数据的操作驳回审核理由
        """
        element = None
        try:
            element = self.project.get_element(self._first_shelf_reason_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def first_shelf_unpass_commit_button(self):
        """
        属性: 列表第一条数据的操作审核不通过确认
        :return: 列表第一条数据的操作审核不通过确认
        """
        element = None
        try:
            element = self.project.get_element(self._first_shelf_unpass_commit_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def first_shelf_audit_his_button(self):
        """
        属性: 列表审核记录
        :return: 列表审核记录
        """
        element = None
        try:
            element = self.project.get_element(self._first_shelf_audit_his_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def first_shelf_audit_his_close_button(self):
        """
        属性: 列表审核记录关闭按钮
        :return: 列表审核记录关闭按钮
        """
        element = None
        try:
            element = self.project.get_element(self._first_shelf_audit_his_close_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def first_shelf_audit_his_result_text(self):
        """
        属性: 列表第一条数据的审核记录
        :return: 列表第一条数据的审核记录
        """
        element = None
        try:
            element = self.project.get_element(self._first_shelf_audit_his_result_text_tag)
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

    def set_search_shelf_product_code_input_action(self, search_shelf_product_code_input):
        """
        动作：设置搜索商品编码
        :param search_shelf_product_code_input: 搜索商品编码
        :return: 设置'搜索商品编码'文本后的页面
        """
        self.project.clear_and_send_keys(self.search_shelf_product_code_input, search_shelf_product_code_input)
        return self.project.get_current_page_source()

    def set_search_shelf_goods_name_input_action(self, search_shelf_goods_name_input):
        """
        动作：设置搜索商品名称
        :param search_shelf_goods_name_input: 搜索商品名称
        :return: 设置'搜索商品名称'文本后的页面
        """
        self.project.clear_and_send_keys(self.search_shelf_goods_name_input, search_shelf_goods_name_input)
        return self.project.get_current_page_source()

    def click_clear_shelf_button_action(self):
        """
        动作：点击重置按钮
        :return: 点击'重置按钮'按钮后的页面
        """
        self.project.click(self.clear_shelf_button)
        return self.project.get_current_page_source()

    def click_search_shelf_button_action(self):
        """
        动作：点击查询按钮
        :return: 点击'查询按钮'按钮后的页面
        """
        self.project.click(self.search_shelf_button)
        return self.project.get_current_page_source()

    def get_first_shelf_product_code_text_action(self):
        """
        动作：获取列表第一条数据的商品编码的文本
        :return: '列表第一条数据的商品编码'的文本
        """
        control_content = self.project.get_element_text(self.first_shelf_product_code_text)
        return control_content

    def get_first_shelf_product_name_text_action(self):
        """
        动作：获取列表第一条数据的商品名称的文本
        :return: '列表第一条数据的商品名称'的文本
        """
        control_content = self.project.get_element_text(self.first_shelf_product_name_text)
        return control_content

    def click_first_shelf_product_name_button_action(self):
        """
        动作：点击列表第一条数据的商品名称按钮
        :return: 点击'列表第一条数据的商品名称按钮'按钮后的页面
        """
        self.project.click(self.first_shelf_product_name_button)
        return self.project.get_current_page_source()

    def get_first_shelf_country_text_action(self):
        """
        动作：获取列表第一条数据的所属国家及地区的文本
        :return: '列表第一条数据的所属国家及地区'的文本
        """
        control_content = self.project.get_element_text(self.first_shelf_country_text)
        return control_content

    def get_first_shelf_upper_text_action(self):
        """
        动作：获取列表第一条数据的上架方式的文本
        :return: '列表第一条数据的上架方式'的文本
        """
        control_content = self.project.get_element_text(self.first_shelf_upper_text)
        return control_content

    def get_first_shelf_upper_time_text_action(self):
        """
        动作：获取列表第一条数据的上架时间的文本
        :return: '列表第一条数据的上架时间'的文本
        """
        control_content = self.project.get_element_text(self.first_shelf_upper_time_text)
        return control_content

    def get_first_shelf_audit_state_text_action(self):
        """
        动作：获取列表第一条数据的审核状态的文本
        :return: '列表第一条数据的审核状态'的文本
        """
        control_content = self.project.get_element_text(self.first_shelf_audit_state_text)
        return control_content

    def get_first_shelf_option_text_action(self):
        """
        动作：获取列表第一条数据的操作文案的文本
        :return: '列表第一条数据的操作文案'的文本
        """
        control_content = self.project.get_element_text(self.first_shelf_option_text)
        return control_content

    def click_first_shelf_pass_button_action(self):
        """
        动作：点击列表第一条数据的操作审核通过
        :return: 点击'列表第一条数据的操作审核通过'按钮后的页面
        """
        self.project.click(self.first_shelf_pass_button)
        return self.project.get_current_page_source()

    def click_first_shelf_pass_commit_button_action(self):
        """
        动作：点击列表第一条数据的操作审核通过确认
        :return: 点击'列表第一条数据的操作审核通过确认'按钮后的页面
        """
        self.project.click(self.first_shelf_pass_commit_button)
        return self.project.get_current_page_source()

    def click_first_shelf_unpass_button_action(self):
        """
        动作：点击列表第一条数据的操作审核不通过
        :return: 点击'列表第一条数据的操作审核不通过'按钮后的页面
        """
        self.project.click(self.first_shelf_unpass_button)
        return self.project.get_current_page_source()

    def set_first_shelf_reason_input_action(self, first_shelf_reason_input):
        """
        动作：设置列表第一条数据的操作驳回审核理由
        :param first_shelf_reason_input: 列表第一条数据的操作驳回审核理由
        :return: 设置'列表第一条数据的操作驳回审核理由'文本后的页面
        """
        self.project.clear_and_send_keys(self.first_shelf_reason_input, first_shelf_reason_input)
        return self.project.get_current_page_source()

    def click_first_shelf_unpass_commit_button_action(self):
        """
        动作：点击列表第一条数据的操作审核不通过确认
        :return: 点击'列表第一条数据的操作审核不通过确认'按钮后的页面
        """
        self.project.click(self.first_shelf_unpass_commit_button)
        return self.project.get_current_page_source()

    def click_first_shelf_audit_his_button_action(self):
        """
        动作：点击列表审核记录
        :return: 点击'列表审核记录'按钮后的页面
        """
        self.project.click(self.first_shelf_audit_his_button)
        return self.project.get_current_page_source()

    def click_first_shelf_audit_his_close_button_action(self):
        """
        动作：点击列表审核记录关闭按钮
        :return: 点击'列表审核记录关闭按钮'按钮后的页面
        """
        self.project.click(self.first_shelf_audit_his_close_button)
        return self.project.get_current_page_source()

    def get_first_shelf_audit_his_result_text_action(self):
        """
        动作：获取列表第一条数据的审核记录的文本
        :return: '列表第一条数据的审核记录'的文本
        """
        control_content = self.project.get_element_text(self.first_shelf_audit_his_result_text)
        return control_content

    # endregion Actions
