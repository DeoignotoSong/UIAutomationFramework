from Utils.Log import log
from poium import Page, Element


'''
手机系统页面
com.jinjilie.daxuezhang.functions.MainActivity
'''


class SystemPage:
    def __init__(self, project):
        self.Android = project
        # region Fields
        # 手机相册第二张照片
        self._picture_second_button_tag = "//*[@resource-id='com.jinjilie.daxuezhang.debug:id/picture_recycler']/android.widget.RelativeLayout[2]/android.widget.LinearLayout"
        # 选择照片-已完成
        self._picture_tv_ok_button_tag = "//*[@resource-id='com.jinjilie.daxuezhang.debug:id/picture_tv_ok']"
        # 选择照片-已完成-裁剪
        self._menu_crop_button_tag = "//*[@resource-id='com.jinjilie.daxuezhang.debug:id/menu_crop']"
        # endregion Fields

    # region Properties
    @property
    def picture_second_button(self):
        """
        属性: 手机相册第二张照片
        :return: 手机相册第二张照片
        """
        element = None
        try:
            element = self.Android.get_element(self._picture_second_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def picture_tv_ok_button(self):
        """
        属性: 选择照片-已完成
        :return: 选择照片-已完成
        """
        element = None
        try:
            element = self.Android.get_element(self._picture_tv_ok_button_tag)
        except AttributeError as error:
            log(error)
        return element

    @property
    def menu_crop_button(self):
        """
        属性: 选择照片-已完成-裁剪
        :return: 选择照片-已完成-裁剪
        """
        element = None
        try:
            element = self.Android.get_element(self._menu_crop_button_tag)
        except AttributeError as error:
            log(error)
        return element

    # endregion Properties

    # region Actions
    def click_picture_second_button_action(self):
        """
        动作：点击手机相册第二张照片
        :return: 点击'手机相册第二张照片'按钮后的页面
        """
        self.Android.click(self.picture_second_button)
        return self.Android.get_current_page_source()

    def click_picture_tv_ok_button_action(self):
        """
        动作：点击选择照片-已完成
        :return: 点击'选择照片-已完成'按钮后的页面
        """
        self.Android.click(self.picture_tv_ok_button)
        return self.Android.get_current_page_source()

    def click_menu_crop_button_action(self):
        """
        动作：点击选择照片-已完成-裁剪
        :return: 点击'选择照片-已完成-裁剪'按钮后的页面
        """
        self.Android.click(self.menu_crop_button)
        return self.Android.get_current_page_source()

    # endregion Actions
