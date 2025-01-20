from Utils.Log import log

"""
学长管家后台意见反馈管理
wpc_url/advice-feedback-manage/advice-feedback
"""


class AdviceFeedbackManageAdviceFeedbackPage:
    def __init__(self, project):
        self.project = project
        self.url = 'wpc_url/advice-feedback-manage/advice-feedback'
        # region Fields
        # 消息提示信息
        self._message_content_text_tag = '/html/body/div[last()]/div/div[last()-1]/p'
        # 搜索意见编号
        self._search_feedback_id_input_tag = '/html/body/div/div/div[2]/section/div/div/div[1]/div[1]/form/div/div[1]/div/div/input'
        # 意见类型
        self._search_feedback_type_button_tag = '/html/body/div[1]/div/div[2]/section/div/div/div[1]/div[1]/form/div/div[2]/div/div/div/input'
        # 下拉框
        self._drop_down_list_select_tag = '/html/body/div[2]/div[1]/div[1]/ul'
        # 搜索状态按钮
        self._search_status_button_tag = '/html/body/div[1]/div/div[2]/section/div/div/div[1]/div[1]/form/div/div[3]/div/div/div[1]/input'
        # 搜索提出人
        self._search_feedback_person_input_tag = '/html/body/div[1]/div/div[2]/section/div/div/div[1]/div[1]/form/div/div[4]/div/div/input'
        # 处理人
        self._search_deal_person_input_tag = '/html/body/div[1]/div/div[2]/section/div/div/div[1]/div[1]/form/div/div[5]/div/div/input'
        # 查询按钮
        self._search_button_tag = '/html/body/div[1]/div/div[2]/section/div/div/div[1]/div[1]/form/div/div[8]/div/button'
        # 重置按钮
        self._search_clear_button_tag = '/html/body/div[1]/div/div[2]/section/div/div/div[1]/div[1]/form/div/div[9]/div/button'
        # 列表第一条数据意见编号
        self._first_advice_id_text_tag = '/html/body/div[1]/div/div[2]/section/div/div/div[2]/div[2]/div[3]/table/tbody/tr[1]/td[1]/div/a/span'
        # 列表第一条数据意见按钮
        self._first_advice_id_button_tag = '/html/body/div[1]/div/div[2]/section/div/div/div[2]/div[2]/div[3]/table/tbody/tr[1]/td[1]/div/a/span'
        # 列表第一条数据意见类型
        self._first_advice_type_text_tag = '/html/body/div[1]/div/div[2]/section/div/div/div[2]/div[2]/div[3]/table/tbody/tr[1]/td[1]/div/a/span'
        # 列表第一条数据提出人
        self._first_advice_person_text_tag = '/html/body/div[1]/div/div[2]/section/div/div/div[2]/div[2]/div[3]/table/tbody/tr[1]/td[3]/div/span'
        # 列表第一条数据意见描述
        self._first_advice_description_text_tag = '/html/body/div[1]/div/div[2]/section/div/div/div[2]/div[2]/div[3]/table/tbody/tr[1]/td[4]/div/span'
        # 列表第一条数据提交时间
        self._first_advice_commit_time_text_tag = '/html/body/div[1]/div/div[2]/section/div/div/div[2]/div[2]/div[3]/table/tbody/tr[1]/td[5]/div/span'
        # 列表第一条数据处理时间
        self._first_advice_deal_time_text_tag = '/html/body/div[1]/div/div[2]/section/div/div/div[2]/div[2]/div[3]/table/tbody/tr[1]/td[6]/div/span'
        # 列表第一条数据处理人
        self._first_advice_deal_person_text_tag = '//*[@id="app"]/div/div[2]/section/div/div/div[2]/div[2]/div[3]/table/tbody/tr/td[7]/div/span'
        # 列表第一条数据处理结果
        self._first_advice_deal_result_text_tag = '//*[@id="app"]/div/div[2]/section/div/div/div[2]/div[2]/div[3]/table/tbody/tr/td[8]/div/span'
        # 列表第一条数据状态
        self._first_advice_deal_stauts_text_tag = '//*[@id="app"]/div/div[2]/section/div/div/div[2]/div[2]/div[3]/table/tbody/tr/td[9]/div/span'
        # 列表第一条数据操作
        self._first_advice_option_button_tag = '/html/body/div/div/div[2]/section/div/div/div[2]/div[2]/div[4]/div[2]/table/tbody/tr/td[10]/div/button'
        # 列表第一条数据操作文案
        self._first_advice_option_text_tag = '/html/body/div/div/div[2]/section/div/div/div[2]/div[2]/div[4]/div[2]/table/tbody/tr/td[10]/div/button/span'
        # 列表第一条数据处理结果填写
        self._first_advice_deal_result_input_tag = '/html/body/div[1]/div/div[2]/section/div/div/div[3]/div/div/div[2]/form/div[5]/div/div/div/div[1]/textarea'
        # 列表第一条数据处理结果确定按钮
        self._first_advice_deal_result_commit_button_tag = '/html/body/div[1]/div/div[2]/section/div/div/div[3]/div/div/div[3]/span/button[2]'



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
    def search_feedback_id_input(self):
        """
        属性: 搜索意见编号
        :return: 搜索意见编号
        """
        element = None
        try:
            element = self.project.get_element(self._search_feedback_id_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def search_feedback_type_button(self):
        """
        属性: 意见类型
        :return: 意见类型
        """
        element = None
        try:
            element = self.project.get_element(self._search_feedback_type_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def drop_down_list_select(self):
        """
        属性: 下拉框
        :return: 下拉框
        """
        element = None
        try:
            element = self.project.get_element(self._drop_down_list_select_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def search_status_button(self):
        """
        属性: 搜索状态按钮
        :return: 搜索状态按钮
        """
        element = None
        try:
            element = self.project.get_element(self._search_status_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def search_feedback_person_input(self):
        """
        属性: 搜索提出人
        :return: 搜索提出人
        """
        element = None
        try:
            element = self.project.get_element(self._search_feedback_person_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def search_deal_person_input(self):
        """
        属性: 处理人
        :return: 处理人
        """
        element = None
        try:
            element = self.project.get_element(self._search_deal_person_input_tag)
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
    def search_clear_button(self):
        """
        属性: 重置按钮
        :return: 重置按钮
        """
        element = None
        try:
            element = self.project.get_element(self._search_clear_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def first_advice_id_text(self):
        """
        属性: 列表第一条数据意见编号
        :return: 列表第一条数据意见编号
        """
        element = None
        try:
            element = self.project.get_element(self._first_advice_id_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def first_advice_id_button(self):
        """
        属性: 列表第一条数据意见按钮
        :return: 列表第一条数据意见按钮
        """
        element = None
        try:
            element = self.project.get_element(self._first_advice_id_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def first_advice_type_text(self):
        """
        属性: 列表第一条数据意见类型
        :return: 列表第一条数据意见类型
        """
        element = None
        try:
            element = self.project.get_element(self._first_advice_type_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def first_advice_person_text(self):
        """
        属性: 列表第一条数据提出人
        :return: 列表第一条数据提出人
        """
        element = None
        try:
            element = self.project.get_element(self._first_advice_person_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def first_advice_description_text(self):
        """
        属性: 列表第一条数据意见描述
        :return: 列表第一条数据意见描述
        """
        element = None
        try:
            element = self.project.get_element(self._first_advice_description_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def first_advice_commit_time_text(self):
        """
        属性: 列表第一条数据提交时间
        :return: 列表第一条数据提交时间
        """
        element = None
        try:
            element = self.project.get_element(self._first_advice_commit_time_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def first_advice_deal_time_text(self):
        """
        属性: 列表第一条数据处理时间
        :return: 列表第一条数据处理时间
        """
        element = None
        try:
            element = self.project.get_element(self._first_advice_deal_time_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def first_advice_deal_person_text(self):
        """
        属性: 列表第一条数据处理人
        :return: 列表第一条数据处理人
        """
        element = None
        try:
            element = self.project.get_element(self._first_advice_deal_person_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def first_advice_deal_result_text(self):
        """
        属性: 列表第一条数据处理结果
        :return: 列表第一条数据处理结果
        """
        element = None
        try:
            element = self.project.get_element(self._first_advice_deal_result_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def first_advice_deal_stauts_text(self):
        """
        属性: 列表第一条数据状态
        :return: 列表第一条数据状态
        """
        element = None
        try:
            element = self.project.get_element(self._first_advice_deal_stauts_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def first_advice_option_button(self):
        """
        属性: 列表第一条数据操作
        :return: 列表第一条数据操作
        """
        element = None
        try:
            element = self.project.get_element(self._first_advice_option_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def first_advice_option_text(self):
        """
        属性: 列表第一条数据操作文案
        :return: 列表第一条数据操作文案
        """
        element = None
        try:
            element = self.project.get_element(self._first_advice_option_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def first_advice_deal_result_input(self):
        """
        属性: 列表第一条数据处理结果填写
        :return: 列表第一条数据处理结果填写
        """
        element = None
        try:
            element = self.project.get_element(self._first_advice_deal_result_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def first_advice_deal_result_commit_button(self):
        """
        属性: 列表第一条数据处理结果确定按钮
        :return: 列表第一条数据处理结果确定按钮
        """
        element = None
        try:
            element = self.project.get_element(self._first_advice_deal_result_commit_button_tag)
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

    def set_search_feedback_id_input_action(self, search_feedback_id_input):
        """
        动作：设置搜索意见编号
        :param search_feedback_id_input: 搜索意见编号
        :return: 设置'搜索意见编号'文本后的页面
        """
        self.project.clear_and_send_keys(self.search_feedback_id_input, search_feedback_id_input)
        return self.project.get_current_page_source()

    def click_search_feedback_type_button_action(self):
        """
        动作：点击意见类型
        :return: 点击'意见类型'按钮后的页面
        """
        self.project.click(self.search_feedback_type_button)
        return self.project.get_current_page_source()

    def get_select_drop_down_list_action(self, drop_down_list_select):
        """
        动作：获取下拉框列表选中的文本
        :param drop_down_list_select: 下拉框列表索引或文本
        :return: '下拉框'的文本
        """
        control_content = self.project.get_select_content(self.drop_down_list_select, drop_down_list_select)
        return control_content

    def select_drop_down_list_action(self, drop_down_list_select):
        """
        动作：选择下拉框
        :param drop_down_list_select: 下拉框列表索引或文本
        :return: 选择'下拉框'选择器后的页面
        """
        self.project.select_control(self.drop_down_list_select, drop_down_list_select)
        return self.project.get_current_page_source()

    def click_search_status_button_action(self):
        """
        动作：点击搜索状态按钮
        :return: 点击'搜索状态按钮'按钮后的页面
        """
        self.project.click(self.search_status_button)
        return self.project.get_current_page_source()

    def set_search_feedback_person_input_action(self, search_feedback_person_input):
        """
        动作：设置搜索提出人
        :param search_feedback_person_input: 搜索提出人
        :return: 设置'搜索提出人'文本后的页面
        """
        self.project.clear_and_send_keys(self.search_feedback_person_input, search_feedback_person_input)
        return self.project.get_current_page_source()

    def set_search_deal_person_input_action(self, search_deal_person_input):
        """
        动作：设置处理人
        :param search_deal_person_input: 处理人
        :return: 设置'处理人'文本后的页面
        """
        self.project.clear_and_send_keys(self.search_deal_person_input, search_deal_person_input)
        return self.project.get_current_page_source()

    def click_search_button_action(self):
        """
        动作：点击查询按钮
        :return: 点击'查询按钮'按钮后的页面
        """
        self.project.click(self.search_button)
        return self.project.get_current_page_source()

    def click_search_clear_button_action(self):
        """
        动作：点击重置按钮
        :return: 点击'重置按钮'按钮后的页面
        """
        self.project.click(self.search_clear_button)
        return self.project.get_current_page_source()

    def get_first_advice_id_text_action(self):
        """
        动作：获取列表第一条数据意见编号的文本
        :return: '列表第一条数据意见编号'的文本
        """
        control_content = self.project.get_element_text(self.first_advice_id_text)
        return control_content

    def click_first_advice_id_button_action(self):
        """
        动作：点击列表第一条数据意见按钮
        :return: 点击'列表第一条数据意见按钮'按钮后的页面
        """
        self.project.click(self.first_advice_id_button)
        return self.project.get_current_page_source()

    def get_first_advice_type_text_action(self):
        """
        动作：获取列表第一条数据意见类型的文本
        :return: '列表第一条数据意见类型'的文本
        """
        control_content = self.project.get_element_text(self.first_advice_type_text)
        return control_content

    def get_first_advice_person_text_action(self):
        """
        动作：获取列表第一条数据提出人的文本
        :return: '列表第一条数据提出人'的文本
        """
        control_content = self.project.get_element_text(self.first_advice_person_text)
        return control_content

    def get_first_advice_description_text_action(self):
        """
        动作：获取列表第一条数据意见描述的文本
        :return: '列表第一条数据意见描述'的文本
        """
        control_content = self.project.get_element_text(self.first_advice_description_text)
        return control_content

    def get_first_advice_commit_time_text_action(self):
        """
        动作：获取列表第一条数据提交时间的文本
        :return: '列表第一条数据提交时间'的文本
        """
        control_content = self.project.get_element_text(self.first_advice_commit_time_text)
        return control_content

    def get_first_advice_deal_time_text_action(self):
        """
        动作：获取列表第一条数据处理时间的文本
        :return: '列表第一条数据处理时间'的文本
        """
        control_content = self.project.get_element_text(self.first_advice_deal_time_text)
        return control_content

    def get_first_advice_deal_person_text_action(self):
        """
        动作：获取列表第一条数据处理人的文本
        :return: '列表第一条数据处理人'的文本
        """
        control_content = self.project.get_element_text(self.first_advice_deal_person_text)
        return control_content

    def get_first_advice_deal_result_text_action(self):
        """
        动作：获取列表第一条数据处理结果的文本
        :return: '列表第一条数据处理结果'的文本
        """
        control_content = self.project.get_element_text(self.first_advice_deal_result_text)
        return control_content

    def get_first_advice_deal_stauts_text_action(self):
        """
        动作：获取列表第一条数据状态的文本
        :return: '列表第一条数据状态'的文本
        """
        control_content = self.project.get_element_text(self.first_advice_deal_stauts_text)
        return control_content

    def click_first_advice_option_button_action(self):
        """
        动作：点击列表第一条数据操作
        :return: 点击'列表第一条数据操作'按钮后的页面
        """
        self.project.click(self.first_advice_option_button)
        return self.project.get_current_page_source()

    def get_first_advice_option_text_action(self):
        """
        动作：获取列表第一条数据操作文案的文本
        :return: '列表第一条数据操作文案'的文本
        """
        control_content = self.project.get_element_text(self.first_advice_option_text)
        return control_content

    def set_first_advice_deal_result_input_action(self, first_advice_deal_result_input):
        """
        动作：设置列表第一条数据处理结果填写
        :param first_advice_deal_result_input: 列表第一条数据处理结果填写
        :return: 设置'列表第一条数据处理结果填写'文本后的页面
        """
        self.project.clear_and_send_keys(self.first_advice_deal_result_input, first_advice_deal_result_input)
        return self.project.get_current_page_source()

    def click_first_advice_deal_result_commit_button_action(self):
        """
        动作：点击列表第一条数据处理结果确定按钮
        :return: 点击'列表第一条数据处理结果确定按钮'按钮后的页面
        """
        self.project.click(self.first_advice_deal_result_commit_button)
        return self.project.get_current_page_source()

    # endregion Actions
