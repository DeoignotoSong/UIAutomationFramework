from Core.Decorator import test_case
from Core.Base import Base
from Projects.Android.Pages.Common.HomePage import HomePage
from Projects.Android.Pages.Common.WechatInnerPage import WechatInnerPage
from Projects.Android.Pages.Common.WechatPersonalDetailPage import WechatPersonalDetailPage
from Projects.Android.Pages.Common.LecturerHomePage import LecturerHomePage
from ..TestCases.search_user_phone import search_user_phone


@test_case
def tearcher_homepage_attention_wechat(*args, **kwargs):
    """
    讲师主页-关注-微聊
    :param args:
    :param kwargs:
    :return:
    """
    project = args[0]  # type: Base
    home_page = HomePage(project)
    # 点击微聊
    home_page.click_footer_nav_chat_button_action()
    # nick = '耿裕明'
    # wechat_icon = "//*[@text='{}']".format(nick)
    user_phone = '18229112116'
    kwargs['user_phone'] = user_phone
    # 搜索指定用户电话
    search_user_phone(*args, **kwargs)

    # # 点击指定微聊内容
    # project.driver.find_element_by_xpath(wechat_icon).click()
    wechat_inner_page = WechatInnerPage(project)
    # project.wait_until(wechat_inner_page._header_right_button_tag)
    # # 点击右上角option
    # wechat_inner_page.click_header_right_button_action()
    # wechat_session_information = WechatSessionInformationPage(project)
    # # 点击好友头像
    # wechat_session_information.click_charts_icon_button_action()
    wechat_personal_detail_page = WechatPersonalDetailPage(project)
    project.wait_until(wechat_personal_detail_page._homepage_button_tag)
    # 点击个人主页
    wechat_personal_detail_page.click_homepage_button_action()
    import time
    time.sleep(5)
    lecturer_home = LecturerHomePage(project)
    # 点击关注
    lecturer_home.click_add_follow_button_action()
    # 点击微聊
    lecturer_home.click_wechat_button_action()
    wechat_content = str(time.time()).replace('.', '')
    wechat_inner_page.chat_fragment_input.send_keys(wechat_content)
    # 点击发送按钮
    wechat_inner_page.click_send_button_action()
