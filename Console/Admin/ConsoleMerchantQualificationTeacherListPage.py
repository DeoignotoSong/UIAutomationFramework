from Utils.Log import log

"""
后台首页-平台入驻-资质审核管理-讲师审核列表
console_url/qualifications/teacher_list
"""


class ConsoleMerchantQualificationTeacherListPage:
    def __init__(self, project):
        self.project = project
        self.url = 'console_url/qualifications/teacher_list'
        # region Fields
        # 消息通知
        self._message_content_text_tag = '/html/body/div[last()]/div/div/p'
        # 下拉列表
        self._drop_down_list_select_tag = '/html/body/div[@class="el-select-dropdown el-popper"]/div[1]/div[1]/ul[@class="el-scrollbar__view el-select-dropdown__list"]'
        # 搜索-客户姓名
        self._search_customer_name_input_tag = '//*[@id="tableSearch"]/form/div/div[1]/div/div/input'
        # 搜索-联系电话
        self._search_mobile_input_tag = '//*[@id="tableSearch"]/form/div/div[2]/div/div/input'
        # 搜索-入驻赛道
        self._search_enter_category_button_tag = '//*[@id="tableSearch"]/form/div/div[3]/div/div'
        # 搜索-渠道
        self._search_source_button_tag = '//*[@id="tableSearch"]/form/div/div[4]/div/div'
        # 搜索-状态
        self._search_status_button_tag = '//*[@id="tableSearch"]/form/div/div[6]/div/div'
        # 搜索-查询
        self._search_query_button_tag = '//*[@id="tableSearch"]/form/div/div[last()-1]/div/button'
        # 搜索-清除
        self._search_clear_button_tag = '//*[@id="tableSearch"]/form/div/div[last()]/div/button'
        # 列表-第一行-客服姓名
        self._list_first_customer_name_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[1]/div'
        # 列表-第一行-联系电话
        self._list_first_mobile_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[2]/div'
        # 列表-第一行-入驻赛道
        self._list_first_enter_category_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[3]/div'
        # 列表-第一行-渠道
        self._list_first_source_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[4]/div'
        # 列表-第一行-提交时间
        self._list_first_commit_time_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[5]/div'
        # 列表-第一行-状态
        self._list_first_status_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[6]/div'
        # 列表-第一行-操作-第一个按钮
        self._list_first_execute_first_button_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div[1]/div[4]/div[2]/table/tbody/tr[1]/td[last()]/div/a[1]'
        # 列表-第一行-操作-第二个按钮
        self._list_first_execute_second_button_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div[1]/div[4]/div[2]/table/tbody/tr[1]/td[last()]/div/a[2]'
        # 资质详情-入驻信息-标题
        self._teacher_detail_enter_info_title_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[1]/div[1]/div/span'
        # 资质详情-入驻信息-商家类型
        self._teacher_detail_enter_info_merchant_type_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[1]/div[2]/div/form/div[1]/div[1]/div/div'
        # 资质详情-入驻信息-入驻赛道
        self._teacher_detail_enter_info_enter_category_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[1]/div[2]/div/form/div[1]/div[2]/div/div'
        # 资质详情-入驻信息-联系人
        self._teacher_detail_enter_info_user_name_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[1]/div[2]/div/form/div[2]/div[1]/div/div/span'
        # 资质详情-入驻信息-联系电话
        self._teacher_detail_enter_info_mobile_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[1]/div[2]/div/form/div[2]/div[2]/div/div/span'
        # 资质详情-证件信息-证件类型
        self._teacher_detail_certificate_info_type_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div[2]/div/form/div[1]/div[1]/div/div'
        # 资质详情-证件信息-姓名
        self._teacher_detail_certificate_info_user_name_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div[2]/div/form/div[1]/div[2]/div/div'
        # 资质详情-证件信息-证件号码
        self._teacher_detail_certificate_info_number_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div[2]/div/form/div[2]/div[1]/div/div'
        # 资质详情-证件信息-有效期
        self._teacher_detail_certificate_info_validity_text_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[2]/div[2]/div/form/div[2]/div[2]/div/div'
        # 资质详情-通过按钮
        self._teacher_detail_pass_button_tag = '//*[@id="ArticleReviewShow"]/button[1]'
        # 资质详情-通过-弹窗-确定
        self._teacher_detail_pass_popup_confirm_button_tag = '/html/body/div[@class="el-message-box__wrapper"]/div/div[3]/button[2]'
        # 资质详情-通过-弹窗-取消
        self._teacher_detail_pass_popup_cancel_button_tag = '/html/body/div[@class="el-message-box__wrapper"]/div/div[3]/button[1]'
        # 资质详情-通过-弹窗-关闭
        self._teacher_detail_pass_popup_close_button_tag = '/html/body/div[@class="el-message-box__wrapper"]/div/div[1]/button'
        # 资质详情-通过-弹窗-标题
        self._teacher_detail_pass_popup_title_text_tag = '/html/body/div[@class="el-message-box__wrapper"]/div/div[1]/div/span'
        # 资质详情-通过-弹窗-提示
        self._teacher_detail_pass_popup_tip_text_tag = '/html/body/div[@class="el-message-box__wrapper"]/div/div[2]/div[1]/div/p'
        # 资质详情-驳回按钮
        self._teacher_detail_reject_button_tag = '//*[@id="ArticleReviewShow"]/button[2]'
        # 资质详情-驳回-弹窗-确定
        self._teacher_detail_reject_popup_confirm_button_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[@class="page-st"]/div/div/div[3]/span/button[1]'
        # 资质详情-驳回-弹窗-取消
        self._teacher_detail_reject_popup_cancel_button_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[6]/div/div/div[3]/span/button[2]'
        # 资质详情-驳回-弹窗-关闭
        self._teacher_detail_reject_popup_close_button_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[6]/div/div/div[1]/button'
        # 资质详情-驳回-弹窗-驳回理由
        self._teacher_detail_reject_popup_reason_button_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[6]/div/div/div[2]/form/div[1]/div/div'
        # 资质详情-驳回-弹窗-驳回理由-其他
        self._teacher_detail_reject_popup_reason_custom_input_tag = '//*[@id="app"]/div/section/main/div/div[2]/div[6]/div/div/div[2]/form/div[2]/div/div/textarea'
        # 资质详情-返回按钮
        self._teacher_detail_return_button_tag = '//*[@id="ArticleReviewShow"]/button'
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
    def search_customer_name_input(self):
        """
        属性: 搜索-客户姓名
        :return: 搜索-客户姓名
        """
        element = None
        try:
            element = self.project.get_element(self._search_customer_name_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def search_mobile_input(self):
        """
        属性: 搜索-联系电话
        :return: 搜索-联系电话
        """
        element = None
        try:
            element = self.project.get_element(self._search_mobile_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def search_enter_category_button(self):
        """
        属性: 搜索-入驻赛道
        :return: 搜索-入驻赛道
        """
        element = None
        try:
            element = self.project.get_element(self._search_enter_category_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def search_source_button(self):
        """
        属性: 搜索-渠道
        :return: 搜索-渠道
        """
        element = None
        try:
            element = self.project.get_element(self._search_source_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def search_status_button(self):
        """
        属性: 搜索-状态
        :return: 搜索-状态
        """
        element = None
        try:
            element = self.project.get_element(self._search_status_button_tag)
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
    def list_first_customer_name_text(self):
        """
        属性: 列表-第一行-客服姓名
        :return: 列表-第一行-客服姓名
        """
        element = None
        try:
            element = self.project.get_element(self._list_first_customer_name_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def list_first_mobile_text(self):
        """
        属性: 列表-第一行-联系电话
        :return: 列表-第一行-联系电话
        """
        element = None
        try:
            element = self.project.get_element(self._list_first_mobile_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def list_first_enter_category_text(self):
        """
        属性: 列表-第一行-入驻赛道
        :return: 列表-第一行-入驻赛道
        """
        element = None
        try:
            element = self.project.get_element(self._list_first_enter_category_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def list_first_source_text(self):
        """
        属性: 列表-第一行-渠道
        :return: 列表-第一行-渠道
        """
        element = None
        try:
            element = self.project.get_element(self._list_first_source_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def list_first_commit_time_text(self):
        """
        属性: 列表-第一行-提交时间
        :return: 列表-第一行-提交时间
        """
        element = None
        try:
            element = self.project.get_element(self._list_first_commit_time_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def list_first_status_text(self):
        """
        属性: 列表-第一行-状态
        :return: 列表-第一行-状态
        """
        element = None
        try:
            element = self.project.get_element(self._list_first_status_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def list_first_execute_first_button(self):
        """
        属性: 列表-第一行-操作-第一个按钮
        :return: 列表-第一行-操作-第一个按钮
        """
        element = None
        try:
            element = self.project.get_element(self._list_first_execute_first_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def list_first_execute_second_button(self):
        """
        属性: 列表-第一行-操作-第二个按钮
        :return: 列表-第一行-操作-第二个按钮
        """
        element = None
        try:
            element = self.project.get_element(self._list_first_execute_second_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def teacher_detail_enter_info_title_text(self):
        """
        属性: 资质详情-入驻信息-标题
        :return: 资质详情-入驻信息-标题
        """
        element = None
        try:
            element = self.project.get_element(self._teacher_detail_enter_info_title_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def teacher_detail_enter_info_merchant_type_text(self):
        """
        属性: 资质详情-入驻信息-商家类型
        :return: 资质详情-入驻信息-商家类型
        """
        element = None
        try:
            element = self.project.get_element(self._teacher_detail_enter_info_merchant_type_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def teacher_detail_enter_info_enter_category_text(self):
        """
        属性: 资质详情-入驻信息-入驻赛道
        :return: 资质详情-入驻信息-入驻赛道
        """
        element = None
        try:
            element = self.project.get_element(self._teacher_detail_enter_info_enter_category_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def teacher_detail_enter_info_user_name_text(self):
        """
        属性: 资质详情-入驻信息-联系人
        :return: 资质详情-入驻信息-联系人
        """
        element = None
        try:
            element = self.project.get_element(self._teacher_detail_enter_info_user_name_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def teacher_detail_enter_info_mobile_text(self):
        """
        属性: 资质详情-入驻信息-联系电话
        :return: 资质详情-入驻信息-联系电话
        """
        element = None
        try:
            element = self.project.get_element(self._teacher_detail_enter_info_mobile_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def teacher_detail_certificate_info_type_text(self):
        """
        属性: 资质详情-证件信息-证件类型
        :return: 资质详情-证件信息-证件类型
        """
        element = None
        try:
            element = self.project.get_element(self._teacher_detail_certificate_info_type_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def teacher_detail_certificate_info_user_name_text(self):
        """
        属性: 资质详情-证件信息-姓名
        :return: 资质详情-证件信息-姓名
        """
        element = None
        try:
            element = self.project.get_element(self._teacher_detail_certificate_info_user_name_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def teacher_detail_certificate_info_number_text(self):
        """
        属性: 资质详情-证件信息-证件号码
        :return: 资质详情-证件信息-证件号码
        """
        element = None
        try:
            element = self.project.get_element(self._teacher_detail_certificate_info_number_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def teacher_detail_certificate_info_validity_text(self):
        """
        属性: 资质详情-证件信息-有效期
        :return: 资质详情-证件信息-有效期
        """
        element = None
        try:
            element = self.project.get_element(self._teacher_detail_certificate_info_validity_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def teacher_detail_pass_button(self):
        """
        属性: 资质详情-通过按钮
        :return: 资质详情-通过按钮
        """
        element = None
        try:
            element = self.project.get_element(self._teacher_detail_pass_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def teacher_detail_pass_popup_confirm_button(self):
        """
        属性: 资质详情-通过-弹窗-确定
        :return: 资质详情-通过-弹窗-确定
        """
        element = None
        try:
            element = self.project.get_element(self._teacher_detail_pass_popup_confirm_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def teacher_detail_pass_popup_cancel_button(self):
        """
        属性: 资质详情-通过-弹窗-取消
        :return: 资质详情-通过-弹窗-取消
        """
        element = None
        try:
            element = self.project.get_element(self._teacher_detail_pass_popup_cancel_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def teacher_detail_pass_popup_close_button(self):
        """
        属性: 资质详情-通过-弹窗-关闭
        :return: 资质详情-通过-弹窗-关闭
        """
        element = None
        try:
            element = self.project.get_element(self._teacher_detail_pass_popup_close_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def teacher_detail_pass_popup_title_text(self):
        """
        属性: 资质详情-通过-弹窗-标题
        :return: 资质详情-通过-弹窗-标题
        """
        element = None
        try:
            element = self.project.get_element(self._teacher_detail_pass_popup_title_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def teacher_detail_pass_popup_tip_text(self):
        """
        属性: 资质详情-通过-弹窗-提示
        :return: 资质详情-通过-弹窗-提示
        """
        element = None
        try:
            element = self.project.get_element(self._teacher_detail_pass_popup_tip_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def teacher_detail_reject_button(self):
        """
        属性: 资质详情-驳回按钮
        :return: 资质详情-驳回按钮
        """
        element = None
        try:
            element = self.project.get_element(self._teacher_detail_reject_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def teacher_detail_reject_popup_confirm_button(self):
        """
        属性: 资质详情-驳回-弹窗-确定
        :return: 资质详情-驳回-弹窗-确定
        """
        element = None
        try:
            element = self.project.get_element(self._teacher_detail_reject_popup_confirm_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def teacher_detail_reject_popup_cancel_button(self):
        """
        属性: 资质详情-驳回-弹窗-取消
        :return: 资质详情-驳回-弹窗-取消
        """
        element = None
        try:
            element = self.project.get_element(self._teacher_detail_reject_popup_cancel_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def teacher_detail_reject_popup_close_button(self):
        """
        属性: 资质详情-驳回-弹窗-关闭
        :return: 资质详情-驳回-弹窗-关闭
        """
        element = None
        try:
            element = self.project.get_element(self._teacher_detail_reject_popup_close_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def teacher_detail_reject_popup_reason_button(self):
        """
        属性: 资质详情-驳回-弹窗-驳回理由
        :return: 资质详情-驳回-弹窗-驳回理由
        """
        element = None
        try:
            element = self.project.get_element(self._teacher_detail_reject_popup_reason_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def teacher_detail_reject_popup_reason_custom_input(self):
        """
        属性: 资质详情-驳回-弹窗-驳回理由-其他
        :return: 资质详情-驳回-弹窗-驳回理由-其他
        """
        element = None
        try:
            element = self.project.get_element(self._teacher_detail_reject_popup_reason_custom_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def teacher_detail_return_button(self):
        """
        属性: 资质详情-返回按钮
        :return: 资质详情-返回按钮
        """
        element = None
        try:
            element = self.project.get_element(self._teacher_detail_return_button_tag)
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

    def set_search_customer_name_input_action(self, search_customer_name_input):
        """
        动作：设置搜索-客户姓名
        :param search_customer_name_input: 搜索-客户姓名
        :return: 设置'搜索-客户姓名'文本后的页面
        """
        self.project.clear_and_send_keys(self.search_customer_name_input, search_customer_name_input)
        return self.project.get_current_page_source()

    def set_search_mobile_input_action(self, search_mobile_input):
        """
        动作：设置搜索-联系电话
        :param search_mobile_input: 搜索-联系电话
        :return: 设置'搜索-联系电话'文本后的页面
        """
        self.project.clear_and_send_keys(self.search_mobile_input, search_mobile_input)
        return self.project.get_current_page_source()

    def click_search_enter_category_button_action(self):
        """
        动作：点击搜索-入驻赛道
        :return: 点击'搜索-入驻赛道'按钮后的页面
        """
        self.project.click(self.search_enter_category_button)
        return self.project.get_current_page_source()

    def click_search_source_button_action(self):
        """
        动作：点击搜索-渠道
        :return: 点击'搜索-渠道'按钮后的页面
        """
        self.project.click(self.search_source_button)
        return self.project.get_current_page_source()

    def click_search_status_button_action(self):
        """
        动作：点击搜索-状态
        :return: 点击'搜索-状态'按钮后的页面
        """
        self.project.click(self.search_status_button)
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

    def get_list_first_customer_name_text_action(self):
        """
        动作：获取列表-第一行-客服姓名的文本
        :return: '列表-第一行-客服姓名'的文本
        """
        control_content = self.project.get_element_text(self.list_first_customer_name_text)
        return control_content

    def get_list_first_mobile_text_action(self):
        """
        动作：获取列表-第一行-联系电话的文本
        :return: '列表-第一行-联系电话'的文本
        """
        control_content = self.project.get_element_text(self.list_first_mobile_text)
        return control_content

    def get_list_first_enter_category_text_action(self):
        """
        动作：获取列表-第一行-入驻赛道的文本
        :return: '列表-第一行-入驻赛道'的文本
        """
        control_content = self.project.get_element_text(self.list_first_enter_category_text)
        return control_content

    def get_list_first_source_text_action(self):
        """
        动作：获取列表-第一行-渠道的文本
        :return: '列表-第一行-渠道'的文本
        """
        control_content = self.project.get_element_text(self.list_first_source_text)
        return control_content

    def get_list_first_commit_time_text_action(self):
        """
        动作：获取列表-第一行-提交时间的文本
        :return: '列表-第一行-提交时间'的文本
        """
        control_content = self.project.get_element_text(self.list_first_commit_time_text)
        return control_content

    def get_list_first_status_text_action(self):
        """
        动作：获取列表-第一行-状态的文本
        :return: '列表-第一行-状态'的文本
        """
        control_content = self.project.get_element_text(self.list_first_status_text)
        return control_content

    def click_list_first_execute_first_button_action(self):
        """
        动作：点击列表-第一行-操作-第一个按钮
        :return: 点击'列表-第一行-操作-第一个按钮'按钮后的页面
        """
        self.project.click(self.list_first_execute_first_button)
        return self.project.get_current_page_source()

    def click_list_first_execute_second_button_action(self):
        """
        动作：点击列表-第一行-操作-第二个按钮
        :return: 点击'列表-第一行-操作-第二个按钮'按钮后的页面
        """
        self.project.click(self.list_first_execute_second_button)
        return self.project.get_current_page_source()

    def get_teacher_detail_enter_info_title_text_action(self):
        """
        动作：获取资质详情-入驻信息-标题的文本
        :return: '资质详情-入驻信息-标题'的文本
        """
        control_content = self.project.get_element_text(self.teacher_detail_enter_info_title_text)
        return control_content

    def get_teacher_detail_enter_info_merchant_type_text_action(self):
        """
        动作：获取资质详情-入驻信息-商家类型的文本
        :return: '资质详情-入驻信息-商家类型'的文本
        """
        control_content = self.project.get_element_text(self.teacher_detail_enter_info_merchant_type_text)
        return control_content

    def get_teacher_detail_enter_info_enter_category_text_action(self):
        """
        动作：获取资质详情-入驻信息-入驻赛道的文本
        :return: '资质详情-入驻信息-入驻赛道'的文本
        """
        control_content = self.project.get_element_text(self.teacher_detail_enter_info_enter_category_text)
        return control_content

    def get_teacher_detail_enter_info_user_name_text_action(self):
        """
        动作：获取资质详情-入驻信息-联系人的文本
        :return: '资质详情-入驻信息-联系人'的文本
        """
        control_content = self.project.get_element_text(self.teacher_detail_enter_info_user_name_text)
        return control_content

    def get_teacher_detail_enter_info_mobile_text_action(self):
        """
        动作：获取资质详情-入驻信息-联系电话的文本
        :return: '资质详情-入驻信息-联系电话'的文本
        """
        control_content = self.project.get_element_text(self.teacher_detail_enter_info_mobile_text)
        return control_content

    def get_teacher_detail_certificate_info_type_text_action(self):
        """
        动作：获取资质详情-证件信息-证件类型的文本
        :return: '资质详情-证件信息-证件类型'的文本
        """
        control_content = self.project.get_element_text(self.teacher_detail_certificate_info_type_text)
        return control_content

    def get_teacher_detail_certificate_info_user_name_text_action(self):
        """
        动作：获取资质详情-证件信息-姓名的文本
        :return: '资质详情-证件信息-姓名'的文本
        """
        control_content = self.project.get_element_text(self.teacher_detail_certificate_info_user_name_text)
        return control_content

    def get_teacher_detail_certificate_info_number_text_action(self):
        """
        动作：获取资质详情-证件信息-证件号码的文本
        :return: '资质详情-证件信息-证件号码'的文本
        """
        control_content = self.project.get_element_text(self.teacher_detail_certificate_info_number_text)
        return control_content

    def get_teacher_detail_certificate_info_validity_text_action(self):
        """
        动作：获取资质详情-证件信息-有效期的文本
        :return: '资质详情-证件信息-有效期'的文本
        """
        control_content = self.project.get_element_text(self.teacher_detail_certificate_info_validity_text)
        return control_content

    def click_teacher_detail_pass_button_action(self):
        """
        动作：点击资质详情-通过按钮
        :return: 点击'资质详情-通过按钮'按钮后的页面
        """
        self.project.click(self.teacher_detail_pass_button)
        return self.project.get_current_page_source()

    def click_teacher_detail_pass_popup_confirm_button_action(self):
        """
        动作：点击资质详情-通过-弹窗-确定
        :return: 点击'资质详情-通过-弹窗-确定'按钮后的页面
        """
        self.project.click(self.teacher_detail_pass_popup_confirm_button)
        return self.project.get_current_page_source()

    def click_teacher_detail_pass_popup_cancel_button_action(self):
        """
        动作：点击资质详情-通过-弹窗-取消
        :return: 点击'资质详情-通过-弹窗-取消'按钮后的页面
        """
        self.project.click(self.teacher_detail_pass_popup_cancel_button)
        return self.project.get_current_page_source()

    def click_teacher_detail_pass_popup_close_button_action(self):
        """
        动作：点击资质详情-通过-弹窗-关闭
        :return: 点击'资质详情-通过-弹窗-关闭'按钮后的页面
        """
        self.project.click(self.teacher_detail_pass_popup_close_button)
        return self.project.get_current_page_source()

    def get_teacher_detail_pass_popup_title_text_action(self):
        """
        动作：获取资质详情-通过-弹窗-标题的文本
        :return: '资质详情-通过-弹窗-标题'的文本
        """
        control_content = self.project.get_element_text(self.teacher_detail_pass_popup_title_text)
        return control_content

    def get_teacher_detail_pass_popup_tip_text_action(self):
        """
        动作：获取资质详情-通过-弹窗-提示的文本
        :return: '资质详情-通过-弹窗-提示'的文本
        """
        control_content = self.project.get_element_text(self.teacher_detail_pass_popup_tip_text)
        return control_content

    def click_teacher_detail_reject_button_action(self):
        """
        动作：点击资质详情-驳回按钮
        :return: 点击'资质详情-驳回按钮'按钮后的页面
        """
        self.project.click(self.teacher_detail_reject_button)
        return self.project.get_current_page_source()

    def click_teacher_detail_reject_popup_confirm_button_action(self):
        """
        动作：点击资质详情-驳回-弹窗-确定
        :return: 点击'资质详情-驳回-弹窗-确定'按钮后的页面
        """
        self.project.click(self.teacher_detail_reject_popup_confirm_button)
        return self.project.get_current_page_source()

    def click_teacher_detail_reject_popup_cancel_button_action(self):
        """
        动作：点击资质详情-驳回-弹窗-取消
        :return: 点击'资质详情-驳回-弹窗-取消'按钮后的页面
        """
        self.project.click(self.teacher_detail_reject_popup_cancel_button)
        return self.project.get_current_page_source()

    def click_teacher_detail_reject_popup_close_button_action(self):
        """
        动作：点击资质详情-驳回-弹窗-关闭
        :return: 点击'资质详情-驳回-弹窗-关闭'按钮后的页面
        """
        self.project.click(self.teacher_detail_reject_popup_close_button)
        return self.project.get_current_page_source()

    def click_teacher_detail_reject_popup_reason_button_action(self):
        """
        动作：点击资质详情-驳回-弹窗-驳回理由
        :return: 点击'资质详情-驳回-弹窗-驳回理由'按钮后的页面
        """
        self.project.click(self.teacher_detail_reject_popup_reason_button)
        return self.project.get_current_page_source()

    def set_teacher_detail_reject_popup_reason_custom_input_action(self, teacher_detail_reject_popup_reason_custom_input):
        """
        动作：设置资质详情-驳回-弹窗-驳回理由-其他
        :param teacher_detail_reject_popup_reason_custom_input: 资质详情-驳回-弹窗-驳回理由-其他
        :return: 设置'资质详情-驳回-弹窗-驳回理由-其他'文本后的页面
        """
        self.project.clear_and_send_keys(self.teacher_detail_reject_popup_reason_custom_input, teacher_detail_reject_popup_reason_custom_input)
        return self.project.get_current_page_source()

    def click_teacher_detail_return_button_action(self):
        """
        动作：点击资质详情-返回按钮
        :return: 点击'资质详情-返回按钮'按钮后的页面
        """
        self.project.click(self.teacher_detail_return_button)
        return self.project.get_current_page_source()

    # endregion Actions
