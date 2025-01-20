from Core.Decorator import test_case
from Core.Base import Base
from Projects.Android.Pages.Common.ArticleDetailPage import ArticleDetailPage
from Projects.Android.Pages.Common.AppCommonDialogPage import AppCommonDialogPage
from ..TestCases.search_article import search_article


@test_case
def search_article_share(*args, **kwargs):
    """
    综合搜索-搜索文章-分享
    :param args:
    :param kwargs:
    :return:
    """
    project = args[0]  # type: Base
    # 搜索文章
    search_article(*args, **kwargs)
    article_detail_page = ArticleDetailPage(project)
    # 点击右上角option
    article_detail_page.click_article_detail_right_option_button_action()
    project.wait_until(article_detail_page._recent_charts_button_tag)
    # 点击分享默认最近的第一个好友
    article_detail_page.click_recent_charts_button_action()
    app_common_dialog = AppCommonDialogPage(project)
    # 等待元素出现
    project.wait_until(app_common_dialog._shared_send_button_tag)
    # 点击发送按钮
    app_common_dialog.click_shared_send_button_action()
