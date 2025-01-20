from Core.Decorator import test_case
from Projects.Android.Pages.Common.UserCenterPage import UserCenterPage
from Projects.Android.Pages.Common.AppSettingPage import AppSettingPage
from Projects.Android.Pages.Common.AppCommonDialogPage import AppCommonDialogPage
from Projects.Android.Pages.Common.HomePage import HomePage
from appium.webdriver.common.touch_action import TouchAction


@test_case()
def if_login_then_user_logout(*args, **kwargs):
    """
    如果登录,则退出
    :param args:
    :param kwargs:
    :return:
    """
    project = args[0]  # type: Base
    back_home_page(project)
    home_page = HomePage(project)
    # 点击我的icon
    home_page.click_footer_nav_my_button_action()
    user_center_page = UserCenterPage(project)
    login_name = user_center_page.login_username_text.get_attribute('text')
    if login_name == '登录/注册':
        return
    try:
        # 点击设置icon
        user_center_page.click_setting_icon_button_action()
    except Exception as e:
        print("向上滑动页面")
        TouchAction(project.driver).long_press(x=550, y=1500).move_to(x=550, y=350).release().perform()
        # 点击设置icon
        user_center_page.click_setting_icon_button_action()
    app_setting_page = AppSettingPage(project)
    # 点击退出登录
    app_setting_page.click_logout_button_action()
    app_common_dialog = AppCommonDialogPage(project)
    # 确认对话框-点击狠心离开
    app_common_dialog.click_logout_closed_button_action()
    # 等待loading对话框消失
    project.wait_until_not(app_common_dialog._loading_tag)


def back_home_page(project):
    """
    递归返回到Home首页
    :param project:
    :return:
    """
    home_activity = 'com.jinjilie.daxuezhang.functions.MainActivity'
    print(project.driver.current_activity)
    if project.driver.current_activity == home_activity:
        return True
    # 返回前一页
    project.driver.press_keycode(keycode=4)
    import time
    time.sleep(1)
    back_home_page(project)
