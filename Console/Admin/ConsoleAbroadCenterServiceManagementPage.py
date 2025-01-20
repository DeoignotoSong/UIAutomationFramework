from Utils.Log import log

"""
后台-留学中心-商品服务管理-服务管理
console_url/advert/advert-add/add/0
"""

class ConsoleAbroadCenterServiceManagementPage:
    def __init__(self, project):
        self.project = project
        self.url = 'console_url/abroad_center/service_management'
        # region Fields
        # 消息提示
        self._message_content_text_tag = '/html/body/div[last()]/div/div[1]/p'
        # 搜索服务编码输入框
        self._search_service_id_input_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[1]/form/div[1]/div[1]/div/div/input'
        # 搜索服务名称
        self._search_service_name_input_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[1]/form/div[1]/div[2]/div/div/input'
        # 搜索所属国家及地区
        self._search_service_country_place_list_select_tag = '/html/body/div[3]/div[1]/div[1]/ul'
        # 搜索所属国家及地区全部
        self._search_service_country_place_all_button_tag = '/html/body/div[5]/div[1]/div[1]/ul/li[1]'
        # 搜索所属国家及地区美国
        self._search_service_country_place_america_button_tag = '/html/body/div[5]/div[1]/div[1]/ul/li[2]'
        # 搜索所属国家及地区澳大利亚
        self._search_service_country_place_australia_button_tag = '/html/body/div[5]/div[1]/div[1]/ul/li[3]'
        # 搜索状态
        self._search_service_state_list_select_tag = '/html/body/div[4]/div[1]/div[1]/ul'
        # 搜索状态全部
        self._search_service_state_all_button_tag = '/html/body/div[5]/div[1]/div[1]/ul/li[1]'
        # 搜索状态禁用
        self._search_service_state_ban_button_tag = '/html/body/div[5]/div[1]/div[1]/ul/li[2]'
        # 搜索状态启用
        self._search_service_state_use_button_tag = '/html/body/div[5]/div[1]/div[1]/ul/li[3]'
        # 搜索审核状态
        self._search_service_audit_state_list_select_tag = '/html/body/div[5]/div[1]/div[1]/ul'
        # 搜索审核状态全部
        self._search_service_audit_state_all_button_tag = '/html/body/div[5]/div[1]/div[1]/ul/li[1]'
        # 搜索审核状态待审核
        self._search_service_audit_state_wait_button_tag = '/html/body/div[5]/div[1]/div[1]/ul/li[2]'
        # 搜索审核状态审核通过
        self._search_service_audit_state_pass_button_tag = '/html/body/div[5]/div[1]/div[1]/ul/li[3]'
        # 搜索审核状态审核未通过
        self._search_service_audit_state_unpass_button_tag = '/html/body/div[5]/div[1]/div[1]/ul/li[4]'
        # 搜索查询按钮
        self._search_service_search_button_tag = '/html/body/div[1]/div/section/main/div/div[2]/div[1]/form/div[1]/div[6]/div/button'
        # 清除按钮
        self._clear_service_button_tag = '/html/body/div[1]/div/section/main/div/div[2]/div[1]/form/div[1]/div[7]/div/button'
        # 组合服务按钮
        self._add_service_button_tag = '/html/body/div[1]/div/section/main/div/div[2]/div[1]/form/div[2]/div/div/button'
        # 服务列表第一条数据服务编码
        self._first_list_service_id_text_tag = '/html/body/div[1]/div/section/main/div/div[2]/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[1]/div'
        # 服务列表第一条数据服务名称
        self._first_list_service_name_text_tag = '/html/body/div[1]/div/section/main/div/div[2]/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[2]/div/a/span'
        # 服务列表第一条数据服务名称点击
        self._first_list_service_name_button_tag = '/html/body/div[1]/div/section/main/div/div[2]/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[2]/div/a'
        # 服务列表第一条数据所属国家及地区
        self._first_list_service_country_place_text_tag = '/html/body/div[1]/div/section/main/div/div[2]/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[3]/div'
        # 服务列表第一条数据价格
        self._first_list_service_price_text_tag = '/html/body/div[1]/div/section/main/div/div[2]/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[4]/div'
        # 服务列表第一条数据审核状态
        self._first_list_service_audit_state_text_tag = '/html/body/div[1]/div/section/main/div/div[2]/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[5]/div'
        # 服务列表第一条数据操作禁用/启用
        self._first_service_ban_button_tag = '/html/body/div[1]/div/section/main/div/div[2]/div[2]/div[1]/div[4]/div[2]/table/tbody/tr[1]/td[6]/div/a'
        # 服务列表第一条数据操作禁用/启用文案
        self._first_service_ban_text_tag = '/html/body/div[1]/div/section/main/div/div[2]/div[2]/div[1]/div[4]/div[2]/table/tbody/tr[1]/td[6]/div/a/span'
        # 服务列表第一条数据操作禁用/启用确定按钮
        self._first_service_ban_commit_button_tag = '/html/body/div[2]/div/div[3]/button[2]'
        # 服务列表第二页按钮
        self._second_page_service_button_tag = '/html/body/div[1]/div/section/main/div/div[2]/div[2]/div[2]/div[2]/div/div/ul/li[2]'
        # 选择服务配置美国
        self._add_service_country_america_button_tag = '/html/body/div[1]/div/section/main/div/form/section/div[1]/div[2]/section[1]/div[2]/button[1]'
        # 选择服务配置澳大利亚
        self._add_service_country_australia_button_tag = '/html/body/div[1]/div/section/main/div/form/section/div[1]/div[2]/section[1]/div[2]/button[2]'
        # 选择一级服务类目规划
        self._add_service_first_plan_button_tag = '/html/body/div/div/section/main/div/form/section/div[1]/div[2]/section[2]/div/div[1]/div/div[2]/div[2]/div/div[1]/div[1]/div/i'
        # 选择一级服务类目文案
        self._add_service_first_category_text_tag = '/html/body/div/div/section/main/div/form/section/div[1]/div[2]/section[2]/div/div[1]/div/div[2]/div[2]/div/div[1]/div[1]/div/span'
        # 选择一级服务类目申请
        self._add_service_first_application_button_tag = '/html/body/div/div/section/main/div/form/section/div[1]/div[2]/section[2]/div/div[1]/div/div[2]/div[2]/div/div[3]/div[1]/div/i'
        # 选择一级服务类目定校
        self._add_service_first_school_button_tag = '/html/body/div/div/section/main/div/form/section/div[1]/div[2]/section[2]/div/div[1]/div/div[2]/div[2]/div/div[2]/div[1]/div/i'
        # 选择二级服务类目-规划-首席规划师
        self._add_service_second_plan_cplan_button_tag = '/html/body/div/div/section/main/div/form/section/div[1]/div[2]/section[2]/div/div[2]/div/div[2]/div[2]/div/div[1]/div[1]/div/i'
        # 选择二级服务类目-规划-资深规划师
        self._add_service_second_plan_splan_button_tag = '/html/body/div/div/section/main/div/form/section/div[1]/div[2]/section[2]/div/div[2]/div/div[2]/div[2]/div/div[2]/div[1]/div/i'
        # 选择二级服务类目-规划-普通规划师
        self._add_service_second_plan_nplan_button_tag = '/html/body/div/div/section/main/div/form/section/div[1]/div[2]/section[2]/div/div[2]/div/div[2]/div[2]/div/div[3]/div[1]/div/i]'
        # 选择三级服务类目-规划-首席规划师-时间与背景规划
        self._add_service_third_plan_cplan_time_button_tag = '/html/body/div/div/section/main/div/form/section/div[1]/div[2]/section[2]/div/div[3]/div/div[2]/div[2]/div/div[1]/div[1]/div/span[1]/span'
        # 选择三级服务类目-规划-首席规划师-申请指导
        self._add_service_third_plan_cplan_application_button_tag = '/html/body/div[1]/div/section/main/div/form/section/div[1]/div[2]/section[2]/div/div[3]/div/div[2]/div[2]/div/div[2]/div[1]/div/span[1]/label/span'
        # 选择三级服务类目-规划-首席规划师-选校方案
        self._add_service_third_plan_cplan_school_button_tag = '/html/body/div[1]/div/section/main/div/form/section/div[1]/div[2]/section[2]/div/div[3]/div/div[2]/div[2]/div/div[3]/div[1]/div/span[1]/label'
        # 选择三级服务类目-规划-首席规划师-入学准备指导
        self._add_service_third_plan_cplan_entrance_button_tag = '/html/body/div/div/section/main/div/form/section/div[1]/div[2]/section[2]/div/div[3]/div/div[2]/div[2]/div/div[4]/div[1]/div/span[1]/span'
        # 选择三级服务类目文案
        self._add_service_third_category_text_tag = '/html/body/div[1]/div/section/main/div/form/section/div[1]/div[2]/section[2]/div/div[3]/div/div[2]/div[2]/div/div[1]/div[1]/div/span[1]/span'
        # 选择三级服务类目价格文案
        self._add_service_third_category_price_text_tag = '/html/body/div[1]/div/section/main/div/form/section/div[1]/div[2]/section[2]/div/div[3]/div/div[2]/div[2]/div/div[1]/div[1]/div/span[2]'
        # 选校数量添加
        self._add_school_number_input_tag = '/html/body/div/div/section/main/div/form/section/div[2]/div[2]/div/div/div/div[3]/table/tbody/tr/td[4]/div/div/div/input'
        # 服务数量添加
        self._add_service_number_input_tag = '/html/body/div/div/section/main/div/form/section/div[2]/div[2]/div/div/div/div[3]/table/tbody/tr/td[5]/div/div/div/input'
        # 服务名称输入
        self._add_service_name_input_tag = '/html/body/div[1]/div/section/main/div/form/div[1]/div[2]/div[1]/div/div/div/div/input'
        # 添加服务提交审核按钮
        self._add_submit_button_tag = '/html/body/div[1]/div/section/main/div/form/div[2]/button'
        # 添加服务提交审核确定按钮
        self._add_submit_commit_button_tag = '/html/body/div[2]/div/div[3]/button[2]'
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
    def search_service_state_list_select(self):
        """
        属性: 搜索状态
        :return: 搜索状态
        """
        element = None
        try:
            element = self.project.get_element(self._search_service_state_list_select_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def search_service_state_all_button(self):
        """
        属性: 搜索状态全部
        :return: 搜索状态全部
        """
        element = None
        try:
            element = self.project.get_element(self._search_service_state_all_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def search_service_state_ban_button(self):
        """
        属性: 搜索状态禁用
        :return: 搜索状态禁用
        """
        element = None
        try:
            element = self.project.get_element(self._search_service_state_ban_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def search_service_state_use_button(self):
        """
        属性: 搜索状态启用
        :return: 搜索状态启用
        """
        element = None
        try:
            element = self.project.get_element(self._search_service_state_use_button_tag)
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
    def search_service_search_button(self):
        """
        属性: 搜索查询按钮
        :return: 搜索查询按钮
        """
        element = None
        try:
            element = self.project.get_element(self._search_service_search_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def clear_service_button(self):
        """
        属性: 清除按钮
        :return: 清除按钮
        """
        element = None
        try:
            element = self.project.get_element(self._clear_service_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def add_service_button(self):
        """
        属性: 组合服务按钮
        :return: 组合服务按钮
        """
        element = None
        try:
            element = self.project.get_element(self._add_service_button_tag)
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
    def first_service_ban_button(self):
        """
        属性: 服务列表第一条数据操作禁用/启用
        :return: 服务列表第一条数据操作禁用/启用
        """
        element = None
        try:
            element = self.project.get_element(self._first_service_ban_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def first_service_ban_text(self):
        """
        属性: 服务列表第一条数据操作禁用/启用文案
        :return: 服务列表第一条数据操作禁用/启用文案
        """
        element = None
        try:
            element = self.project.get_element(self._first_service_ban_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def first_service_ban_commit_button(self):
        """
        属性: 服务列表第一条数据操作禁用/启用确定按钮
        :return: 服务列表第一条数据操作禁用/启用确定按钮
        """
        element = None
        try:
            element = self.project.get_element(self._first_service_ban_commit_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def second_page_service_button(self):
        """
        属性: 服务列表第二页按钮
        :return: 服务列表第二页按钮
        """
        element = None
        try:
            element = self.project.get_element(self._second_page_service_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def add_service_country_america_button(self):
        """
        属性: 选择服务配置美国
        :return: 选择服务配置美国
        """
        element = None
        try:
            element = self.project.get_element(self._add_service_country_america_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def add_service_country_australia_button(self):
        """
        属性: 选择服务配置澳大利亚
        :return: 选择服务配置澳大利亚
        """
        element = None
        try:
            element = self.project.get_element(self._add_service_country_australia_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def add_service_first_plan_button(self):
        """
        属性: 选择一级服务类目规划
        :return: 选择一级服务类目规划
        """
        element = None
        try:
            element = self.project.get_element(self._add_service_first_plan_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def add_service_first_category_text(self):
        """
        属性: 选择一级服务类目文案
        :return: 选择一级服务类目文案
        """
        element = None
        try:
            element = self.project.get_element(self._add_service_first_category_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def add_service_first_application_button(self):
        """
        属性: 选择一级服务类目申请
        :return: 选择一级服务类目申请
        """
        element = None
        try:
            element = self.project.get_element(self._add_service_first_application_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def add_service_first_school_button(self):
        """
        属性: 选择一级服务类目定校
        :return: 选择一级服务类目定校
        """
        element = None
        try:
            element = self.project.get_element(self._add_service_first_school_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def add_service_second_plan_cplan_button(self):
        """
        属性: 选择二级服务类目-规划-首席规划师
        :return: 选择二级服务类目-规划-首席规划师
        """
        element = None
        try:
            element = self.project.get_element(self._add_service_second_plan_cplan_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def add_service_second_plan_splan_button(self):
        """
        属性: 选择二级服务类目-规划-资深规划师
        :return: 选择二级服务类目-规划-资深规划师
        """
        element = None
        try:
            element = self.project.get_element(self._add_service_second_plan_splan_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def add_service_second_plan_nplan_button(self):
        """
        属性: 选择二级服务类目-规划-普通规划师
        :return: 选择二级服务类目-规划-普通规划师
        """
        element = None
        try:
            element = self.project.get_element(self._add_service_second_plan_nplan_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def add_service_third_plan_cplan_time_button(self):
        """
        属性: 选择三级服务类目-规划-首席规划师-时间与背景规划
        :return: 选择三级服务类目-规划-首席规划师-时间与背景规划
        """
        element = None
        try:
            element = self.project.get_element(self._add_service_third_plan_cplan_time_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def add_service_third_plan_cplan_application_button(self):
        """
        属性: 选择三级服务类目-规划-首席规划师-申请指导
        :return: 选择三级服务类目-规划-首席规划师-申请指导
        """
        element = None
        try:
            element = self.project.get_element(self._add_service_third_plan_cplan_application_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def add_service_third_plan_cplan_school_button(self):
        """
        属性: 选择三级服务类目-规划-首席规划师-选校方案
        :return: 选择三级服务类目-规划-首席规划师-选校方案
        """
        element = None
        try:
            element = self.project.get_element(self._add_service_third_plan_cplan_school_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def add_service_third_plan_cplan_entrance_button(self):
        """
        属性: 选择三级服务类目-规划-首席规划师-入学准备指导
        :return: 选择三级服务类目-规划-首席规划师-入学准备指导
        """
        element = None
        try:
            element = self.project.get_element(self._add_service_third_plan_cplan_entrance_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def add_service_third_category_text(self):
        """
        属性: 选择三级服务类目文案
        :return: 选择三级服务类目文案
        """
        element = None
        try:
            element = self.project.get_element(self._add_service_third_category_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def add_service_third_category_price_text(self):
        """
        属性: 选择三级服务类目价格文案
        :return: 选择三级服务类目价格文案
        """
        element = None
        try:
            element = self.project.get_element(self._add_service_third_category_price_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def add_school_number_input(self):
        """
        属性: 选校数量添加
        :return: 选校数量添加
        """
        element = None
        try:
            element = self.project.get_element(self._add_school_number_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def add_service_number_input(self):
        """
        属性: 服务数量添加
        :return: 服务数量添加
        """
        element = None
        try:
            element = self.project.get_element(self._add_service_number_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def add_service_name_input(self):
        """
        属性: 服务名称输入
        :return: 服务名称输入
        """
        element = None
        try:
            element = self.project.get_element(self._add_service_name_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def add_submit_button(self):
        """
        属性: 添加服务提交审核按钮
        :return: 添加服务提交审核按钮
        """
        element = None
        try:
            element = self.project.get_element(self._add_submit_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def add_submit_commit_button(self):
        """
        属性: 添加服务提交审核确定按钮
        :return: 添加服务提交审核确定按钮
        """
        element = None
        try:
            element = self.project.get_element(self._add_submit_commit_button_tag)
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

    def get_select_search_service_state_list_action(self, search_service_state_list_select):
        """
        动作：获取搜索状态列表选中的文本
        :param search_service_state_list_select: 搜索状态列表索引或文本
        :return: '搜索状态'的文本
        """
        control_content = self.project.get_select_content(self.search_service_state_list_select, search_service_state_list_select)
        return control_content

    def select_search_service_state_list_action(self, search_service_state_list_select):
        """
        动作：选择搜索状态
        :param search_service_state_list_select: 搜索状态列表索引或文本
        :return: 选择'搜索状态'选择器后的页面
        """
        self.project.select_control(self.search_service_state_list_select, search_service_state_list_select)
        return self.project.get_current_page_source()

    def click_search_service_state_all_button_action(self):
        """
        动作：点击搜索状态全部
        :return: 点击'搜索状态全部'按钮后的页面
        """
        self.project.click(self.search_service_state_all_button)
        return self.project.get_current_page_source()

    def click_search_service_state_ban_button_action(self):
        """
        动作：点击搜索状态禁用
        :return: 点击'搜索状态禁用'按钮后的页面
        """
        self.project.click(self.search_service_state_ban_button)
        return self.project.get_current_page_source()

    def click_search_service_state_use_button_action(self):
        """
        动作：点击搜索状态启用
        :return: 点击'搜索状态启用'按钮后的页面
        """
        self.project.click(self.search_service_state_use_button)
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

    def click_search_service_search_button_action(self):
        """
        动作：点击搜索查询按钮
        :return: 点击'搜索查询按钮'按钮后的页面
        """
        self.project.click(self.search_service_search_button)
        return self.project.get_current_page_source()

    def click_clear_service_button_action(self):
        """
        动作：点击清除按钮
        :return: 点击'清除按钮'按钮后的页面
        """
        self.project.click(self.clear_service_button)
        return self.project.get_current_page_source()

    def click_add_service_button_action(self):
        """
        动作：点击组合服务按钮
        :return: 点击'组合服务按钮'按钮后的页面
        """
        self.project.click(self.add_service_button)
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

    def click_first_service_ban_button_action(self):
        """
        动作：点击服务列表第一条数据操作禁用/启用
        :return: 点击'服务列表第一条数据操作禁用/启用'按钮后的页面
        """
        self.project.click(self.first_service_ban_button)
        return self.project.get_current_page_source()

    def get_first_service_ban_text_action(self):
        """
        动作：获取服务列表第一条数据操作禁用/启用文案的文本
        :return: '服务列表第一条数据操作禁用/启用文案'的文本
        """
        control_content = self.project.get_element_text(self.first_service_ban_text)
        return control_content

    def click_first_service_ban_commit_button_action(self):
        """
        动作：点击服务列表第一条数据操作禁用/启用确定按钮
        :return: 点击'服务列表第一条数据操作禁用/启用确定按钮'按钮后的页面
        """
        self.project.click(self.first_service_ban_commit_button)
        return self.project.get_current_page_source()

    def click_second_page_service_button_action(self):
        """
        动作：点击服务列表第二页按钮
        :return: 点击'服务列表第二页按钮'按钮后的页面
        """
        self.project.click(self.second_page_service_button)
        return self.project.get_current_page_source()

    def click_add_service_country_america_button_action(self):
        """
        动作：点击选择服务配置美国
        :return: 点击'选择服务配置美国'按钮后的页面
        """
        self.project.click(self.add_service_country_america_button)
        return self.project.get_current_page_source()

    def click_add_service_country_australia_button_action(self):
        """
        动作：点击选择服务配置澳大利亚
        :return: 点击'选择服务配置澳大利亚'按钮后的页面
        """
        self.project.click(self.add_service_country_australia_button)
        return self.project.get_current_page_source()

    def click_add_service_first_plan_button_action(self):
        """
        动作：点击选择一级服务类目规划
        :return: 点击'选择一级服务类目规划'按钮后的页面
        """
        self.project.click(self.add_service_first_plan_button)
        return self.project.get_current_page_source()

    def get_add_service_first_category_text_action(self):
        """
        动作：获取选择一级服务类目文案的文本
        :return: '选择一级服务类目文案'的文本
        """
        control_content = self.project.get_element_text(self.add_service_first_category_text)
        return control_content

    def click_add_service_first_application_button_action(self):
        """
        动作：点击选择一级服务类目申请
        :return: 点击'选择一级服务类目申请'按钮后的页面
        """
        self.project.click(self.add_service_first_application_button)
        return self.project.get_current_page_source()

    def click_add_service_first_school_button_action(self):
        """
        动作：点击选择一级服务类目定校
        :return: 点击'选择一级服务类目定校'按钮后的页面
        """
        self.project.click(self.add_service_first_school_button)
        return self.project.get_current_page_source()

    def click_add_service_second_plan_cplan_button_action(self):
        """
        动作：点击选择二级服务类目-规划-首席规划师
        :return: 点击'选择二级服务类目-规划-首席规划师'按钮后的页面
        """
        self.project.click(self.add_service_second_plan_cplan_button)
        return self.project.get_current_page_source()

    def click_add_service_second_plan_splan_button_action(self):
        """
        动作：点击选择二级服务类目-规划-资深规划师
        :return: 点击'选择二级服务类目-规划-资深规划师'按钮后的页面
        """
        self.project.click(self.add_service_second_plan_splan_button)
        return self.project.get_current_page_source()

    def click_add_service_second_plan_nplan_button_action(self):
        """
        动作：点击选择二级服务类目-规划-普通规划师
        :return: 点击'选择二级服务类目-规划-普通规划师'按钮后的页面
        """
        self.project.click(self.add_service_second_plan_nplan_button)
        return self.project.get_current_page_source()

    def click_add_service_third_plan_cplan_time_button_action(self):
        """
        动作：点击选择三级服务类目-规划-首席规划师-时间与背景规划
        :return: 点击'选择三级服务类目-规划-首席规划师-时间与背景规划'按钮后的页面
        """
        self.project.click(self.add_service_third_plan_cplan_time_button)
        return self.project.get_current_page_source()

    def click_add_service_third_plan_cplan_application_button_action(self):
        """
        动作：点击选择三级服务类目-规划-首席规划师-申请指导
        :return: 点击'选择三级服务类目-规划-首席规划师-申请指导'按钮后的页面
        """
        self.project.click(self.add_service_third_plan_cplan_application_button)
        return self.project.get_current_page_source()

    def click_add_service_third_plan_cplan_school_button_action(self):
        """
        动作：点击选择三级服务类目-规划-首席规划师-选校方案
        :return: 点击'选择三级服务类目-规划-首席规划师-选校方案'按钮后的页面
        """
        self.project.click(self.add_service_third_plan_cplan_school_button)
        return self.project.get_current_page_source()

    def click_add_service_third_plan_cplan_entrance_button_action(self):
        """
        动作：点击选择三级服务类目-规划-首席规划师-入学准备指导
        :return: 点击'选择三级服务类目-规划-首席规划师-入学准备指导'按钮后的页面
        """
        self.project.click(self.add_service_third_plan_cplan_entrance_button)
        return self.project.get_current_page_source()

    def get_add_service_third_category_text_action(self):
        """
        动作：获取选择三级服务类目文案的文本
        :return: '选择三级服务类目文案'的文本
        """
        control_content = self.project.get_element_text(self.add_service_third_category_text)
        return control_content

    def get_add_service_third_category_price_text_action(self):
        """
        动作：获取选择三级服务类目价格文案的文本
        :return: '选择三级服务类目价格文案'的文本
        """
        control_content = self.project.get_element_text(self.add_service_third_category_price_text)
        return control_content

    def set_add_school_number_input_action(self, add_school_number_input):
        """
        动作：设置选校数量添加
        :param add_school_number_input: 选校数量添加
        :return: 设置'选校数量添加'文本后的页面
        """
        self.project.clear_and_send_keys(self.add_school_number_input, add_school_number_input)
        return self.project.get_current_page_source()

    def set_add_service_number_input_action(self, add_service_number_input):
        """
        动作：设置服务数量添加
        :param add_service_number_input: 服务数量添加
        :return: 设置'服务数量添加'文本后的页面
        """
        self.project.clear_and_send_keys(self.add_service_number_input, add_service_number_input)
        return self.project.get_current_page_source()

    def set_add_service_name_input_action(self, add_service_name_input):
        """
        动作：设置服务名称输入
        :param add_service_name_input: 服务名称输入
        :return: 设置'服务名称输入'文本后的页面
        """
        self.project.clear_and_send_keys(self.add_service_name_input, add_service_name_input)
        return self.project.get_current_page_source()

    def click_add_submit_button_action(self):
        """
        动作：点击添加服务提交审核按钮
        :return: 点击'添加服务提交审核按钮'按钮后的页面
        """
        self.project.click(self.add_submit_button)
        return self.project.get_current_page_source()

    def click_add_submit_commit_button_action(self):
        """
        动作：点击添加服务提交审核确定按钮
        :return: 点击'添加服务提交审核确定按钮'按钮后的页面
        """
        self.project.click(self.add_submit_commit_button)
        return self.project.get_current_page_source()

    # endregion Actions
