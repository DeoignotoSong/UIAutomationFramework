from Core.Decorator import test_case
from Core.Base import Base
from Projects.Android.Pages.Common.HomePage import HomePage
from Projects.Android.Pages.Common.WechatInnerPage import WechatInnerPage
from Projects.Android.Pages.Common.WechatPersonalDetailPage import WechatPersonalDetailPage
from Projects.Android.Pages.Common.UserHomePage import UserHomePage
from Projects.Android.Pages.Common.WechatHomePage import WechatHomePage
from Projects.Android.Pages.Common.WechatSessionInformationPage import WechatSessionInformationPage
from ..TestCases.search_article_share import search_article_share
from ..TestCases.search_course_share import search_course_share


@test_case
def user_homepage_attention_wechat(*args, **kwargs):
    """
    普通用户主页-关注-微聊
    :param args:
    :param kwargs:
    :return:
    """
    project = args[0]  # type: Base
    home_page = HomePage(project)
    # 点击微聊
    home_page.click_footer_nav_chat_button_action()
    nick = kwargs['nick']
    wechat_icon = "//*[@text='{}']".format(nick)
    # 点击指定微聊内容
    project.driver.find_element_by_xpath(wechat_icon).click()
    wechat_inner_page = WechatInnerPage(project)
    project.wait_until(wechat_inner_page._header_right_button_tag)
    # 点击右上角option
    wechat_inner_page.click_header_right_button_action()
    wechat_session_information = WechatSessionInformationPage(project)
    # 点击好友头像
    wechat_session_information.click_charts_icon_button_action()
    wechat_personal_detail_page = WechatPersonalDetailPage(project)
    # 点击个人主页
    wechat_personal_detail_page.click_homepage_button_action()
    import time
    time.sleep(5)
    user_home = UserHomePage(project)
    # 点击关注
    user_home.click_user_focus_button_action()
    # 点击微聊
    user_home.click_user_chat_button_action()
    wechat_content = str(time.time()).replace('.', '')
    wechat_inner_page.chat_fragment_input.send_keys(wechat_content)
    # 点击发送按钮
    wechat_inner_page.click_send_button_action()
    # 返回微聊首页
    back_wechat_home_page(project)
    wechat_home = WechatHomePage(project)
    # 展示好友列表
    wechat_home.click_header_right_book_button_action()
    back_wechat_home_page(project)
    search_content = '测试'
    kwargs['search_content'] = search_content
    # 点击home首页
    home_page.click_footer_nav_home_button_action()
    search_article_share(*args, **kwargs)
    back_wechat_home_page(project)
    search_course_share(*args, **kwargs)


def back_wechat_home_page(project: Base):
    """
    递归返回到微聊首页
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
    back_wechat_home_page(project)

