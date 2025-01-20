from Utils.Log import log


"""
后台-商品服务管理-商品管理-保存草稿箱-包装
console_url/review/course_record
"""


class ConsoleAbroadCenterGoodsManagementEditPage:
    def __init__(self, project):
        self.project = project
        self.url = 'console_url/abroad_center/goods_management/save/REPT0201000001590001'
        # region Fields
        # 消息提示
        self._message_content_text_tag = '/html/body/div[last()]/p'
        # 商品组合服务重新选择按钮
        self._product_pack_edit_button_tag = '/html/body/div[1]/div/section/main/div/div[2]/div/div[2]/form/div[1]/div/a/span'
        # 商品包装组合服务服务编码查询
        self._product_pack_edit_service_id_input_tag = '/html/body/div[3]/div/div[2]/div[1]/form/div/div[1]/div/div/input'
        # 商品包装组合服务服务名称查询
        self._product_pack_edit_service_name_input_tag = '/html/body/div[3]/div/div[2]/div[1]/form/div/div[2]/div/div/input'
        # 商品包装组合服务所属国家及地区
        self._product_pack_edit_service_country_list_select_tag = '/html/body/div[3]/div/div[2]/div[1]/form/div/div[3]/div/div/div[1]/input'
        # 商品包装组合服务所属国家及地区全部
        self._product_pack_edit_service_country_all_button_tag = '/html/body/div[4]/div[1]/div[1]/ul/li[1]'
        # 商品包装组合服务所属国家及地区美国
        self._product_pack_edit_service_country_america_button_tag = '/html/body/div[4]/div[1]/div[1]/ul/li[2]'
        # 商品包装组合服务查询
        self._product_pack_edit_service_search_button_tag = '/html/body/div[3]/div/div[2]/div[1]/form/div/div[4]/div/button'
        # 商品包装组合服务重置
        self._product_pack_edit_service_clear_button_tag = '/html/body/div[3]/div/div[2]/div[1]/form/div/div[5]/div/button'
        # 商品包装组合服务第一条数据服务编码
        self._first_list_product_pack_edit_service_id_text_tag = '/html/body/div[3]/div/div[2]/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[1]/div'
        # 商品包装组合服务第一条数据服务名称
        self._first_list_product_pack_edit_service_name_text_tag = '/html/body/div[3]/div/div[2]/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[2]/div'
        # 商品包装组合服务第一条数据所属国家和地区
        self._first_list_product_pack_edit_service_country_text_tag = '/html/body/div[3]/div/div[2]/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[3]/div'
        # 商品包装组合服务第一条数据包装
        self._first_list_product_pack_edit_service_pack_button_tag = '/html/body/div[3]/div/div[2]/div[2]/div[1]/div[4]/div[2]/table/tbody/tr[1]/td[4]/div/a/span'
        # 商品包装服务名称
        self._product_pack_product_edit_service_name_text_tag = '/html/body/div[1]/div/section/main/div/div[2]/div/div[2]/form/div[2]/div[1]/div/span'
        # 商品包装服务价格
        self._product_pack_product_edit_service_price_text_tag = '/html/body/div[1]/div/section/main/div/div[2]/div/div[2]/form/div[2]/div[3]/div/span'
        # 商品包装基本信息商品名称
        self._product_pack_product_edit_name_input_tag = '/html/body/div[1]/div/section/main/div/div[2]/form/div[1]/div[2]/div[1]/div/div/div[2]/div/input'
        # 商品包装基本信息商品价格
        self._product_pack_product_edit_price_input_tag = '/html/body/div[1]/div/section/main/div/div[2]/form/div[1]/div[2]/div[2]/div/div/div[2]/div[1]/input'
        # 商品服务内容合计价格作为划线价展示在前台
        self._product_pack_product_edit_price_display_button_tag = '/html/body/div[1]/div/section/main/div/div[2]/form/div[1]/div[2]/div[3]/div/div/div[2]/label[1]/span[2]'
        # 商品服务内容合计价格作为划线价不展示在前台
        self._product_pack_product_edit_price_undisplay_button_tag = '/html/body/div[1]/div/section/main/div/div[2]/form/div[1]/div[2]/div[3]/div/div/div[2]/label[2]/span[2]'
        # 商品包装基本信息商品标签优选
        self._product_pack_product_edit_lable_preference_button_tag = '/html/body/div[1]/div/section/main/div/div[2]/form/div[1]/div[2]/div[4]/div/div/div[2]/label[1]/span[2]'
        # 商品包装基本信息商品标签人气
        self._product_pack_product_edit_lable_popularity_button_tag = '/html/body/div[1]/div/section/main/div/div[2]/form/div[1]/div[2]/div[4]/div/div/div[2]/label[2]/span[2]'
        # 商品包装基本信息商品标签特色
        self._product_pack_product_edit_lable_characteristic_button_tag = '/html/body/div[1]/div/section/main/div/div[2]/form/div[1]/div[2]/div[4]/div/div/div[2]/label[3]/span[2]'
        # 商品包装基本信息商品卖点
        self._product_pack_product_edit_usp_input_tag = '/html/body/div[1]/div/section/main/div/div[2]/form/div[1]/div[2]/div[5]/div/div/div[2]/div/textarea'
        # 商品包装基本信息退款说明
        self._product_pack_product_edit_refund_input_tag = '/html/body/div[1]/div/section/main/div/div[2]/form/div[1]/div[2]/div[6]/div/div/div[2]/div/textarea'
        # 商品包装基本信息专项条款
        self._product_pack_product_edit_terms_input_tag = '/html/body/div[1]/div/section/main/div/div[2]/form/div[1]/div[2]/div[7]/div/div/div[2]/div/textarea'
        # 商品包装基本信息搜索关键词1
        self._product_pack_product_edit_first_key_input_tag = '/html/body/div[1]/div/section/main/div/div[2]/form/div[1]/div[2]/div[8]/div/div/div[2]/div[1]/div/input'
        # 商品包装基本信息搜索关键词2
        self._product_pack_product_edit_second_key_input_tag = '/html/body/div[1]/div/section/main/div/div[2]/form/div[1]/div[2]/div[8]/div/div/div[2]/div[2]/div/input'
        # 商品包装基本信息搜索关键词3
        self._product_pack_product_edit_third_key_input_tag = '/html/body/div[1]/div/section/main/div/div[2]/form/div[1]/div[2]/div[8]/div/div/div[2]/div[3]/div/input'
        # 商品包装基本信息主图1
        self._product_pack_product_edit_first_image_button_tag = '/html/body/div[1]/div/section/main/div/div[2]/form/div[1]/div[2]/div[9]/div/div/div[2]/div[1]/div[1]/div/div'
        # 商品包装基本信息主图1上传
        self._product_pack_product_edit_first_image_upload_input_tag = '/html/body/div[1]/div/section/main/div/div[2]/form/div[1]/div[2]/div[9]/div/div/div[2]/div[1]/div[1]/div/div/input'
        # 商品包装基本信息主图2
        self._product_pack_product_edit_second_image_button_tag = '/html/body/div[1]/div/section/main/div/div[2]/form/div[1]/div[2]/div[9]/div/div/div[2]/div[1]/div[2]'
        # 商品包装基本信息主图2上传
        self._product_pack_product_edit_second_image_upload_input_tag = '/html/body/div[1]/div/section/main/div/div[2]/form/div[1]/div[2]/div[9]/div/div/div[2]/div[1]/div[2]/div/div/input'
        # 商品包装基本信息主图3
        self._product_pack_product_edit_third_image_button_tag = '/html/body/div[1]/div/section/main/div/div[2]/form/div[1]/div[2]/div[9]/div/div/div[2]/div[1]/div[3]'
        # 商品包装基本信息主图3上传
        self._product_pack_product_edit_third_image_upload_input_tag = '/html/body/div[1]/div/section/main/div/div[2]/form/div[1]/div[2]/div[9]/div/div/div[2]/div[1]/div[3]/div/div/input'
        # 商品包装基本信息主图4
        self._product_pack_product_edit_fourth_image_button_tag = '/html/body/div[1]/div/section/main/div/div[2]/form/div[1]/div[2]/div[9]/div/div/div[2]/div[1]/div[4]'
        # 商品包装基本信息主图4上传
        self._product_pack_product_edit_fourth_image_upload_input_tag = '/html/body/div[1]/div/section/main/div/div[2]/form/div[1]/div[2]/div[9]/div/div/div[2]/div[1]/div[4]/div/div/input'
        # 商品包装基本信息主图5
        self._product_pack_product_edit_fifth_image_button_tag = '/html/body/div[1]/div/section/main/div/div[2]/form/div[1]/div[2]/div[9]/div/div/div[2]/div[1]/div[5]'
        # 商品包装基本信息主图5上传
        self._product_pack_product_edit_fifth_image_upload_input_tag = '/html/body/div[1]/div/section/main/div/div[2]/form/div[1]/div[2]/div[9]/div/div/div[2]/div[1]/div[5]/div/div/input'
        # 商品包装基本信息视频
        self._product_pack_product_edit_video_button_tag = '/html/body/div[1]/div/section/main/div/div[2]/form/div[1]/div[2]/div[10]/div/div/div[2]/div[1]/label'
        # 商品包装基本信息视频上传
        self._product_pack_product_edit_video_upload_input_tag = '//*[@id="file00"]'
        # 商品包装基本信息feed流图片
        self._product_pack_product_edit_feed_image_button_tag = '/html/body/div[1]/div/section/main/div/div[2]/form/div[1]/div[2]/div[11]/div/div/div[2]/div[1]/div/div/input'
        # 商品包装基本信息feed流图片上传
        self._product_pack_product_edit_feed_image_upload_input_tag = '/html/body/div[1]/div/section/main/div/div[2]/form/div[1]/div[2]/div[11]/div/div/div[2]/div[1]/div/div/input'
        # 商品包装其他信息服务保证退款
        self._product_pack_edit_other_ensue_refund_button_tag = '/html/body/div[1]/div/section/main/div/div[2]/form/div[2]/div[2]/div[1]/div/div/div[2]/div/label[1]/span[2]'
        # 商品包装其他信息服务保证平台
        self._product_pack_edit_other_ensue_platform_button_tag = '/html/body/div[1]/div/section/main/div/div[2]/form/div[2]/div[2]/div[1]/div/div/div[2]/div/label[2]/span[2]'
        # 商品包装其他信息服务服务流程
        self._product_pack_edit_other_ensue_service_button_tag = '/html/body/div[1]/div/section/main/div/div[2]/form/div[2]/div[2]/div[1]/div/div/div[2]/div/label[3]/span[2]'
        # 商品包装其他信息服务常见问题1
        self._product_pack_edit_other_first_question_input_tag = '/html/body/div[1]/div/section/main/div/div[2]/form/div[2]/div[2]/div[2]/div[1]/div/div/div[2]/div/input'
        # 商品包装其他信息服务常见问题1回答
        self._product_pack_edit_other_first_question_answer_input_tag = '/html/body/div[1]/div/section/main/div/div[2]/form/div[2]/div[2]/div[2]/div[2]/div[1]/div/div[2]/div/textarea'
        # 商品包装其他信息服务常见问题添加
        self._product_pack_edit_other_first_question_add_button_tag = '/html/body/div[1]/div/section/main/div/div[2]/form/div[2]/div[2]/div[2]/div[2]/div[2]/a/span'
        # 商品包装其他信息服务常见问题2
        self._product_pack_edit_other_second_question_input_tag = '/html/body/div[1]/div/section/main/div/div[2]/form/div[2]/div[2]/div[3]/div[1]/div/div/div[2]/div/input'
        # 商品包装其他信息服务常见问题2回答
        self._product_pack_edit_other_second_question_answer_input_tag = '/html/body/div[1]/div/section/main/div/div[2]/form/div[2]/div[2]/div[3]/div[2]/div[1]/div/div[2]/div/textarea'
        # 商品包装商品详情详情图
        self._product_pack_product_edit_detail_image_button_tag = '/html/body/div[1]/div/section/main/div/div[2]/form/div[3]/div[2]/div/div/div/div[2]/div[1]/div/div/input'
        # 商品包装商品详情详情图上传
        self._product_pack_product_edit_detail_image_upload_input_tag = '/html/body/div[1]/div/section/main/div/div[2]/form/div[3]/div[2]/div/div/div/div[2]/div[1]/div/div/input'
        # 商品包装附件合同
        self._product_pack_product_edit_contract_button_tag = '/html/body/div[1]/div/section/main/div/div[2]/form/div[4]/div[2]/div/div/div/div[2]/div[1]/div/div/div/div'
        # 商品包装附件合同上传
        self._product_pack_product_edit_contract_upload_input_tag = '/html/body/div[1]/div/section/main/div/div[2]/form/div[4]/div[2]/div/div/div/div[2]/div[1]/div/div/div/div/input'
        # 商品包装预览
        self._product_pack_product_edit_prview_button_tag = '/html/body/div[1]/div/section/main/div/div[3]/button[1]'
        # 商品包装保存
        self._product_pack_product_edit_save_button_tag = '/html/body/div[1]/div/section/main/div/div[3]/button[2]'
        # 商品包装提交审核
        self._product_pack_product_edit_submit_button_tag = '/html/body/div[1]/div/section/main/div/div[3]/button[3]'
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
    def product_pack_edit_button(self):
        """
        属性: 商品组合服务重新选择按钮
        :return: 商品组合服务重新选择按钮
        """
        element = None
        try:
            element = self.project.get_element(self._product_pack_edit_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def product_pack_edit_service_id_input(self):
        """
        属性: 商品包装组合服务服务编码查询
        :return: 商品包装组合服务服务编码查询
        """
        element = None
        try:
            element = self.project.get_element(self._product_pack_edit_service_id_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def product_pack_edit_service_name_input(self):
        """
        属性: 商品包装组合服务服务名称查询
        :return: 商品包装组合服务服务名称查询
        """
        element = None
        try:
            element = self.project.get_element(self._product_pack_edit_service_name_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def product_pack_edit_service_country_list_select(self):
        """
        属性: 商品包装组合服务所属国家及地区
        :return: 商品包装组合服务所属国家及地区
        """
        element = None
        try:
            element = self.project.get_element(self._product_pack_edit_service_country_list_select_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def product_pack_edit_service_country_all_button(self):
        """
        属性: 商品包装组合服务所属国家及地区全部
        :return: 商品包装组合服务所属国家及地区全部
        """
        element = None
        try:
            element = self.project.get_element(self._product_pack_edit_service_country_all_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def product_pack_edit_service_country_america_button(self):
        """
        属性: 商品包装组合服务所属国家及地区美国
        :return: 商品包装组合服务所属国家及地区美国
        """
        element = None
        try:
            element = self.project.get_element(self._product_pack_edit_service_country_america_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def product_pack_edit_service_search_button(self):
        """
        属性: 商品包装组合服务查询
        :return: 商品包装组合服务查询
        """
        element = None
        try:
            element = self.project.get_element(self._product_pack_edit_service_search_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def product_pack_edit_service_clear_button(self):
        """
        属性: 商品包装组合服务重置
        :return: 商品包装组合服务重置
        """
        element = None
        try:
            element = self.project.get_element(self._product_pack_edit_service_clear_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def first_list_product_pack_edit_service_id_text(self):
        """
        属性: 商品包装组合服务第一条数据服务编码
        :return: 商品包装组合服务第一条数据服务编码
        """
        element = None
        try:
            element = self.project.get_element(self._first_list_product_pack_edit_service_id_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def first_list_product_pack_edit_service_name_text(self):
        """
        属性: 商品包装组合服务第一条数据服务名称
        :return: 商品包装组合服务第一条数据服务名称
        """
        element = None
        try:
            element = self.project.get_element(self._first_list_product_pack_edit_service_name_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def first_list_product_pack_edit_service_country_text(self):
        """
        属性: 商品包装组合服务第一条数据所属国家和地区
        :return: 商品包装组合服务第一条数据所属国家和地区
        """
        element = None
        try:
            element = self.project.get_element(self._first_list_product_pack_edit_service_country_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def first_list_product_pack_edit_service_pack_button(self):
        """
        属性: 商品包装组合服务第一条数据包装
        :return: 商品包装组合服务第一条数据包装
        """
        element = None
        try:
            element = self.project.get_element(self._first_list_product_pack_edit_service_pack_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def product_pack_product_edit_service_name_text(self):
        """
        属性: 商品包装服务名称
        :return: 商品包装服务名称
        """
        element = None
        try:
            element = self.project.get_element(self._product_pack_product_edit_service_name_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def product_pack_product_edit_service_price_text(self):
        """
        属性: 商品包装服务价格
        :return: 商品包装服务价格
        """
        element = None
        try:
            element = self.project.get_element(self._product_pack_product_edit_service_price_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def product_pack_product_edit_name_input(self):
        """
        属性: 商品包装基本信息商品名称
        :return: 商品包装基本信息商品名称
        """
        element = None
        try:
            element = self.project.get_element(self._product_pack_product_edit_name_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def product_pack_product_edit_price_input(self):
        """
        属性: 商品包装基本信息商品价格
        :return: 商品包装基本信息商品价格
        """
        element = None
        try:
            element = self.project.get_element(self._product_pack_product_edit_price_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def product_pack_product_edit_price_display_button(self):
        """
        属性: 商品服务内容合计价格作为划线价展示在前台
        :return: 商品服务内容合计价格作为划线价展示在前台
        """
        element = None
        try:
            element = self.project.get_element(self._product_pack_product_edit_price_display_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def product_pack_product_edit_price_undisplay_button(self):
        """
        属性: 商品服务内容合计价格作为划线价不展示在前台
        :return: 商品服务内容合计价格作为划线价不展示在前台
        """
        element = None
        try:
            element = self.project.get_element(self._product_pack_product_edit_price_undisplay_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def product_pack_product_edit_lable_preference_button(self):
        """
        属性: 商品包装基本信息商品标签优选
        :return: 商品包装基本信息商品标签优选
        """
        element = None
        try:
            element = self.project.get_element(self._product_pack_product_edit_lable_preference_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def product_pack_product_edit_lable_popularity_button(self):
        """
        属性: 商品包装基本信息商品标签人气
        :return: 商品包装基本信息商品标签人气
        """
        element = None
        try:
            element = self.project.get_element(self._product_pack_product_edit_lable_popularity_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def product_pack_product_edit_lable_characteristic_button(self):
        """
        属性: 商品包装基本信息商品标签特色
        :return: 商品包装基本信息商品标签特色
        """
        element = None
        try:
            element = self.project.get_element(self._product_pack_product_edit_lable_characteristic_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def product_pack_product_edit_usp_input(self):
        """
        属性: 商品包装基本信息商品卖点
        :return: 商品包装基本信息商品卖点
        """
        element = None
        try:
            element = self.project.get_element(self._product_pack_product_edit_usp_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def product_pack_product_edit_refund_input(self):
        """
        属性: 商品包装基本信息退款说明
        :return: 商品包装基本信息退款说明
        """
        element = None
        try:
            element = self.project.get_element(self._product_pack_product_edit_refund_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def product_pack_product_edit_terms_input(self):
        """
        属性: 商品包装基本信息专项条款
        :return: 商品包装基本信息专项条款
        """
        element = None
        try:
            element = self.project.get_element(self._product_pack_product_edit_terms_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def product_pack_product_edit_first_key_input(self):
        """
        属性: 商品包装基本信息搜索关键词1
        :return: 商品包装基本信息搜索关键词1
        """
        element = None
        try:
            element = self.project.get_element(self._product_pack_product_edit_first_key_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def product_pack_product_edit_second_key_input(self):
        """
        属性: 商品包装基本信息搜索关键词2
        :return: 商品包装基本信息搜索关键词2
        """
        element = None
        try:
            element = self.project.get_element(self._product_pack_product_edit_second_key_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def product_pack_product_edit_third_key_input(self):
        """
        属性: 商品包装基本信息搜索关键词3
        :return: 商品包装基本信息搜索关键词3
        """
        element = None
        try:
            element = self.project.get_element(self._product_pack_product_edit_third_key_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def product_pack_product_edit_first_image_button(self):
        """
        属性: 商品包装基本信息主图1
        :return: 商品包装基本信息主图1
        """
        element = None
        try:
            element = self.project.get_element(self._product_pack_product_edit_first_image_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def product_pack_product_edit_first_image_upload_input(self):
        """
        属性: 商品包装基本信息主图1上传
        :return: 商品包装基本信息主图1上传
        """
        element = None
        try:
            element = self.project.get_element(self._product_pack_product_edit_first_image_upload_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def product_pack_product_edit_second_image_button(self):
        """
        属性: 商品包装基本信息主图2
        :return: 商品包装基本信息主图2
        """
        element = None
        try:
            element = self.project.get_element(self._product_pack_product_edit_second_image_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def product_pack_product_edit_second_image_upload_input(self):
        """
        属性: 商品包装基本信息主图2上传
        :return: 商品包装基本信息主图2上传
        """
        element = None
        try:
            element = self.project.get_element(self._product_pack_product_edit_second_image_upload_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def product_pack_product_edit_third_image_button(self):
        """
        属性: 商品包装基本信息主图3
        :return: 商品包装基本信息主图3
        """
        element = None
        try:
            element = self.project.get_element(self._product_pack_product_edit_third_image_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def product_pack_product_edit_third_image_upload_input(self):
        """
        属性: 商品包装基本信息主图3上传
        :return: 商品包装基本信息主图3上传
        """
        element = None
        try:
            element = self.project.get_element(self._product_pack_product_edit_third_image_upload_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def product_pack_product_edit_fourth_image_button(self):
        """
        属性: 商品包装基本信息主图4
        :return: 商品包装基本信息主图4
        """
        element = None
        try:
            element = self.project.get_element(self._product_pack_product_edit_fourth_image_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def product_pack_product_edit_fourth_image_upload_input(self):
        """
        属性: 商品包装基本信息主图4上传
        :return: 商品包装基本信息主图4上传
        """
        element = None
        try:
            element = self.project.get_element(self._product_pack_product_edit_fourth_image_upload_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def product_pack_product_edit_fifth_image_button(self):
        """
        属性: 商品包装基本信息主图5
        :return: 商品包装基本信息主图5
        """
        element = None
        try:
            element = self.project.get_element(self._product_pack_product_edit_fifth_image_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def product_pack_product_edit_fifth_image_upload_input(self):
        """
        属性: 商品包装基本信息主图5上传
        :return: 商品包装基本信息主图5上传
        """
        element = None
        try:
            element = self.project.get_element(self._product_pack_product_edit_fifth_image_upload_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def product_pack_product_edit_video_button(self):
        """
        属性: 商品包装基本信息视频
        :return: 商品包装基本信息视频
        """
        element = None
        try:
            element = self.project.get_element(self._product_pack_product_edit_video_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def product_pack_product_edit_video_upload_input(self):
        """
        属性: 商品包装基本信息视频上传
        :return: 商品包装基本信息视频上传
        """
        element = None
        try:
            element = self.project.get_element(self._product_pack_product_edit_video_upload_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def product_pack_product_edit_feed_image_button(self):
        """
        属性: 商品包装基本信息feed流图片
        :return: 商品包装基本信息feed流图片
        """
        element = None
        try:
            element = self.project.get_element(self._product_pack_product_edit_feed_image_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def product_pack_product_edit_feed_image_upload_input(self):
        """
        属性: 商品包装基本信息feed流图片上传
        :return: 商品包装基本信息feed流图片上传
        """
        element = None
        try:
            element = self.project.get_element(self._product_pack_product_edit_feed_image_upload_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def product_pack_edit_other_ensue_refund_button(self):
        """
        属性: 商品包装其他信息服务保证退款
        :return: 商品包装其他信息服务保证退款
        """
        element = None
        try:
            element = self.project.get_element(self._product_pack_edit_other_ensue_refund_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def product_pack_edit_other_ensue_platform_button(self):
        """
        属性: 商品包装其他信息服务保证平台
        :return: 商品包装其他信息服务保证平台
        """
        element = None
        try:
            element = self.project.get_element(self._product_pack_edit_other_ensue_platform_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def product_pack_edit_other_ensue_service_button(self):
        """
        属性: 商品包装其他信息服务服务流程
        :return: 商品包装其他信息服务服务流程
        """
        element = None
        try:
            element = self.project.get_element(self._product_pack_edit_other_ensue_service_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def product_pack_edit_other_first_question_input(self):
        """
        属性: 商品包装其他信息服务常见问题1
        :return: 商品包装其他信息服务常见问题1
        """
        element = None
        try:
            element = self.project.get_element(self._product_pack_edit_other_first_question_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def product_pack_edit_other_first_question_answer_input(self):
        """
        属性: 商品包装其他信息服务常见问题1回答
        :return: 商品包装其他信息服务常见问题1回答
        """
        element = None
        try:
            element = self.project.get_element(self._product_pack_edit_other_first_question_answer_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def product_pack_edit_other_first_question_add_button(self):
        """
        属性: 商品包装其他信息服务常见问题添加
        :return: 商品包装其他信息服务常见问题添加
        """
        element = None
        try:
            element = self.project.get_element(self._product_pack_edit_other_first_question_add_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def product_pack_edit_other_second_question_input(self):
        """
        属性: 商品包装其他信息服务常见问题2
        :return: 商品包装其他信息服务常见问题2
        """
        element = None
        try:
            element = self.project.get_element(self._product_pack_edit_other_second_question_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def product_pack_edit_other_second_question_answer_input(self):
        """
        属性: 商品包装其他信息服务常见问题2回答
        :return: 商品包装其他信息服务常见问题2回答
        """
        element = None
        try:
            element = self.project.get_element(self._product_pack_edit_other_second_question_answer_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def product_pack_product_edit_detail_image_button(self):
        """
        属性: 商品包装商品详情详情图
        :return: 商品包装商品详情详情图
        """
        element = None
        try:
            element = self.project.get_element(self._product_pack_product_edit_detail_image_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def product_pack_product_edit_detail_image_upload_input(self):
        """
        属性: 商品包装商品详情详情图上传
        :return: 商品包装商品详情详情图上传
        """
        element = None
        try:
            element = self.project.get_element(self._product_pack_product_edit_detail_image_upload_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def product_pack_product_edit_contract_button(self):
        """
        属性: 商品包装附件合同
        :return: 商品包装附件合同
        """
        element = None
        try:
            element = self.project.get_element(self._product_pack_product_edit_contract_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def product_pack_product_edit_contract_upload_input(self):
        """
        属性: 商品包装附件合同上传
        :return: 商品包装附件合同上传
        """
        element = None
        try:
            element = self.project.get_element(self._product_pack_product_edit_contract_upload_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def product_pack_product_edit_prview_button(self):
        """
        属性: 商品包装预览
        :return: 商品包装预览
        """
        element = None
        try:
            element = self.project.get_element(self._product_pack_product_edit_prview_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def product_pack_product_edit_save_button(self):
        """
        属性: 商品包装保存
        :return: 商品包装保存
        """
        element = None
        try:
            element = self.project.get_element(self._product_pack_product_edit_save_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def product_pack_product_edit_submit_button(self):
        """
        属性: 商品包装提交审核
        :return: 商品包装提交审核
        """
        element = None
        try:
            element = self.project.get_element(self._product_pack_product_edit_submit_button_tag)
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

    def click_product_pack_edit_button_action(self):
        """
        动作：点击商品组合服务重新选择按钮
        :return: 点击'商品组合服务重新选择按钮'按钮后的页面
        """
        self.project.click(self.product_pack_edit_button)
        return self.project.get_current_page_source()

    def set_product_pack_edit_service_id_input_action(self, product_pack_edit_service_id_input):
        """
        动作：设置商品包装组合服务服务编码查询
        :param product_pack_edit_service_id_input: 商品包装组合服务服务编码查询
        :return: 设置'商品包装组合服务服务编码查询'文本后的页面
        """
        self.project.clear_and_send_keys(self.product_pack_edit_service_id_input, product_pack_edit_service_id_input)
        return self.project.get_current_page_source()

    def set_product_pack_edit_service_name_input_action(self, product_pack_edit_service_name_input):
        """
        动作：设置商品包装组合服务服务名称查询
        :param product_pack_edit_service_name_input: 商品包装组合服务服务名称查询
        :return: 设置'商品包装组合服务服务名称查询'文本后的页面
        """
        self.project.clear_and_send_keys(self.product_pack_edit_service_name_input, product_pack_edit_service_name_input)
        return self.project.get_current_page_source()

    def get_select_product_pack_edit_service_country_list_action(self, product_pack_edit_service_country_list_select):
        """
        动作：获取商品包装组合服务所属国家及地区列表选中的文本
        :param product_pack_edit_service_country_list_select: 商品包装组合服务所属国家及地区列表索引或文本
        :return: '商品包装组合服务所属国家及地区'的文本
        """
        control_content = self.project.get_select_content(self.product_pack_edit_service_country_list_select, product_pack_edit_service_country_list_select)
        return control_content

    def select_product_pack_edit_service_country_list_action(self, product_pack_edit_service_country_list_select):
        """
        动作：选择商品包装组合服务所属国家及地区
        :param product_pack_edit_service_country_list_select: 商品包装组合服务所属国家及地区列表索引或文本
        :return: 选择'商品包装组合服务所属国家及地区'选择器后的页面
        """
        self.project.select_control(self.product_pack_edit_service_country_list_select, product_pack_edit_service_country_list_select)
        return self.project.get_current_page_source()

    def click_product_pack_edit_service_country_all_button_action(self):
        """
        动作：点击商品包装组合服务所属国家及地区全部
        :return: 点击'商品包装组合服务所属国家及地区全部'按钮后的页面
        """
        self.project.click(self.product_pack_edit_service_country_all_button)
        return self.project.get_current_page_source()

    def click_product_pack_edit_service_country_america_button_action(self):
        """
        动作：点击商品包装组合服务所属国家及地区美国
        :return: 点击'商品包装组合服务所属国家及地区美国'按钮后的页面
        """
        self.project.click(self.product_pack_edit_service_country_america_button)
        return self.project.get_current_page_source()

    def click_product_pack_edit_service_search_button_action(self):
        """
        动作：点击商品包装组合服务查询
        :return: 点击'商品包装组合服务查询'按钮后的页面
        """
        self.project.click(self.product_pack_edit_service_search_button)
        return self.project.get_current_page_source()

    def click_product_pack_edit_service_clear_button_action(self):
        """
        动作：点击商品包装组合服务重置
        :return: 点击'商品包装组合服务重置'按钮后的页面
        """
        self.project.click(self.product_pack_edit_service_clear_button)
        return self.project.get_current_page_source()

    def get_first_list_product_pack_edit_service_id_text_action(self):
        """
        动作：获取商品包装组合服务第一条数据服务编码的文本
        :return: '商品包装组合服务第一条数据服务编码'的文本
        """
        control_content = self.project.get_element_text(self.first_list_product_pack_edit_service_id_text)
        return control_content

    def get_first_list_product_pack_edit_service_name_text_action(self):
        """
        动作：获取商品包装组合服务第一条数据服务名称的文本
        :return: '商品包装组合服务第一条数据服务名称'的文本
        """
        control_content = self.project.get_element_text(self.first_list_product_pack_edit_service_name_text)
        return control_content

    def get_first_list_product_pack_edit_service_country_text_action(self):
        """
        动作：获取商品包装组合服务第一条数据所属国家和地区的文本
        :return: '商品包装组合服务第一条数据所属国家和地区'的文本
        """
        control_content = self.project.get_element_text(self.first_list_product_pack_edit_service_country_text)
        return control_content

    def click_first_list_product_pack_edit_service_pack_button_action(self):
        """
        动作：点击商品包装组合服务第一条数据包装
        :return: 点击'商品包装组合服务第一条数据包装'按钮后的页面
        """
        self.project.click(self.first_list_product_pack_edit_service_pack_button)
        return self.project.get_current_page_source()

    def get_product_pack_product_edit_service_name_text_action(self):
        """
        动作：获取商品包装服务名称的文本
        :return: '商品包装服务名称'的文本
        """
        control_content = self.project.get_element_text(self.product_pack_product_edit_service_name_text)
        return control_content

    def get_product_pack_product_edit_service_price_text_action(self):
        """
        动作：获取商品包装服务价格的文本
        :return: '商品包装服务价格'的文本
        """
        control_content = self.project.get_element_text(self.product_pack_product_edit_service_price_text)
        return control_content

    def set_product_pack_product_edit_name_input_action(self, product_pack_product_edit_name_input):
        """
        动作：设置商品包装基本信息商品名称
        :param product_pack_product_edit_name_input: 商品包装基本信息商品名称
        :return: 设置'商品包装基本信息商品名称'文本后的页面
        """
        self.project.clear_and_send_keys(self.product_pack_product_edit_name_input, product_pack_product_edit_name_input)
        return self.project.get_current_page_source()

    def set_product_pack_product_edit_price_input_action(self, product_pack_product_edit_price_input):
        """
        动作：设置商品包装基本信息商品价格
        :param product_pack_product_edit_price_input: 商品包装基本信息商品价格
        :return: 设置'商品包装基本信息商品价格'文本后的页面
        """
        self.project.clear_and_send_keys(self.product_pack_product_edit_price_input, product_pack_product_edit_price_input)
        return self.project.get_current_page_source()

    def click_product_pack_product_edit_price_display_button_action(self):
        """
        动作：点击商品服务内容合计价格作为划线价展示在前台
        :return: 点击'商品服务内容合计价格作为划线价展示在前台'按钮后的页面
        """
        self.project.click(self.product_pack_product_edit_price_display_button)
        return self.project.get_current_page_source()

    def click_product_pack_product_edit_price_undisplay_button_action(self):
        """
        动作：点击商品服务内容合计价格作为划线价不展示在前台
        :return: 点击'商品服务内容合计价格作为划线价不展示在前台'按钮后的页面
        """
        self.project.click(self.product_pack_product_edit_price_undisplay_button)
        return self.project.get_current_page_source()

    def click_product_pack_product_edit_lable_preference_button_action(self):
        """
        动作：点击商品包装基本信息商品标签优选
        :return: 点击'商品包装基本信息商品标签优选'按钮后的页面
        """
        self.project.click(self.product_pack_product_edit_lable_preference_button)
        return self.project.get_current_page_source()

    def click_product_pack_product_edit_lable_popularity_button_action(self):
        """
        动作：点击商品包装基本信息商品标签人气
        :return: 点击'商品包装基本信息商品标签人气'按钮后的页面
        """
        self.project.click(self.product_pack_product_edit_lable_popularity_button)
        return self.project.get_current_page_source()

    def click_product_pack_product_edit_lable_characteristic_button_action(self):
        """
        动作：点击商品包装基本信息商品标签特色
        :return: 点击'商品包装基本信息商品标签特色'按钮后的页面
        """
        self.project.click(self.product_pack_product_edit_lable_characteristic_button)
        return self.project.get_current_page_source()

    def set_product_pack_product_edit_usp_input_action(self, product_pack_product_edit_usp_input):
        """
        动作：设置商品包装基本信息商品卖点
        :param product_pack_product_edit_usp_input: 商品包装基本信息商品卖点
        :return: 设置'商品包装基本信息商品卖点'文本后的页面
        """
        self.project.clear_and_send_keys(self.product_pack_product_edit_usp_input, product_pack_product_edit_usp_input)
        return self.project.get_current_page_source()

    def set_product_pack_product_edit_refund_input_action(self, product_pack_product_edit_refund_input):
        """
        动作：设置商品包装基本信息退款说明
        :param product_pack_product_edit_refund_input: 商品包装基本信息退款说明
        :return: 设置'商品包装基本信息退款说明'文本后的页面
        """
        self.project.clear_and_send_keys(self.product_pack_product_edit_refund_input, product_pack_product_edit_refund_input)
        return self.project.get_current_page_source()

    def set_product_pack_product_edit_terms_input_action(self, product_pack_product_edit_terms_input):
        """
        动作：设置商品包装基本信息专项条款
        :param product_pack_product_edit_terms_input: 商品包装基本信息专项条款
        :return: 设置'商品包装基本信息专项条款'文本后的页面
        """
        self.project.clear_and_send_keys(self.product_pack_product_edit_terms_input, product_pack_product_edit_terms_input)
        return self.project.get_current_page_source()

    def set_product_pack_product_edit_first_key_input_action(self, product_pack_product_edit_first_key_input):
        """
        动作：设置商品包装基本信息搜索关键词1
        :param product_pack_product_edit_first_key_input: 商品包装基本信息搜索关键词1
        :return: 设置'商品包装基本信息搜索关键词1'文本后的页面
        """
        self.project.clear_and_send_keys(self.product_pack_product_edit_first_key_input, product_pack_product_edit_first_key_input)
        return self.project.get_current_page_source()

    def set_product_pack_product_edit_second_key_input_action(self, product_pack_product_edit_second_key_input):
        """
        动作：设置商品包装基本信息搜索关键词2
        :param product_pack_product_edit_second_key_input: 商品包装基本信息搜索关键词2
        :return: 设置'商品包装基本信息搜索关键词2'文本后的页面
        """
        self.project.clear_and_send_keys(self.product_pack_product_edit_second_key_input, product_pack_product_edit_second_key_input)
        return self.project.get_current_page_source()

    def set_product_pack_product_edit_third_key_input_action(self, product_pack_product_edit_third_key_input):
        """
        动作：设置商品包装基本信息搜索关键词3
        :param product_pack_product_edit_third_key_input: 商品包装基本信息搜索关键词3
        :return: 设置'商品包装基本信息搜索关键词3'文本后的页面
        """
        self.project.clear_and_send_keys(self.product_pack_product_edit_third_key_input, product_pack_product_edit_third_key_input)
        return self.project.get_current_page_source()

    def click_product_pack_product_edit_first_image_button_action(self):
        """
        动作：点击商品包装基本信息主图1
        :return: 点击'商品包装基本信息主图1'按钮后的页面
        """
        self.project.click(self.product_pack_product_edit_first_image_button)
        return self.project.get_current_page_source()

    def set_product_pack_product_edit_first_image_upload_input_action(self, product_pack_product_edit_first_image_upload_input):
        """
        动作：设置商品包装基本信息主图1上传
        :param product_pack_product_edit_first_image_upload_input: 商品包装基本信息主图1上传
        :return: 设置'商品包装基本信息主图1上传'文本后的页面
        """
        self.project.clear_and_send_keys(self.product_pack_product_edit_first_image_upload_input, product_pack_product_edit_first_image_upload_input)
        return self.project.get_current_page_source()

    def click_product_pack_product_edit_second_image_button_action(self):
        """
        动作：点击商品包装基本信息主图2
        :return: 点击'商品包装基本信息主图2'按钮后的页面
        """
        self.project.click(self.product_pack_product_edit_second_image_button)
        return self.project.get_current_page_source()

    def set_product_pack_product_edit_second_image_upload_input_action(self, product_pack_product_edit_second_image_upload_input):
        """
        动作：设置商品包装基本信息主图2上传
        :param product_pack_product_edit_second_image_upload_input: 商品包装基本信息主图2上传
        :return: 设置'商品包装基本信息主图2上传'文本后的页面
        """
        self.project.clear_and_send_keys(self.product_pack_product_edit_second_image_upload_input, product_pack_product_edit_second_image_upload_input)
        return self.project.get_current_page_source()

    def click_product_pack_product_edit_third_image_button_action(self):
        """
        动作：点击商品包装基本信息主图3
        :return: 点击'商品包装基本信息主图3'按钮后的页面
        """
        self.project.click(self.product_pack_product_edit_third_image_button)
        return self.project.get_current_page_source()

    def set_product_pack_product_edit_third_image_upload_input_action(self, product_pack_product_edit_third_image_upload_input):
        """
        动作：设置商品包装基本信息主图3上传
        :param product_pack_product_edit_third_image_upload_input: 商品包装基本信息主图3上传
        :return: 设置'商品包装基本信息主图3上传'文本后的页面
        """
        self.project.clear_and_send_keys(self.product_pack_product_edit_third_image_upload_input, product_pack_product_edit_third_image_upload_input)
        return self.project.get_current_page_source()

    def click_product_pack_product_edit_fourth_image_button_action(self):
        """
        动作：点击商品包装基本信息主图4
        :return: 点击'商品包装基本信息主图4'按钮后的页面
        """
        self.project.click(self.product_pack_product_edit_fourth_image_button)
        return self.project.get_current_page_source()

    def set_product_pack_product_edit_fourth_image_upload_input_action(self, product_pack_product_edit_fourth_image_upload_input):
        """
        动作：设置商品包装基本信息主图4上传
        :param product_pack_product_edit_fourth_image_upload_input: 商品包装基本信息主图4上传
        :return: 设置'商品包装基本信息主图4上传'文本后的页面
        """
        self.project.clear_and_send_keys(self.product_pack_product_edit_fourth_image_upload_input, product_pack_product_edit_fourth_image_upload_input)
        return self.project.get_current_page_source()

    def click_product_pack_product_edit_fifth_image_button_action(self):
        """
        动作：点击商品包装基本信息主图5
        :return: 点击'商品包装基本信息主图5'按钮后的页面
        """
        self.project.click(self.product_pack_product_edit_fifth_image_button)
        return self.project.get_current_page_source()

    def set_product_pack_product_edit_fifth_image_upload_input_action(self, product_pack_product_edit_fifth_image_upload_input):
        """
        动作：设置商品包装基本信息主图5上传
        :param product_pack_product_edit_fifth_image_upload_input: 商品包装基本信息主图5上传
        :return: 设置'商品包装基本信息主图5上传'文本后的页面
        """
        self.project.clear_and_send_keys(self.product_pack_product_edit_fifth_image_upload_input, product_pack_product_edit_fifth_image_upload_input)
        return self.project.get_current_page_source()

    def click_product_pack_product_edit_video_button_action(self):
        """
        动作：点击商品包装基本信息视频
        :return: 点击'商品包装基本信息视频'按钮后的页面
        """
        self.project.click(self.product_pack_product_edit_video_button)
        return self.project.get_current_page_source()

    def set_product_pack_product_edit_video_upload_input_action(self, product_pack_product_edit_video_upload_input):
        """
        动作：设置商品包装基本信息视频上传
        :param product_pack_product_edit_video_upload_input: 商品包装基本信息视频上传
        :return: 设置'商品包装基本信息视频上传'文本后的页面
        """
        self.project.clear_and_send_keys(self.product_pack_product_edit_video_upload_input, product_pack_product_edit_video_upload_input)
        return self.project.get_current_page_source()

    def click_product_pack_product_edit_feed_image_button_action(self):
        """
        动作：点击商品包装基本信息feed流图片
        :return: 点击'商品包装基本信息feed流图片'按钮后的页面
        """
        self.project.click(self.product_pack_product_edit_feed_image_button)
        return self.project.get_current_page_source()

    def set_product_pack_product_edit_feed_image_upload_input_action(self, product_pack_product_edit_feed_image_upload_input):
        """
        动作：设置商品包装基本信息feed流图片上传
        :param product_pack_product_edit_feed_image_upload_input: 商品包装基本信息feed流图片上传
        :return: 设置'商品包装基本信息feed流图片上传'文本后的页面
        """
        self.project.clear_and_send_keys(self.product_pack_product_edit_feed_image_upload_input, product_pack_product_edit_feed_image_upload_input)
        return self.project.get_current_page_source()

    def click_product_pack_edit_other_ensue_refund_button_action(self):
        """
        动作：点击商品包装其他信息服务保证退款
        :return: 点击'商品包装其他信息服务保证退款'按钮后的页面
        """
        self.project.click(self.product_pack_edit_other_ensue_refund_button)
        return self.project.get_current_page_source()

    def click_product_pack_edit_other_ensue_platform_button_action(self):
        """
        动作：点击商品包装其他信息服务保证平台
        :return: 点击'商品包装其他信息服务保证平台'按钮后的页面
        """
        self.project.click(self.product_pack_edit_other_ensue_platform_button)
        return self.project.get_current_page_source()

    def click_product_pack_edit_other_ensue_service_button_action(self):
        """
        动作：点击商品包装其他信息服务服务流程
        :return: 点击'商品包装其他信息服务服务流程'按钮后的页面
        """
        self.project.click(self.product_pack_edit_other_ensue_service_button)
        return self.project.get_current_page_source()

    def set_product_pack_edit_other_first_question_input_action(self, product_pack_edit_other_first_question_input):
        """
        动作：设置商品包装其他信息服务常见问题1
        :param product_pack_edit_other_first_question_input: 商品包装其他信息服务常见问题1
        :return: 设置'商品包装其他信息服务常见问题1'文本后的页面
        """
        self.project.clear_and_send_keys(self.product_pack_edit_other_first_question_input, product_pack_edit_other_first_question_input)
        return self.project.get_current_page_source()

    def set_product_pack_edit_other_first_question_answer_input_action(self, product_pack_edit_other_first_question_answer_input):
        """
        动作：设置商品包装其他信息服务常见问题1回答
        :param product_pack_edit_other_first_question_answer_input: 商品包装其他信息服务常见问题1回答
        :return: 设置'商品包装其他信息服务常见问题1回答'文本后的页面
        """
        self.project.clear_and_send_keys(self.product_pack_edit_other_first_question_answer_input, product_pack_edit_other_first_question_answer_input)
        return self.project.get_current_page_source()

    def click_product_pack_edit_other_first_question_add_button_action(self):
        """
        动作：点击商品包装其他信息服务常见问题添加
        :return: 点击'商品包装其他信息服务常见问题添加'按钮后的页面
        """
        self.project.click(self.product_pack_edit_other_first_question_add_button)
        return self.project.get_current_page_source()

    def set_product_pack_edit_other_second_question_input_action(self, product_pack_edit_other_second_question_input):
        """
        动作：设置商品包装其他信息服务常见问题2
        :param product_pack_edit_other_second_question_input: 商品包装其他信息服务常见问题2
        :return: 设置'商品包装其他信息服务常见问题2'文本后的页面
        """
        self.project.clear_and_send_keys(self.product_pack_edit_other_second_question_input, product_pack_edit_other_second_question_input)
        return self.project.get_current_page_source()

    def set_product_pack_edit_other_second_question_answer_input_action(self, product_pack_edit_other_second_question_answer_input):
        """
        动作：设置商品包装其他信息服务常见问题2回答
        :param product_pack_edit_other_second_question_answer_input: 商品包装其他信息服务常见问题2回答
        :return: 设置'商品包装其他信息服务常见问题2回答'文本后的页面
        """
        self.project.clear_and_send_keys(self.product_pack_edit_other_second_question_answer_input, product_pack_edit_other_second_question_answer_input)
        return self.project.get_current_page_source()

    def click_product_pack_product_edit_detail_image_button_action(self):
        """
        动作：点击商品包装商品详情详情图
        :return: 点击'商品包装商品详情详情图'按钮后的页面
        """
        self.project.click(self.product_pack_product_edit_detail_image_button)
        return self.project.get_current_page_source()

    def set_product_pack_product_edit_detail_image_upload_input_action(self, product_pack_product_edit_detail_image_upload_input):
        """
        动作：设置商品包装商品详情详情图上传
        :param product_pack_product_edit_detail_image_upload_input: 商品包装商品详情详情图上传
        :return: 设置'商品包装商品详情详情图上传'文本后的页面
        """
        self.project.clear_and_send_keys(self.product_pack_product_edit_detail_image_upload_input, product_pack_product_edit_detail_image_upload_input)
        return self.project.get_current_page_source()

    def click_product_pack_product_edit_contract_button_action(self):
        """
        动作：点击商品包装附件合同
        :return: 点击'商品包装附件合同'按钮后的页面
        """
        self.project.click(self.product_pack_product_edit_contract_button)
        return self.project.get_current_page_source()

    def set_product_pack_product_edit_contract_upload_input_action(self, product_pack_product_edit_contract_upload_input):
        """
        动作：设置商品包装附件合同上传
        :param product_pack_product_edit_contract_upload_input: 商品包装附件合同上传
        :return: 设置'商品包装附件合同上传'文本后的页面
        """
        self.project.clear_and_send_keys(self.product_pack_product_edit_contract_upload_input, product_pack_product_edit_contract_upload_input)
        return self.project.get_current_page_source()

    def click_product_pack_product_edit_prview_button_action(self):
        """
        动作：点击商品包装预览
        :return: 点击'商品包装预览'按钮后的页面
        """
        self.project.click(self.product_pack_product_edit_prview_button)
        return self.project.get_current_page_source()

    def click_product_pack_product_edit_save_button_action(self):
        """
        动作：点击商品包装保存
        :return: 点击'商品包装保存'按钮后的页面
        """
        self.project.click(self.product_pack_product_edit_save_button)
        return self.project.get_current_page_source()

    def click_product_pack_product_edit_submit_button_action(self):
        """
        动作：点击商品包装提交审核
        :return: 点击'商品包装提交审核'按钮后的页面
        """
        self.project.click(self.product_pack_product_edit_submit_button)
        return self.project.get_current_page_source()

    # endregion Actions
