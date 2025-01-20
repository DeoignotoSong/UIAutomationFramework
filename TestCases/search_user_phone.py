from Core.Decorator import test_case
from Projects.Android.Pages.Common.WechatHomePage import WechatHomePage
from Projects.Android.Pages.Common.WechatAdressBookPage import WechatAdressBookPage
from Projects.Android.Pages.Common.HomePage import HomePage
from Projects.Android.Pages.Common.WechatAddUserPage import WechatAddUserPage


@test_case()
def search_user_phone(*args, **kwargs):
    """
    综合搜索-搜索问答-进入到问答详情页面
    :param args:
    :param kwargs:
    :return:
    """
    project = args[0]  # type: Base
    home_page = HomePage(project)
    # 点击微聊
    home_page.click_footer_nav_chat_button_action()
    wechat_home = WechatHomePage(project)
    # 展示好友列表
    wechat_home.click_header_right_book_button_action()
    wechat_address_book = WechatAdressBookPage(project)
    # 点击添加学友
    wechat_address_book.click_add_user_icon_button_action()
    # 输入学友电话号
    wechat_add_user = WechatAddUserPage(project)
    user_phone = kwargs['user_phone']
    wechat_add_user.search_edit.send_keys(user_phone)
    # 点击搜索号码
    project.click(wechat_add_user.search_text)
