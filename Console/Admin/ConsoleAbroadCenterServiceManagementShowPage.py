from Utils.Log import log

"""
后台-留学中心-商品服务管理-服务管理-一条服务
console_url/advert/advert-add/add/0
"""

class ConsoleAbroadCenterServiceManagementShowPage:
    def __init__(self, project):
        self.project = project
        self.url = 'http://console.dxzjjl.net.cn/abroad_center/service_management/show/SP020101002925'
        # region Fields
        # 消息提示
        self._message_content_text_tag = '/html/body/div[last()]/div/div[1]/p'
        # 服务名称
        self._service_name_text_tag = '/html/body/div[1]/div/section/main/div/div[2]/div[2]/div/section[2]/form/div[1]/div/span'
        # 审核结果
        self._service_audit_state_text_tag = '/html/body/div[1]/div/section/main/div/div[3]/div[2]/div/div/div[3]/table/tbody/tr/td[3]/div'
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
    def service_name_text(self):
        """
        属性: 服务名称
        :return: 服务名称
        """
        element = None
        try:
            element = self.project.get_element(self._service_name_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def service_audit_state_text(self):
        """
        属性: 审核结果
        :return: 审核结果
        """
        element = None
        try:
            element = self.project.get_element(self._service_audit_state_text_tag)
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

    def get_service_name_text_action(self):
        """
        动作：获取服务名称的文本
        :return: '服务名称'的文本
        """
        control_content = self.project.get_element_text(self.service_name_text)
        return control_content

    def get_service_audit_state_text_action(self):
        """
        动作：获取审核结果的文本
        :return: '审核结果'的文本
        """
        control_content = self.project.get_element_text(self.service_audit_state_text)
        return control_content

    # endregion Actions
