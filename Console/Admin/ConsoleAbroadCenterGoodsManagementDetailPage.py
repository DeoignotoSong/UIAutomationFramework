from Utils.Log import log


"""
后台-商品服务管理-商品管理
console_url/review/course_record
"""


class ConsoleAbroadCenterGoodsManagementDetailPage:
    def __init__(self, project):
        self.project = project
        self.url = 'console_url/abroad_center/goods_management/detail/REPR0201000382800001'
        # region Fields
        # 消息提示
        self._message_content_text_tag = '/html/body/div[last()]/div/div[1]/p'
        # 商品包装服务名称
        self._product_pack_product_detail_service_name_text_tag = '/html/body/div/div/section/main/div/div[2]/div[2]/div/section[1]/form/div[1]/div/span'
        # 商品包装服务价格
        self._product_pack_product_detail_service_price_text_tag = '/html/body/div/div/section/main/div/div[2]/div[2]/div/section[1]/form/div[3]/div/span'
        # 商品包装基本信息商品名称
        self._product_pack_product_detail_name_text_tag = '/html/body/div/div/section/main/div/div[3]/div/div[2]/div/section[1]/form/div[1]/div/span'
        # 商品包装基本信息商品价格
        self._product_pack_product_detail_price_text_tag = '/html/body/div/div/section/main/div/div[3]/div/div[2]/div/section[1]/form/div[2]/div/span'
        # 商品服务内容合计价格
        self._product_pack_product_detail_price_strand_text_tag = '/html/body/div/div/section/main/div/div[3]/div/div[2]/div/section[1]/form/div[3]/div/span[1]'
        # 商品服务内容合计价格作为划线价是否展示在前台
        self._product_pack_product_detail_price_display_text_tag = '/html/body/div/div/section/main/div/div[3]/div/div[2]/div/section[1]/form/div[3]/div/span[2]'
        # 商品包装基本信息商品标签
        self._product_pack_product_detail_lable_text_tag = '/html/body/div/div/section/main/div/div[3]/div/div[2]/div/section[1]/form/div[4]/div/span'
        # 商品包装基本信息商品卖点
        self._product_pack_product_detail_usp_text_tag = '/html/body/div/div/section/main/div/div[3]/div/div[2]/div/section[1]/form/div[5]/div/span'
        # 商品包装基本信息退款说明
        self._product_pack_product_detail_refund_text_tag = '/html/body/div/div/section/main/div/div[3]/div/div[2]/div/section[1]/form/div[6]/div/span'
        # 商品包装基本信息专项条款
        self._product_pack_product_detail_terms_text_tag = '/html/body/div/div/section/main/div/div[3]/div/div[2]/div/section[1]/form/div[7]/div/span'
        # 商品包装基本信息搜索关键词1
        self._product_pack_product_detail_first_key_text_tag = '/html/body/div/div/section/main/div/div[3]/div/div[2]/div/section[1]/form/div[8]/div'
        # 商品包装基本信息搜索关键词2
        self._product_pack_product_detail_second_key_text_tag = '/html/body/div[1]/div/section/main/div/div[2]/form/div[1]/div[2]/div[8]/div/div/div[2]/div[2]/div/input'
        # 商品包装基本信息搜索关键词3
        self._product_pack_product_detail_third_key_text_tag = '/html/body/div[1]/div/section/main/div/div[2]/form/div[1]/div[2]/div[8]/div/div/div[2]/div[3]/div/input'
        # 商品包装其他信息服务保证
        self._product_pack_detail_other_ensue_text_tag = '/html/body/div/div/section/main/div/div[3]/div/div[2]/div/section[2]/form/div[1]/div/span'
        # 商品包装其他信息服务常见问题1
        self._product_pack_detail_other_first_question_text_tag = '/html/body/div/div/section/main/div/div[3]/div/div[2]/div/section[2]/form/div[2]/div[1]/div/span'
        # 商品包装其他信息服务常见问题1回答
        self._product_pack_detail_other_first_question_answer_text_tag = '/html/body/div/div/section/main/div/div[3]/div/div[2]/div/section[2]/form/div[2]/div[2]/div/span'
        # 商品包装其他信息服务常见问题2
        self._product_pack_detail_other_second_question_text_tag = '/html/body/div[1]/div/section/main/div/div[2]/form/div[2]/div[2]/div[3]/div[1]/div/div/div[2]/div/input'
        # 商品包装其他信息服务常见问题2回答
        self._product_pack_detail_other_second_question_answer_text_tag = '/html/body/div[1]/div/section/main/div/div[2]/form/div[2]/div[2]/div[3]/div[2]/div[1]/div/div[2]/div/textarea'
        # 商品包装审核记录结果
        self._product_pack_detail_audit_his_result_text_tag = '/html/body/div/div/section/main/div/div[4]/div[2]/div/div/div[3]/table/tbody/tr/td[3]/div'
        # 商品包装审核记录意见
        self._product_pack_detail_audit_his_opinion_text_tag = '/html/body/div/div/section/main/div/div[4]/div[2]/div/div/div[3]/table/tbody/tr/td[4]/div'
        # 商品履历编码
        self._product_pack_detail_product_his_id_text_tag = '/html/body/div/div/section/main/div/div[5]/div[2]/div/div/div[3]/table/tbody/tr/td[1]/div/a/span'
        # 商品履历审核状态
        self._product_pack_detail_product_his_result_text_tag = '/html/body/div/div/section/main/div/div[5]/div[2]/div/div/div[3]/table/tbody/tr/td[2]/div'
        # 商品预览按钮
        self._product_pack_detail_product_preview_button_tag = '/html/body/div/div/section/main/div/div[6]/button[1]'
        # 商品返回按钮
        self._product_pack_detail_product_return_button_tag = '/html/body/div/div/section/main/div/div[6]/button[2]'
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
    def product_pack_product_detail_service_name_text(self):
        """
        属性: 商品包装服务名称
        :return: 商品包装服务名称
        """
        element = None
        try:
            element = self.project.get_element(self._product_pack_product_detail_service_name_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def product_pack_product_detail_service_price_text(self):
        """
        属性: 商品包装服务价格
        :return: 商品包装服务价格
        """
        element = None
        try:
            element = self.project.get_element(self._product_pack_product_detail_service_price_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def product_pack_product_detail_name_text(self):
        """
        属性: 商品包装基本信息商品名称
        :return: 商品包装基本信息商品名称
        """
        element = None
        try:
            element = self.project.get_element(self._product_pack_product_detail_name_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def product_pack_product_detail_price_text(self):
        """
        属性: 商品包装基本信息商品价格
        :return: 商品包装基本信息商品价格
        """
        element = None
        try:
            element = self.project.get_element(self._product_pack_product_detail_price_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def product_pack_product_detail_price_strand_text(self):
        """
        属性: 商品服务内容合计价格
        :return: 商品服务内容合计价格
        """
        element = None
        try:
            element = self.project.get_element(self._product_pack_product_detail_price_strand_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def product_pack_product_detail_price_display_text(self):
        """
        属性: 商品服务内容合计价格作为划线价是否展示在前台
        :return: 商品服务内容合计价格作为划线价是否展示在前台
        """
        element = None
        try:
            element = self.project.get_element(self._product_pack_product_detail_price_display_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def product_pack_product_detail_lable_text(self):
        """
        属性: 商品包装基本信息商品标签
        :return: 商品包装基本信息商品标签
        """
        element = None
        try:
            element = self.project.get_element(self._product_pack_product_detail_lable_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def product_pack_product_detail_usp_text(self):
        """
        属性: 商品包装基本信息商品卖点
        :return: 商品包装基本信息商品卖点
        """
        element = None
        try:
            element = self.project.get_element(self._product_pack_product_detail_usp_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def product_pack_product_detail_refund_text(self):
        """
        属性: 商品包装基本信息退款说明
        :return: 商品包装基本信息退款说明
        """
        element = None
        try:
            element = self.project.get_element(self._product_pack_product_detail_refund_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def product_pack_product_detail_terms_text(self):
        """
        属性: 商品包装基本信息专项条款
        :return: 商品包装基本信息专项条款
        """
        element = None
        try:
            element = self.project.get_element(self._product_pack_product_detail_terms_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def product_pack_product_detail_first_key_text(self):
        """
        属性: 商品包装基本信息搜索关键词1
        :return: 商品包装基本信息搜索关键词1
        """
        element = None
        try:
            element = self.project.get_element(self._product_pack_product_detail_first_key_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def product_pack_product_detail_second_key_text(self):
        """
        属性: 商品包装基本信息搜索关键词2
        :return: 商品包装基本信息搜索关键词2
        """
        element = None
        try:
            element = self.project.get_element(self._product_pack_product_detail_second_key_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def product_pack_product_detail_third_key_text(self):
        """
        属性: 商品包装基本信息搜索关键词3
        :return: 商品包装基本信息搜索关键词3
        """
        element = None
        try:
            element = self.project.get_element(self._product_pack_product_detail_third_key_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def product_pack_detail_other_ensue_text(self):
        """
        属性: 商品包装其他信息服务保证
        :return: 商品包装其他信息服务保证
        """
        element = None
        try:
            element = self.project.get_element(self._product_pack_detail_other_ensue_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def product_pack_detail_other_first_question_text(self):
        """
        属性: 商品包装其他信息服务常见问题1
        :return: 商品包装其他信息服务常见问题1
        """
        element = None
        try:
            element = self.project.get_element(self._product_pack_detail_other_first_question_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def product_pack_detail_other_first_question_answer_text(self):
        """
        属性: 商品包装其他信息服务常见问题1回答
        :return: 商品包装其他信息服务常见问题1回答
        """
        element = None
        try:
            element = self.project.get_element(self._product_pack_detail_other_first_question_answer_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def product_pack_detail_other_second_question_text(self):
        """
        属性: 商品包装其他信息服务常见问题2
        :return: 商品包装其他信息服务常见问题2
        """
        element = None
        try:
            element = self.project.get_element(self._product_pack_detail_other_second_question_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def product_pack_detail_other_second_question_answer_text(self):
        """
        属性: 商品包装其他信息服务常见问题2回答
        :return: 商品包装其他信息服务常见问题2回答
        """
        element = None
        try:
            element = self.project.get_element(self._product_pack_detail_other_second_question_answer_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def product_pack_detail_audit_his_result_text(self):
        """
        属性: 商品包装审核记录结果
        :return: 商品包装审核记录结果
        """
        element = None
        try:
            element = self.project.get_element(self._product_pack_detail_audit_his_result_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def product_pack_detail_audit_his_opinion_text(self):
        """
        属性: 商品包装审核记录意见
        :return: 商品包装审核记录意见
        """
        element = None
        try:
            element = self.project.get_element(self._product_pack_detail_audit_his_opinion_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def product_pack_detail_product_his_id_text(self):
        """
        属性: 商品履历编码
        :return: 商品履历编码
        """
        element = None
        try:
            element = self.project.get_element(self._product_pack_detail_product_his_id_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def product_pack_detail_product_his_result_text(self):
        """
        属性: 商品履历审核状态
        :return: 商品履历审核状态
        """
        element = None
        try:
            element = self.project.get_element(self._product_pack_detail_product_his_result_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def product_pack_detail_product_preview_button(self):
        """
        属性: 商品预览按钮
        :return: 商品预览按钮
        """
        element = None
        try:
            element = self.project.get_element(self._product_pack_detail_product_preview_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def product_pack_detail_product_return_button(self):
        """
        属性: 商品返回按钮
        :return: 商品返回按钮
        """
        element = None
        try:
            element = self.project.get_element(self._product_pack_detail_product_return_button_tag)
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

    def get_product_pack_product_detail_service_name_text_action(self):
        """
        动作：获取商品包装服务名称的文本
        :return: '商品包装服务名称'的文本
        """
        control_content = self.project.get_element_text(self.product_pack_product_detail_service_name_text)
        return control_content

    def get_product_pack_product_detail_service_price_text_action(self):
        """
        动作：获取商品包装服务价格的文本
        :return: '商品包装服务价格'的文本
        """
        control_content = self.project.get_element_text(self.product_pack_product_detail_service_price_text)
        return control_content

    def get_product_pack_product_detail_name_text_action(self):
        """
        动作：获取商品包装基本信息商品名称的文本
        :return: '商品包装基本信息商品名称'的文本
        """
        control_content = self.project.get_element_text(self.product_pack_product_detail_name_text)
        return control_content

    def get_product_pack_product_detail_price_text_action(self):
        """
        动作：获取商品包装基本信息商品价格的文本
        :return: '商品包装基本信息商品价格'的文本
        """
        control_content = self.project.get_element_text(self.product_pack_product_detail_price_text)
        return control_content

    def get_product_pack_product_detail_price_strand_text_action(self):
        """
        动作：获取商品服务内容合计价格的文本
        :return: '商品服务内容合计价格'的文本
        """
        control_content = self.project.get_element_text(self.product_pack_product_detail_price_strand_text)
        return control_content

    def get_product_pack_product_detail_price_display_text_action(self):
        """
        动作：获取商品服务内容合计价格作为划线价是否展示在前台的文本
        :return: '商品服务内容合计价格作为划线价是否展示在前台'的文本
        """
        control_content = self.project.get_element_text(self.product_pack_product_detail_price_display_text)
        return control_content

    def get_product_pack_product_detail_lable_text_action(self):
        """
        动作：获取商品包装基本信息商品标签的文本
        :return: '商品包装基本信息商品标签'的文本
        """
        control_content = self.project.get_element_text(self.product_pack_product_detail_lable_text)
        return control_content

    def get_product_pack_product_detail_usp_text_action(self):
        """
        动作：获取商品包装基本信息商品卖点的文本
        :return: '商品包装基本信息商品卖点'的文本
        """
        control_content = self.project.get_element_text(self.product_pack_product_detail_usp_text)
        return control_content

    def get_product_pack_product_detail_refund_text_action(self):
        """
        动作：获取商品包装基本信息退款说明的文本
        :return: '商品包装基本信息退款说明'的文本
        """
        control_content = self.project.get_element_text(self.product_pack_product_detail_refund_text)
        return control_content

    def get_product_pack_product_detail_terms_text_action(self):
        """
        动作：获取商品包装基本信息专项条款的文本
        :return: '商品包装基本信息专项条款'的文本
        """
        control_content = self.project.get_element_text(self.product_pack_product_detail_terms_text)
        return control_content

    def get_product_pack_product_detail_first_key_text_action(self):
        """
        动作：获取商品包装基本信息搜索关键词1的文本
        :return: '商品包装基本信息搜索关键词1'的文本
        """
        control_content = self.project.get_element_text(self.product_pack_product_detail_first_key_text)
        return control_content

    def get_product_pack_product_detail_second_key_text_action(self):
        """
        动作：获取商品包装基本信息搜索关键词2的文本
        :return: '商品包装基本信息搜索关键词2'的文本
        """
        control_content = self.project.get_element_text(self.product_pack_product_detail_second_key_text)
        return control_content

    def get_product_pack_product_detail_third_key_text_action(self):
        """
        动作：获取商品包装基本信息搜索关键词3的文本
        :return: '商品包装基本信息搜索关键词3'的文本
        """
        control_content = self.project.get_element_text(self.product_pack_product_detail_third_key_text)
        return control_content

    def get_product_pack_detail_other_ensue_text_action(self):
        """
        动作：获取商品包装其他信息服务保证的文本
        :return: '商品包装其他信息服务保证'的文本
        """
        control_content = self.project.get_element_text(self.product_pack_detail_other_ensue_text)
        return control_content

    def get_product_pack_detail_other_first_question_text_action(self):
        """
        动作：获取商品包装其他信息服务常见问题1的文本
        :return: '商品包装其他信息服务常见问题1'的文本
        """
        control_content = self.project.get_element_text(self.product_pack_detail_other_first_question_text)
        return control_content

    def get_product_pack_detail_other_first_question_answer_text_action(self):
        """
        动作：获取商品包装其他信息服务常见问题1回答的文本
        :return: '商品包装其他信息服务常见问题1回答'的文本
        """
        control_content = self.project.get_element_text(self.product_pack_detail_other_first_question_answer_text)
        return control_content

    def get_product_pack_detail_other_second_question_text_action(self):
        """
        动作：获取商品包装其他信息服务常见问题2的文本
        :return: '商品包装其他信息服务常见问题2'的文本
        """
        control_content = self.project.get_element_text(self.product_pack_detail_other_second_question_text)
        return control_content

    def get_product_pack_detail_other_second_question_answer_text_action(self):
        """
        动作：获取商品包装其他信息服务常见问题2回答的文本
        :return: '商品包装其他信息服务常见问题2回答'的文本
        """
        control_content = self.project.get_element_text(self.product_pack_detail_other_second_question_answer_text)
        return control_content

    def get_product_pack_detail_audit_his_result_text_action(self):
        """
        动作：获取商品包装审核记录结果的文本
        :return: '商品包装审核记录结果'的文本
        """
        control_content = self.project.get_element_text(self.product_pack_detail_audit_his_result_text)
        return control_content

    def get_product_pack_detail_audit_his_opinion_text_action(self):
        """
        动作：获取商品包装审核记录意见的文本
        :return: '商品包装审核记录意见'的文本
        """
        control_content = self.project.get_element_text(self.product_pack_detail_audit_his_opinion_text)
        return control_content

    def get_product_pack_detail_product_his_id_text_action(self):
        """
        动作：获取商品履历编码的文本
        :return: '商品履历编码'的文本
        """
        control_content = self.project.get_element_text(self.product_pack_detail_product_his_id_text)
        return control_content

    def get_product_pack_detail_product_his_result_text_action(self):
        """
        动作：获取商品履历审核状态的文本
        :return: '商品履历审核状态'的文本
        """
        control_content = self.project.get_element_text(self.product_pack_detail_product_his_result_text)
        return control_content

    def click_product_pack_detail_product_preview_button_action(self):
        """
        动作：点击商品预览按钮
        :return: 点击'商品预览按钮'按钮后的页面
        """
        self.project.click(self.product_pack_detail_product_preview_button)
        return self.project.get_current_page_source()

    def click_product_pack_detail_product_return_button_action(self):
        """
        动作：点击商品返回按钮
        :return: 点击'商品返回按钮'按钮后的页面
        """
        self.project.click(self.product_pack_detail_product_return_button)
        return self.project.get_current_page_source()

    # endregion Actions
