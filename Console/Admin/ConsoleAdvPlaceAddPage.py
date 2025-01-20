from Utils.Log import log

"""
后台-运营中心-广告位管理-添加广告位页面
console_url/advert/advert-space-add/add/0
"""

class ConsoleAdvPlaceAddPage:
    def __init__(self, project):
        self.project = project
        self.url = 'console_url/advert/advert-space-add/add/0'
        # region Fields
        # 消息提示
        self._message_content_text_tag = '/html/body/div[last()]/div/div[1]/p'
        # 禁用确认提示框
        self._message_dialog_content_text_tag = '/html/body/div[2]/div/div[2]/div[1]/div[2]/p'
        # 基础信息-广告位名称
        self._add_advert_name_input_tag = '//*[@id="app"]/div/section/main/div/div[2]/form/div[1]/div[2]/div/div[1]/div/div/div/input'
        # 默认广告设置-广告位类型
        self._add_advert_type_tag = '//*[@id="app"]/div/section/main/div/div[2]/form/div[2]/div[2]/div[1]/div[1]/div/div/div/div/input'
        # 默认广告设置-广告位类型-列表
        self._add_advert_type_lsit_tag = '/html/body/div[2]/div[1]/div[1]/ul/li[2]'
        # 默认广告设置-广告图片尺寸
        self._add_advert_size_show_input_tag = '//*[@id="app"]/div/section/main/div/div[2]/form/div[2]/div[2]/div[1]/div[3]/div/div/div/input'
        # 默认广告设置-删除按钮
        self._add_advert_delete_button_tag = '//*[@id="app"]/div/section/main/div/div[2]/form/div[2]/div[2]/div[3]/div[4]/button'
        # 广告位模板-模板URL
        self._add_advert_template_url_input_tag = '//*[@id="app"]/div/section/main/div/div[2]/form/div[3]/div[2]/div/div[1]/div[1]/div/div/input'
        # 广告位末班-bannerID
        self._add_advert_bannerid_input_tag = '//*[@id="app"]/div/section/main/div/div[2]/form/div[3]/div[2]/div/div[1]/div[2]/div/div/input'
        # 提交按钮
        self._add_advert_submit_button_tag = '//*[@id="app"]/div/section/main/div/div[2]/form/div[4]/button/span'
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
    def message_dialog_content_text(self):
        """
        属性: 禁用确认提示框
        :return: 禁用确认提示框
        """
        element = None
        try:
            element = self.project.get_element(self._message_dialog_content_text_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def add_advert_name_input(self):
        """
        属性: 基础信息-广告位名称
        :return: 基础信息-广告位名称
        """
        element = None
        try:
            element = self.project.get_element(self._add_advert_name_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def add_advert_type(self):
        """
        属性: 默认广告设置-广告位类型
        :return: 默认广告设置-广告位类型
        """
        element = None
        try:
            element = self.project.get_element(self._add_advert_type_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def add_advert_type_lsit(self):
        """
        属性: 默认广告设置-广告位类型-列表
        :return: 默认广告设置-广告位类型-列表
        """
        element = None
        try:
            element = self.project.get_element(self._add_advert_type_lsit_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def add_advert_size_show_input(self):
        """
        属性: 默认广告设置-广告图片尺寸
        :return: 默认广告设置-广告图片尺寸
        """
        element = None
        try:
            element = self.project.get_element(self._add_advert_size_show_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def add_advert_delete_button(self):
        """
        属性: 默认广告设置-删除按钮
        :return: 默认广告设置-删除按钮
        """
        element = None
        try:
            element = self.project.get_element(self._add_advert_delete_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def add_advert_template_url_input(self):
        """
        属性: 广告位模板-模板URL
        :return: 广告位模板-模板URL
        """
        element = None
        try:
            element = self.project.get_element(self._add_advert_template_url_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def add_advert_bannerid_input(self):
        """
        属性: 广告位末班-bannerID
        :return: 广告位末班-bannerID
        """
        element = None
        try:
            element = self.project.get_element(self._add_advert_bannerid_input_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def add_advert_submit_button(self):
        """
        属性: 提交按钮
        :return: 提交按钮
        """
        element = None
        try:
            element = self.project.get_element(self._add_advert_submit_button_tag)
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

    def get_message_dialog_content_text_action(self):
        """
        动作：获取禁用确认提示框的文本
        :return: '禁用确认提示框'的文本
        """
        control_content = self.project.get_element_text(self.message_dialog_content_text)
        return control_content

    def set_add_advert_name_input_action(self, add_advert_name_input):
        """
        动作：设置基础信息-广告位名称
        :param add_advert_name_input: 基础信息-广告位名称
        :return: 设置'基础信息-广告位名称'文本后的页面
        """
        self.project.clear_and_send_keys(self.add_advert_name_input, add_advert_name_input)
        return self.project.get_current_page_source()

    def set_add_advert_size_show_input_action(self, add_advert_size_show_input):
        """
        动作：设置默认广告设置-广告图片尺寸
        :param add_advert_size_show_input: 默认广告设置-广告图片尺寸
        :return: 设置'默认广告设置-广告图片尺寸'文本后的页面
        """
        self.project.clear_and_send_keys(self.add_advert_size_show_input, add_advert_size_show_input)
        return self.project.get_current_page_source()

    def click_add_advert_delete_button_action(self):
        """
        动作：点击默认广告设置-删除按钮
        :return: 点击'默认广告设置-删除按钮'按钮后的页面
        """
        self.project.click(self.add_advert_delete_button)
        return self.project.get_current_page_source()

    def set_add_advert_template_url_input_action(self, add_advert_template_url_input):
        """
        动作：设置广告位模板-模板URL
        :param add_advert_template_url_input: 广告位模板-模板URL
        :return: 设置'广告位模板-模板URL'文本后的页面
        """
        self.project.clear_and_send_keys(self.add_advert_template_url_input, add_advert_template_url_input)
        return self.project.get_current_page_source()

    def set_add_advert_bannerid_input_action(self, add_advert_bannerid_input):
        """
        动作：设置广告位末班-bannerID
        :param add_advert_bannerid_input: 广告位末班-bannerID
        :return: 设置'广告位末班-bannerID'文本后的页面
        """
        self.project.clear_and_send_keys(self.add_advert_bannerid_input, add_advert_bannerid_input)
        return self.project.get_current_page_source()

    def click_add_advert_submit_button_action(self):
        """
        动作：点击提交按钮
        :return: 点击'提交按钮'按钮后的页面
        """
        self.project.click(self.add_advert_submit_button)
        return self.project.get_current_page_source()

    # endregion Actions
