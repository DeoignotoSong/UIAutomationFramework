from Utils.Log import log

"""
后台-留学中心-留学审核管理-服务审核
http://console.dxzjjl.net.cn/abroad_center/service_audit/show/SP020101002844
"""

class ConsoleAbroadCenterServiceAuditShowPage:
    def __init__(self, project):
        self.project = project
        self.url = 'http://console.dxzjjl.net.cn/abroad_center/service_audit'
        # region Fields
        # 消息提示
        self._message_content_text_tag = '/html/body/div[last()]/div/div[1]/p'
        # 服务名称
        self._audit_service_name_text_tag = '/html/body/div[1]/div/section/main/div/div[2]/div[2]/div/section[1]/form/div[1]/div/span'
        # 服务已选一级类目
        self._audit_service_first_category_text_tag = '/html/body/div[1]/div/section/main/div/div[2]/div[2]/div/section[2]/div/div/div/div[3]/table/tbody/tr/td[1]/div'
        # 服务已选二级类目
        self._audit_service_second_category_text_tag = '/html/body/div[1]/div/section/main/div/div[2]/div[2]/div/section[2]/div/div/div/div[3]/table/tbody/tr/td[2]/div'
        # 服务已选三级类目
        self._audit_service_third_category_text_tag = '/html/body/div[1]/div/section/main/div/div[2]/div[2]/div/section[2]/div/div/div/div[3]/table/tbody/tr/td[3]/div'
        # 服务已选数量
        self._audit_service_number_text_tag = '/html/body/div[1]/div/section/main/div/div[2]/div[2]/div/section[2]/div/div/div/div[3]/table/tbody/tr/td[4]/div'
        # 审核结果
        self._audit_service_result_text_tag = '/html/body/div[1]/div/section/main/div/div[4]/div[2]/div/div/div[3]/table/tbody/tr/td[3]/div'
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
    def audit_service_name_text(self):
        """
        属性: 服务名称
        :return: 服务名称
        """
        element = None
        try:
            element = self.project.get_element(self._audit_service_name_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def audit_service_first_category_text(self):
        """
        属性: 服务已选一级类目
        :return: 服务已选一级类目
        """
        element = None
        try:
            element = self.project.get_element(self._audit_service_first_category_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def audit_service_second_category_text(self):
        """
        属性: 服务已选二级类目
        :return: 服务已选二级类目
        """
        element = None
        try:
            element = self.project.get_element(self._audit_service_second_category_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def audit_service_third_category_text(self):
        """
        属性: 服务已选三级类目
        :return: 服务已选三级类目
        """
        element = None
        try:
            element = self.project.get_element(self._audit_service_third_category_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def audit_service_number_text(self):
        """
        属性: 服务已选数量
        :return: 服务已选数量
        """
        element = None
        try:
            element = self.project.get_element(self._audit_service_number_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def audit_service_result_text(self):
        """
        属性: 审核结果
        :return: 审核结果
        """
        element = None
        try:
            element = self.project.get_element(self._audit_service_result_text_tag)
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

    def get_audit_service_name_text_action(self):
        """
        动作：获取服务名称的文本
        :return: '服务名称'的文本
        """
        control_content = self.project.get_element_text(self.audit_service_name_text)
        return control_content

    def get_audit_service_first_category_text_action(self):
        """
        动作：获取服务已选一级类目的文本
        :return: '服务已选一级类目'的文本
        """
        control_content = self.project.get_element_text(self.audit_service_first_category_text)
        return control_content

    def get_audit_service_second_category_text_action(self):
        """
        动作：获取服务已选二级类目的文本
        :return: '服务已选二级类目'的文本
        """
        control_content = self.project.get_element_text(self.audit_service_second_category_text)
        return control_content

    def get_audit_service_third_category_text_action(self):
        """
        动作：获取服务已选三级类目的文本
        :return: '服务已选三级类目'的文本
        """
        control_content = self.project.get_element_text(self.audit_service_third_category_text)
        return control_content

    def get_audit_service_number_text_action(self):
        """
        动作：获取服务已选数量的文本
        :return: '服务已选数量'的文本
        """
        control_content = self.project.get_element_text(self.audit_service_number_text)
        return control_content

    def get_audit_service_result_text_action(self):
        """
        动作：获取审核结果的文本
        :return: '审核结果'的文本
        """
        control_content = self.project.get_element_text(self.audit_service_result_text)
        return control_content

    # endregion Actions
