from Utils.Log import log

"""
后台-留学中心-留学审核管理-服务审核
console_url/abroad_center/service_audit
"""

class ConsoleAbroadCenterServiceAuditPage:
    def __init__(self, project):
        self.project = project
        self.url = 'console_url/abroad_center/service_audit'
        # region Fields
        # 消息提示
        self._message_content_text_tag = '/html/body/div[last()]/div/div[1]/p'
        # 搜索服务编码输入框
        self._search_service_id_input_tag = '/html/body/div/div/section/main/div/div[2]/form/div/div[1]/div/div/input'
        # 搜索服务名称
        self._search_service_name_input_tag = '/html/body/div/div/section/main/div/div[2]/form/div/div[2]/div/div/input'
        # 搜索所属国家及地区
        self._search_service_country_place_list_select_tag = '/html/body/div[1]/div/section/main/div/div[2]/form/div/div[3]/div/div/div/input'
        # 搜索所属国家及地区全部
        self._search_service_country_place_all_button_tag = '/html/body/div[2]/div[1]/div[1]/ul/li[1]'
        # 搜索所属国家及地区美国
        self._search_service_country_place_america_button_tag = '/html/body/div[2]/div[1]/div[1]/ul/li[2]'
        # 搜索所属国家及地区澳大利亚
        self._search_service_country_place_australia_button_tag = '/html/body/div[2]/div[1]/div[1]/ul/li[3]'
        # 搜索审核状态
        self._search_service_audit_state_list_select_tag = '/html/body/div[1]/div/section/main/div/div[2]/form/div/div[4]/div/div/div/input'
        # 搜索审核状态全部
        self._search_service_audit_state_all_button_tag = '/html/body/div[3]/div[1]/div[1]/ul/li[1]'
        # 搜索审核状态待审核
        self._search_service_audit_state_wait_button_tag = '/html/body/div[3]/div[1]/div[1]/ul/li[2]'
        # 搜索审核状态审核通过
        self._search_service_audit_state_pass_button_tag = '/html/body/div[3]/div[1]/div[1]/ul/li[3]'
        # 搜索审核状态审核未通过
        self._search_service_audit_state_unpass_button_tag = '/html/body/div[3]/div[1]/div[1]/ul/li[4]'
        # 搜索查询按钮
        self._search_service_audit_search_button_tag = '/html/body/div/div/section/main/div/div[2]/form/div/div[5]/div/button'
        # 搜索清除按钮
        self._search_service_audit_clear_button_tag = '/html/body/div/div/section/main/div/div[2]/form/div/div[6]/div/button'
        # 服务列表第一条数据服务编码
        self._first_list_service_id_text_tag = '/html/body/div[1]/div/section/main/div/div[3]/div[1]/div[3]/table/tbody/tr[1]/td[1]/div'
        # 服务列表第一条数据服务名称
        self._first_list_service_name_text_tag = '/html/body/div[1]/div/section/main/div/div[3]/div[1]/div[3]/table/tbody/tr[1]/td[2]/div/a/span'
        # 服务列表第一条数据服务名称点击
        self._first_list_service_name_button_tag = '/html/body/div[1]/div/section/main/div/div[3]/div[1]/div[3]/table/tbody/tr[1]/td[2]/div/a'
        # 服务列表第一条数据所属国家及地区
        self._first_list_service_country_place_text_tag = '/html/body/div[1]/div/section/main/div/div[3]/div[1]/div[3]/table/tbody/tr[1]/td[3]/div'
        # 服务列表第一条数据价格
        self._first_list_service_price_text_tag = '/html/body/div[1]/div/section/main/div/div[3]/div[1]/div[3]/table/tbody/tr[1]/td[4]/div'
        # 服务列表第一条数据审核状态
        self._first_list_service_audit_state_text_tag = '/html/body/div[1]/div/section/main/div/div[3]/div[1]/div[3]/table/tbody/tr[1]/td[5]/div'
        # 服务列表第一条数据操作审核文本
        self._first_service_audit_text_tag = '/html/body/div[1]/div/section/main/div/div[3]/div[1]/div[4]/div[2]/table/tbody/tr[1]/td[6]/div/a/span'
        # 服务列表第一条数据操作审核按钮
        self._first_service_audit_button_tag = '/html/body/div/div/section/main/div/div[3]/div[1]/div[4]/div[2]/table/tbody/tr[1]/td[6]/div/a/span'
        # 服务列表第一条数据操作审核通过按钮
        self._first_service_audit_passs_button_tag = '/html/body/div/div/section/main/div/div[3]/div/button[1]'
        # 服务列表第一条数据操作审核不通过按钮
        self._first_service_audit_unpass_button_tag = '/html/body/div/div/section/main/div/div[3]/div/button[2]'
        # 服务列表第一条数据操作审核驳回理由
        self._first_service_audit_unpass_input_tag = '/html/body/div[1]/div/section/main/div/div[4]/div/div[2]/form/div/div/div[1]/textarea'
        # 服务列表第一条数据操作审核驳回理由确认按钮
        self._first_service_audit_commit_unpass_button_tag = '/html/body/div[1]/div/section/main/div/div[4]/div/div[3]/div/button[2]'
        # 服务列表第一条数据操作审核通过确认按钮
        self._first_service_audit_commit_pass_button_tag = '/html/body/div[2]/div/div[3]/button[2]'
        # 服务列表第二页按钮
        self._service_audit_second_page_button_tag = '/html/body/div[1]/div/section/main/div/div[3]/div[2]/div[2]/div/div/ul/li[2]'
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
    def search_service_id_input(self):
        """
        属性: 搜索服务编码输入框
        :return: 搜索服务编码输入框
        """
        element = None
        try:
            element = self.project.get_element(self._search_service_id_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def search_service_name_input(self):
        """
        属性: 搜索服务名称
        :return: 搜索服务名称
        """
        element = None
        try:
            element = self.project.get_element(self._search_service_name_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def search_service_country_place_list_select(self):
        """
        属性: 搜索所属国家及地区
        :return: 搜索所属国家及地区
        """
        element = None
        try:
            element = self.project.get_element(self._search_service_country_place_list_select_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def search_service_country_place_all_button(self):
        """
        属性: 搜索所属国家及地区全部
        :return: 搜索所属国家及地区全部
        """
        element = None
        try:
            element = self.project.get_element(self._search_service_country_place_all_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def search_service_country_place_america_button(self):
        """
        属性: 搜索所属国家及地区美国
        :return: 搜索所属国家及地区美国
        """
        element = None
        try:
            element = self.project.get_element(self._search_service_country_place_america_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def search_service_country_place_australia_button(self):
        """
        属性: 搜索所属国家及地区澳大利亚
        :return: 搜索所属国家及地区澳大利亚
        """
        element = None
        try:
            element = self.project.get_element(self._search_service_country_place_australia_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def search_service_audit_state_list_select(self):
        """
        属性: 搜索审核状态
        :return: 搜索审核状态
        """
        element = None
        try:
            element = self.project.get_element(self._search_service_audit_state_list_select_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def search_service_audit_state_all_button(self):
        """
        属性: 搜索审核状态全部
        :return: 搜索审核状态全部
        """
        element = None
        try:
            element = self.project.get_element(self._search_service_audit_state_all_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def search_service_audit_state_wait_button(self):
        """
        属性: 搜索审核状态待审核
        :return: 搜索审核状态待审核
        """
        element = None
        try:
            element = self.project.get_element(self._search_service_audit_state_wait_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def search_service_audit_state_pass_button(self):
        """
        属性: 搜索审核状态审核通过
        :return: 搜索审核状态审核通过
        """
        element = None
        try:
            element = self.project.get_element(self._search_service_audit_state_pass_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def search_service_audit_state_unpass_button(self):
        """
        属性: 搜索审核状态审核未通过
        :return: 搜索审核状态审核未通过
        """
        element = None
        try:
            element = self.project.get_element(self._search_service_audit_state_unpass_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def search_service_audit_search_button(self):
        """
        属性: 搜索查询按钮
        :return: 搜索查询按钮
        """
        element = None
        try:
            element = self.project.get_element(self._search_service_audit_search_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def search_service_audit_clear_button(self):
        """
        属性: 搜索清除按钮
        :return: 搜索清除按钮
        """
        element = None
        try:
            element = self.project.get_element(self._search_service_audit_clear_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def first_list_service_id_text(self):
        """
        属性: 服务列表第一条数据服务编码
        :return: 服务列表第一条数据服务编码
        """
        element = None
        try:
            element = self.project.get_element(self._first_list_service_id_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def first_list_service_name_text(self):
        """
        属性: 服务列表第一条数据服务名称
        :return: 服务列表第一条数据服务名称
        """
        element = None
        try:
            element = self.project.get_element(self._first_list_service_name_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def first_list_service_name_button(self):
        """
        属性: 服务列表第一条数据服务名称点击
        :return: 服务列表第一条数据服务名称点击
        """
        element = None
        try:
            element = self.project.get_element(self._first_list_service_name_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def first_list_service_country_place_text(self):
        """
        属性: 服务列表第一条数据所属国家及地区
        :return: 服务列表第一条数据所属国家及地区
        """
        element = None
        try:
            element = self.project.get_element(self._first_list_service_country_place_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def first_list_service_price_text(self):
        """
        属性: 服务列表第一条数据价格
        :return: 服务列表第一条数据价格
        """
        element = None
        try:
            element = self.project.get_element(self._first_list_service_price_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def first_list_service_audit_state_text(self):
        """
        属性: 服务列表第一条数据审核状态
        :return: 服务列表第一条数据审核状态
        """
        element = None
        try:
            element = self.project.get_element(self._first_list_service_audit_state_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def first_service_audit_text(self):
        """
        属性: 服务列表第一条数据操作审核文本
        :return: 服务列表第一条数据操作审核文本
        """
        element = None
        try:
            element = self.project.get_element(self._first_service_audit_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def first_service_audit_button(self):
        """
        属性: 服务列表第一条数据操作审核按钮
        :return: 服务列表第一条数据操作审核按钮
        """
        element = None
        try:
            element = self.project.get_element(self._first_service_audit_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def first_service_audit_passs_button(self):
        """
        属性: 服务列表第一条数据操作审核通过按钮
        :return: 服务列表第一条数据操作审核通过按钮
        """
        element = None
        try:
            element = self.project.get_element(self._first_service_audit_passs_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def first_service_audit_unpass_button(self):
        """
        属性: 服务列表第一条数据操作审核不通过按钮
        :return: 服务列表第一条数据操作审核不通过按钮
        """
        element = None
        try:
            element = self.project.get_element(self._first_service_audit_unpass_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def first_service_audit_unpass_input(self):
        """
        属性: 服务列表第一条数据操作审核驳回理由
        :return: 服务列表第一条数据操作审核驳回理由
        """
        element = None
        try:
            element = self.project.get_element(self._first_service_audit_unpass_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def first_service_audit_commit_unpass_button(self):
        """
        属性: 服务列表第一条数据操作审核驳回理由确认按钮
        :return: 服务列表第一条数据操作审核驳回理由确认按钮
        """
        element = None
        try:
            element = self.project.get_element(self._first_service_audit_commit_unpass_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def first_service_audit_commit_pass_button(self):
        """
        属性: 服务列表第一条数据操作审核通过确认按钮
        :return: 服务列表第一条数据操作审核通过确认按钮
        """
        element = None
        try:
            element = self.project.get_element(self._first_service_audit_commit_pass_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def service_audit_second_page_button(self):
        """
        属性: 服务列表第二页按钮
        :return: 服务列表第二页按钮
        """
        element = None
        try:
            element = self.project.get_element(self._service_audit_second_page_button_tag)
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

    def set_search_service_id_input_action(self, search_service_id_input):
        """
        动作：设置搜索服务编码输入框
        :param search_service_id_input: 搜索服务编码输入框
        :return: 设置'搜索服务编码输入框'文本后的页面
        """
        self.project.clear_and_send_keys(self.search_service_id_input, search_service_id_input)
        return self.project.get_current_page_source()

    def set_search_service_name_input_action(self, search_service_name_input):
        """
        动作：设置搜索服务名称
        :param search_service_name_input: 搜索服务名称
        :return: 设置'搜索服务名称'文本后的页面
        """
        self.project.clear_and_send_keys(self.search_service_name_input, search_service_name_input)
        return self.project.get_current_page_source()

    def get_select_search_service_country_place_list_action(self, search_service_country_place_list_select):
        """
        动作：获取搜索所属国家及地区列表选中的文本
        :param search_service_country_place_list_select: 搜索所属国家及地区列表索引或文本
        :return: '搜索所属国家及地区'的文本
        """
        control_content = self.project.get_select_content(self.search_service_country_place_list_select, search_service_country_place_list_select)
        return control_content

    def select_search_service_country_place_list_action(self, search_service_country_place_list_select):
        """
        动作：选择搜索所属国家及地区
        :param search_service_country_place_list_select: 搜索所属国家及地区列表索引或文本
        :return: 选择'搜索所属国家及地区'选择器后的页面
        """
        self.project.select_control(self.search_service_country_place_list_select, search_service_country_place_list_select)
        return self.project.get_current_page_source()

    def click_search_service_country_place_all_button_action(self):
        """
        动作：点击搜索所属国家及地区全部
        :return: 点击'搜索所属国家及地区全部'按钮后的页面
        """
        self.project.click(self.search_service_country_place_all_button)
        return self.project.get_current_page_source()

    def click_search_service_country_place_america_button_action(self):
        """
        动作：点击搜索所属国家及地区美国
        :return: 点击'搜索所属国家及地区美国'按钮后的页面
        """
        self.project.click(self.search_service_country_place_america_button)
        return self.project.get_current_page_source()

    def click_search_service_country_place_australia_button_action(self):
        """
        动作：点击搜索所属国家及地区澳大利亚
        :return: 点击'搜索所属国家及地区澳大利亚'按钮后的页面
        """
        self.project.click(self.search_service_country_place_australia_button)
        return self.project.get_current_page_source()

    def get_select_search_service_audit_state_list_action(self, search_service_audit_state_list_select):
        """
        动作：获取搜索审核状态列表选中的文本
        :param search_service_audit_state_list_select: 搜索审核状态列表索引或文本
        :return: '搜索审核状态'的文本
        """
        control_content = self.project.get_select_content(self.search_service_audit_state_list_select, search_service_audit_state_list_select)
        return control_content

    def select_search_service_audit_state_list_action(self, search_service_audit_state_list_select):
        """
        动作：选择搜索审核状态
        :param search_service_audit_state_list_select: 搜索审核状态列表索引或文本
        :return: 选择'搜索审核状态'选择器后的页面
        """
        self.project.select_control(self.search_service_audit_state_list_select, search_service_audit_state_list_select)
        return self.project.get_current_page_source()

    def click_search_service_audit_state_all_button_action(self):
        """
        动作：点击搜索审核状态全部
        :return: 点击'搜索审核状态全部'按钮后的页面
        """
        self.project.click(self.search_service_audit_state_all_button)
        return self.project.get_current_page_source()

    def click_search_service_audit_state_wait_button_action(self):
        """
        动作：点击搜索审核状态待审核
        :return: 点击'搜索审核状态待审核'按钮后的页面
        """
        self.project.click(self.search_service_audit_state_wait_button)
        return self.project.get_current_page_source()

    def click_search_service_audit_state_pass_button_action(self):
        """
        动作：点击搜索审核状态审核通过
        :return: 点击'搜索审核状态审核通过'按钮后的页面
        """
        self.project.click(self.search_service_audit_state_pass_button)
        return self.project.get_current_page_source()

    def click_search_service_audit_state_unpass_button_action(self):
        """
        动作：点击搜索审核状态审核未通过
        :return: 点击'搜索审核状态审核未通过'按钮后的页面
        """
        self.project.click(self.search_service_audit_state_unpass_button)
        return self.project.get_current_page_source()

    def click_search_service_audit_search_button_action(self):
        """
        动作：点击搜索查询按钮
        :return: 点击'搜索查询按钮'按钮后的页面
        """
        self.project.click(self.search_service_audit_search_button)
        return self.project.get_current_page_source()

    def click_search_service_audit_clear_button_action(self):
        """
        动作：点击搜索清除按钮
        :return: 点击'搜索清除按钮'按钮后的页面
        """
        self.project.click(self.search_service_audit_clear_button)
        return self.project.get_current_page_source()

    def get_first_list_service_id_text_action(self):
        """
        动作：获取服务列表第一条数据服务编码的文本
        :return: '服务列表第一条数据服务编码'的文本
        """
        control_content = self.project.get_element_text(self.first_list_service_id_text)
        return control_content

    def get_first_list_service_name_text_action(self):
        """
        动作：获取服务列表第一条数据服务名称的文本
        :return: '服务列表第一条数据服务名称'的文本
        """
        control_content = self.project.get_element_text(self.first_list_service_name_text)
        return control_content

    def click_first_list_service_name_button_action(self):
        """
        动作：点击服务列表第一条数据服务名称点击
        :return: 点击'服务列表第一条数据服务名称点击'按钮后的页面
        """
        self.project.click(self.first_list_service_name_button)
        return self.project.get_current_page_source()

    def get_first_list_service_country_place_text_action(self):
        """
        动作：获取服务列表第一条数据所属国家及地区的文本
        :return: '服务列表第一条数据所属国家及地区'的文本
        """
        control_content = self.project.get_element_text(self.first_list_service_country_place_text)
        return control_content

    def get_first_list_service_price_text_action(self):
        """
        动作：获取服务列表第一条数据价格的文本
        :return: '服务列表第一条数据价格'的文本
        """
        control_content = self.project.get_element_text(self.first_list_service_price_text)
        return control_content

    def get_first_list_service_audit_state_text_action(self):
        """
        动作：获取服务列表第一条数据审核状态的文本
        :return: '服务列表第一条数据审核状态'的文本
        """
        control_content = self.project.get_element_text(self.first_list_service_audit_state_text)
        return control_content

    def get_first_service_audit_text_action(self):
        """
        动作：获取服务列表第一条数据操作审核文本的文本
        :return: '服务列表第一条数据操作审核文本'的文本
        """
        control_content = self.project.get_element_text(self.first_service_audit_text)
        return control_content

    def click_first_service_audit_button_action(self):
        """
        动作：点击服务列表第一条数据操作审核按钮
        :return: 点击'服务列表第一条数据操作审核按钮'按钮后的页面
        """
        self.project.click(self.first_service_audit_button)
        return self.project.get_current_page_source()

    def click_first_service_audit_passs_button_action(self):
        """
        动作：点击服务列表第一条数据操作审核通过按钮
        :return: 点击'服务列表第一条数据操作审核通过按钮'按钮后的页面
        """
        self.project.click(self.first_service_audit_passs_button)
        return self.project.get_current_page_source()

    def click_first_service_audit_unpass_button_action(self):
        """
        动作：点击服务列表第一条数据操作审核不通过按钮
        :return: 点击'服务列表第一条数据操作审核不通过按钮'按钮后的页面
        """
        self.project.click(self.first_service_audit_unpass_button)
        return self.project.get_current_page_source()

    def set_first_service_audit_unpass_input_action(self, first_service_audit_unpass_input):
        """
        动作：设置服务列表第一条数据操作审核驳回理由
        :param first_service_audit_unpass_input: 服务列表第一条数据操作审核驳回理由
        :return: 设置'服务列表第一条数据操作审核驳回理由'文本后的页面
        """
        self.project.clear_and_send_keys(self.first_service_audit_unpass_input, first_service_audit_unpass_input)
        return self.project.get_current_page_source()

    def click_first_service_audit_commit_unpass_button_action(self):
        """
        动作：点击服务列表第一条数据操作审核驳回理由确认按钮
        :return: 点击'服务列表第一条数据操作审核驳回理由确认按钮'按钮后的页面
        """
        self.project.click(self.first_service_audit_commit_unpass_button)
        return self.project.get_current_page_source()

    def click_first_service_audit_commit_pass_button_action(self):
        """
        动作：点击服务列表第一条数据操作审核通过确认按钮
        :return: 点击'服务列表第一条数据操作审核通过确认按钮'按钮后的页面
        """
        self.project.click(self.first_service_audit_commit_pass_button)
        return self.project.get_current_page_source()

    def click_service_audit_second_page_button_action(self):
        """
        动作：点击服务列表第二页按钮
        :return: 点击'服务列表第二页按钮'按钮后的页面
        """
        self.project.click(self.service_audit_second_page_button)
        return self.project.get_current_page_source()

    # endregion Actions
