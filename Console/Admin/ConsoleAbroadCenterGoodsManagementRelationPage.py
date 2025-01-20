from Utils.Log import log


"""
后台-商品管理-关联商品
console_url/abroad_center/goods_audit
"""


class ConsoleAbroadCenterGoodsManagementRelationPage:
    def __init__(self, project):
        self.project = project
        self.url = 'console_url/abroad_center/goods_management/relation/PR020100039353'
        # region Fields
        # 消息提示
        self._message_content_text_tag = '/html/body/div[last()]/div/div[1]/p'
        # 关联商品按钮
        self._abroad_goods_relation_button_tag = '/html/body/div/div/section/main/div/button'
        # 关联商品编码搜索
        self._search_goods_relation_product_code_input_tag = '/html/body/div[1]/div/section/main/div/div[3]/div/div/div[2]/div[1]/form/div/div[1]/div/div/input'
        # 关联商品名字搜索
        self._search_goods_relation_product_name_input_tag = '/html/body/div[1]/div/section/main/div/div[3]/div/div/div[2]/div[1]/form/div/div[2]/div/div/input'
        # 关联商品查询
        self._search_goods_relation_search_button_tag = '/html/body/div[1]/div/section/main/div/div[3]/div/div/div[2]/div[1]/form/div/div[5]/div/button'
        # 关联商品清除
        self._relation_clear_goods_relation_button_tag = '/html/body/div[1]/div/section/main/div/div[3]/div/div/div[2]/div[1]/form/div/div[6]/div/button'
        # 关联列表第一条数据的选择框
        self._relation_first_relation_product_button_tag = '/html/body/div[1]/div/section/main/div/div[3]/div/div/div[2]/div[2]/div[1]/div[3]/table/tbody/tr/td[1]/div/label/span/span'
        # 关联列表第一条数据的商品编码
        self._relation_first_relation_product_code_text_tag = '/html/body/div[1]/div/section/main/div/div[3]/div/div/div[2]/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[2]/div'
        # 关联列表第一条数据的商品名称
        self._relation_first_relation_product_name_text_tag = '/html/body/div[1]/div/section/main/div/div[3]/div/div/div[2]/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[3]/div/a/span'
        # 关联列表第一条数据的商品名称按钮
        self._relation_first_relation_product_name_button_tag = '/html/body/div[1]/div/section/main/div/div[3]/div/div/div[2]/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[3]/div/a'
        # 关联列表第一条数据的服务名称按钮
        self._relation_first_relation_service_name_text_tag = '/html/body/div[1]/div/section/main/div/div[3]/div/div/div[2]/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[4]/div'
        # 关联列表第一条数据的所属国家及地区
        self._relation_first_relation_country_text_tag = '/html/body/div[1]/div/section/main/div/div[3]/div/div/div[2]/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[5]/div'
        # 关联列表第一条数据的商品价格
        self._relation_first_relation_price_text_tag = '/html/body/div[1]/div/section/main/div/div[3]/div/div/div[2]/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[6]/div'
        # 关联商品确定
        self._relation_commit_goods_relation_button_tag = '/html/body/div[1]/div/section/main/div/div[3]/div/div/div[3]/span/button[2]'
        # 列表第一条数据的商品编码
        self._first_relation_product_code_text_tag = '/html/body/div[1]/div/section/main/div/div[2]/div/div[3]/table/tbody/tr[1]/td[1]/div'
        # 列表第一条数据的商品名称
        self._first_relation_product_name_text_tag = '/html/body/div[1]/div/section/main/div/div[2]/div/div[3]/table/tbody/tr[1]/td[2]/div/a/span'
        # 列表第一条数据的商品名称按钮
        self._first_relation_product_name_button_tag = '/html/body/div[1]/div/section/main/div/div[2]/div/div[3]/table/tbody/tr[1]/td[2]/div/a'
        # 列表第一条数据的服务名称按钮
        self._first_relation_service_name_text_tag = '/html/body/div[1]/div/section/main/div/div[2]/div/div[3]/table/tbody/tr[1]/td[3]/div'
        # 列表第一条数据的所属国家及地区
        self._first_relation_country_text_tag = '/html/body/div[1]/div/section/main/div/div[2]/div/div[3]/table/tbody/tr[1]/td[4]/div'
        # 列表第一条数据的商品价格
        self._first_relation_price_text_tag = '/html/body/div[1]/div/section/main/div/div[2]/div/div[3]/table/tbody/tr[1]/td[5]/div'
        # 列表第一条数据的上架状态
        self._first_relation_upper_text_tag = '/html/body/div[1]/div/section/main/div/div[2]/div/div[3]/table/tbody/tr[1]/td[6]/div'
        # 列表第一条数据的展示状态
        self._first_relation_display_text_tag = '/html/body/div[1]/div/section/main/div/div[2]/div/div[3]/table/tbody/tr[1]/td[7]/div'
        # 列表第一条数据的关联状态
        self._first_relation_state_text_tag = '/html/body/div[1]/div/section/main/div/div[2]/div/div[3]/table/tbody/tr[1]/td[8]/div'
        # 列表第一条数据的操作文案
        self._first_relation_option_text_tag = '/html/body/div[1]/div/section/main/div/div[2]/div/div[4]/div[2]/table/tbody/tr[1]/td[9]/div/a/span'
        # 列表第一条数据的操作
        self._first_relation_option_button_tag = '/html/body/div[1]/div/section/main/div/div[2]/div/div[4]/div[2]/table/tbody/tr[1]/td[9]/div/a'
        # 列表第一条数据的取消关联确认
        self._first_relation_option_commit_button_tag = '/html/body/div[2]/div/div[3]/button[2]'
        # 列表无数据文本
        self._first_relation_no_data_text_tag = '/html/body/div[1]/div/section/main/div/div[2]/div/div[3]/div/span/label'
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
    def abroad_goods_relation_button(self):
        """
        属性: 关联商品按钮
        :return: 关联商品按钮
        """
        element = None
        try:
            element = self.project.get_element(self._abroad_goods_relation_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def search_goods_relation_product_code_input(self):
        """
        属性: 关联商品编码搜索
        :return: 关联商品编码搜索
        """
        element = None
        try:
            element = self.project.get_element(self._search_goods_relation_product_code_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def search_goods_relation_product_name_input(self):
        """
        属性: 关联商品名字搜索
        :return: 关联商品名字搜索
        """
        element = None
        try:
            element = self.project.get_element(self._search_goods_relation_product_name_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def search_goods_relation_search_button(self):
        """
        属性: 关联商品查询
        :return: 关联商品查询
        """
        element = None
        try:
            element = self.project.get_element(self._search_goods_relation_search_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def relation_clear_goods_relation_button(self):
        """
        属性: 关联商品清除
        :return: 关联商品清除
        """
        element = None
        try:
            element = self.project.get_element(self._relation_clear_goods_relation_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def relation_first_relation_product_button(self):
        """
        属性: 关联列表第一条数据的选择框
        :return: 关联列表第一条数据的选择框
        """
        element = None
        try:
            element = self.project.get_element(self._relation_first_relation_product_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def relation_first_relation_product_code_text(self):
        """
        属性: 关联列表第一条数据的商品编码
        :return: 关联列表第一条数据的商品编码
        """
        element = None
        try:
            element = self.project.get_element(self._relation_first_relation_product_code_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def relation_first_relation_product_name_text(self):
        """
        属性: 关联列表第一条数据的商品名称
        :return: 关联列表第一条数据的商品名称
        """
        element = None
        try:
            element = self.project.get_element(self._relation_first_relation_product_name_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def relation_first_relation_product_name_button(self):
        """
        属性: 关联列表第一条数据的商品名称按钮
        :return: 关联列表第一条数据的商品名称按钮
        """
        element = None
        try:
            element = self.project.get_element(self._relation_first_relation_product_name_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def relation_first_relation_service_name_text(self):
        """
        属性: 关联列表第一条数据的服务名称按钮
        :return: 关联列表第一条数据的服务名称按钮
        """
        element = None
        try:
            element = self.project.get_element(self._relation_first_relation_service_name_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def relation_first_relation_country_text(self):
        """
        属性: 关联列表第一条数据的所属国家及地区
        :return: 关联列表第一条数据的所属国家及地区
        """
        element = None
        try:
            element = self.project.get_element(self._relation_first_relation_country_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def relation_first_relation_price_text(self):
        """
        属性: 关联列表第一条数据的商品价格
        :return: 关联列表第一条数据的商品价格
        """
        element = None
        try:
            element = self.project.get_element(self._relation_first_relation_price_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def relation_commit_goods_relation_button(self):
        """
        属性: 关联商品确定
        :return: 关联商品确定
        """
        element = None
        try:
            element = self.project.get_element(self._relation_commit_goods_relation_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def first_relation_product_code_text(self):
        """
        属性: 列表第一条数据的商品编码
        :return: 列表第一条数据的商品编码
        """
        element = None
        try:
            element = self.project.get_element(self._first_relation_product_code_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def first_relation_product_name_text(self):
        """
        属性: 列表第一条数据的商品名称
        :return: 列表第一条数据的商品名称
        """
        element = None
        try:
            element = self.project.get_element(self._first_relation_product_name_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def first_relation_product_name_button(self):
        """
        属性: 列表第一条数据的商品名称按钮
        :return: 列表第一条数据的商品名称按钮
        """
        element = None
        try:
            element = self.project.get_element(self._first_relation_product_name_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def first_relation_service_name_text(self):
        """
        属性: 列表第一条数据的服务名称按钮
        :return: 列表第一条数据的服务名称按钮
        """
        element = None
        try:
            element = self.project.get_element(self._first_relation_service_name_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def first_relation_country_text(self):
        """
        属性: 列表第一条数据的所属国家及地区
        :return: 列表第一条数据的所属国家及地区
        """
        element = None
        try:
            element = self.project.get_element(self._first_relation_country_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def first_relation_price_text(self):
        """
        属性: 列表第一条数据的商品价格
        :return: 列表第一条数据的商品价格
        """
        element = None
        try:
            element = self.project.get_element(self._first_relation_price_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def first_relation_upper_text(self):
        """
        属性: 列表第一条数据的上架状态
        :return: 列表第一条数据的上架状态
        """
        element = None
        try:
            element = self.project.get_element(self._first_relation_upper_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def first_relation_display_text(self):
        """
        属性: 列表第一条数据的展示状态
        :return: 列表第一条数据的展示状态
        """
        element = None
        try:
            element = self.project.get_element(self._first_relation_display_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def first_relation_state_text(self):
        """
        属性: 列表第一条数据的关联状态
        :return: 列表第一条数据的关联状态
        """
        element = None
        try:
            element = self.project.get_element(self._first_relation_state_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def first_relation_option_text(self):
        """
        属性: 列表第一条数据的操作文案
        :return: 列表第一条数据的操作文案
        """
        element = None
        try:
            element = self.project.get_element(self._first_relation_option_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def first_relation_option_button(self):
        """
        属性: 列表第一条数据的操作
        :return: 列表第一条数据的操作
        """
        element = None
        try:
            element = self.project.get_element(self._first_relation_option_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def first_relation_option_commit_button(self):
        """
        属性: 列表第一条数据的取消关联确认
        :return: 列表第一条数据的取消关联确认
        """
        element = None
        try:
            element = self.project.get_element(self._first_relation_option_commit_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def first_relation_no_data_text(self):
        """
        属性: 列表无数据文本
        :return: 列表无数据文本
        """
        element = None
        try:
            element = self.project.get_element(self._first_relation_no_data_text_tag)
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

    def click_abroad_goods_relation_button_action(self):
        """
        动作：点击关联商品按钮
        :return: 点击'关联商品按钮'按钮后的页面
        """
        self.project.click(self.abroad_goods_relation_button)
        return self.project.get_current_page_source()

    def set_search_goods_relation_product_code_input_action(self, search_goods_relation_product_code_input):
        """
        动作：设置关联商品编码搜索
        :param search_goods_relation_product_code_input: 关联商品编码搜索
        :return: 设置'关联商品编码搜索'文本后的页面
        """
        self.project.clear_and_send_keys(self.search_goods_relation_product_code_input, search_goods_relation_product_code_input)
        return self.project.get_current_page_source()

    def set_search_goods_relation_product_name_input_action(self, search_goods_relation_product_name_input):
        """
        动作：设置关联商品名字搜索
        :param search_goods_relation_product_name_input: 关联商品名字搜索
        :return: 设置'关联商品名字搜索'文本后的页面
        """
        self.project.clear_and_send_keys(self.search_goods_relation_product_name_input, search_goods_relation_product_name_input)
        return self.project.get_current_page_source()

    def click_search_goods_relation_search_button_action(self):
        """
        动作：点击关联商品查询
        :return: 点击'关联商品查询'按钮后的页面
        """
        self.project.click(self.search_goods_relation_search_button)
        return self.project.get_current_page_source()

    def click_relation_clear_goods_relation_button_action(self):
        """
        动作：点击关联商品清除
        :return: 点击'关联商品清除'按钮后的页面
        """
        self.project.click(self.relation_clear_goods_relation_button)
        return self.project.get_current_page_source()

    def click_relation_first_relation_product_button_action(self):
        """
        动作：点击关联列表第一条数据的选择框
        :return: 点击'关联列表第一条数据的选择框'按钮后的页面
        """
        self.project.click(self.relation_first_relation_product_button)
        return self.project.get_current_page_source()

    def get_relation_first_relation_product_code_text_action(self):
        """
        动作：获取关联列表第一条数据的商品编码的文本
        :return: '关联列表第一条数据的商品编码'的文本
        """
        control_content = self.project.get_element_text(self.relation_first_relation_product_code_text)
        return control_content

    def get_relation_first_relation_product_name_text_action(self):
        """
        动作：获取关联列表第一条数据的商品名称的文本
        :return: '关联列表第一条数据的商品名称'的文本
        """
        control_content = self.project.get_element_text(self.relation_first_relation_product_name_text)
        return control_content

    def click_relation_first_relation_product_name_button_action(self):
        """
        动作：点击关联列表第一条数据的商品名称按钮
        :return: 点击'关联列表第一条数据的商品名称按钮'按钮后的页面
        """
        self.project.click(self.relation_first_relation_product_name_button)
        return self.project.get_current_page_source()

    def get_relation_first_relation_service_name_text_action(self):
        """
        动作：获取关联列表第一条数据的服务名称按钮的文本
        :return: '关联列表第一条数据的服务名称按钮'的文本
        """
        control_content = self.project.get_element_text(self.relation_first_relation_service_name_text)
        return control_content

    def get_relation_first_relation_country_text_action(self):
        """
        动作：获取关联列表第一条数据的所属国家及地区的文本
        :return: '关联列表第一条数据的所属国家及地区'的文本
        """
        control_content = self.project.get_element_text(self.relation_first_relation_country_text)
        return control_content

    def get_relation_first_relation_price_text_action(self):
        """
        动作：获取关联列表第一条数据的商品价格的文本
        :return: '关联列表第一条数据的商品价格'的文本
        """
        control_content = self.project.get_element_text(self.relation_first_relation_price_text)
        return control_content

    def click_relation_commit_goods_relation_button_action(self):
        """
        动作：点击关联商品确定
        :return: 点击'关联商品确定'按钮后的页面
        """
        self.project.click(self.relation_commit_goods_relation_button)
        return self.project.get_current_page_source()

    def get_first_relation_product_code_text_action(self):
        """
        动作：获取列表第一条数据的商品编码的文本
        :return: '列表第一条数据的商品编码'的文本
        """
        control_content = self.project.get_element_text(self.first_relation_product_code_text)
        return control_content

    def get_first_relation_product_name_text_action(self):
        """
        动作：获取列表第一条数据的商品名称的文本
        :return: '列表第一条数据的商品名称'的文本
        """
        control_content = self.project.get_element_text(self.first_relation_product_name_text)
        return control_content

    def click_first_relation_product_name_button_action(self):
        """
        动作：点击列表第一条数据的商品名称按钮
        :return: 点击'列表第一条数据的商品名称按钮'按钮后的页面
        """
        self.project.click(self.first_relation_product_name_button)
        return self.project.get_current_page_source()

    def get_first_relation_service_name_text_action(self):
        """
        动作：获取列表第一条数据的服务名称按钮的文本
        :return: '列表第一条数据的服务名称按钮'的文本
        """
        control_content = self.project.get_element_text(self.first_relation_service_name_text)
        return control_content

    def get_first_relation_country_text_action(self):
        """
        动作：获取列表第一条数据的所属国家及地区的文本
        :return: '列表第一条数据的所属国家及地区'的文本
        """
        control_content = self.project.get_element_text(self.first_relation_country_text)
        return control_content

    def get_first_relation_price_text_action(self):
        """
        动作：获取列表第一条数据的商品价格的文本
        :return: '列表第一条数据的商品价格'的文本
        """
        control_content = self.project.get_element_text(self.first_relation_price_text)
        return control_content

    def get_first_relation_upper_text_action(self):
        """
        动作：获取列表第一条数据的上架状态的文本
        :return: '列表第一条数据的上架状态'的文本
        """
        control_content = self.project.get_element_text(self.first_relation_upper_text)
        return control_content

    def get_first_relation_display_text_action(self):
        """
        动作：获取列表第一条数据的展示状态的文本
        :return: '列表第一条数据的展示状态'的文本
        """
        control_content = self.project.get_element_text(self.first_relation_display_text)
        return control_content

    def get_first_relation_state_text_action(self):
        """
        动作：获取列表第一条数据的关联状态的文本
        :return: '列表第一条数据的关联状态'的文本
        """
        control_content = self.project.get_element_text(self.first_relation_state_text)
        return control_content

    def get_first_relation_option_text_action(self):
        """
        动作：获取列表第一条数据的操作文案的文本
        :return: '列表第一条数据的操作文案'的文本
        """
        control_content = self.project.get_element_text(self.first_relation_option_text)
        return control_content

    def click_first_relation_option_button_action(self):
        """
        动作：点击列表第一条数据的操作
        :return: 点击'列表第一条数据的操作'按钮后的页面
        """
        self.project.click(self.first_relation_option_button)
        return self.project.get_current_page_source()

    def click_first_relation_option_commit_button_action(self):
        """
        动作：点击列表第一条数据的取消关联确认
        :return: 点击'列表第一条数据的取消关联确认'按钮后的页面
        """
        self.project.click(self.first_relation_option_commit_button)
        return self.project.get_current_page_source()

    def get_first_relation_no_data_text_action(self):
        """
        动作：获取列表无数据文本的文本
        :return: '列表无数据文本'的文本
        """
        control_content = self.project.get_element_text(self.first_relation_no_data_text)
        return control_content

    # endregion Actions
