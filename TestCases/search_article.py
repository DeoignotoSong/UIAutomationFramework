from Core.Decorator import test_case
from Projects.Android.Pages.Common.SearchPage import SearchPage
from Projects.Android.Pages.Common.SearchResultPage import SearchResultPage
from Projects.Android.Pages.Common.HomePage import HomePage
from Projects.Android.Pages.Common.ArticleDetailPage import ArticleDetailPage


@test_case()
def search_article(*args, **kwargs):
    """
    综合搜索-搜索文章
    :param args:
    :param kwargs:
    :return:
    """
    project = args[0]  # type: Base
    home_page = HomePage(project)
    home_page.click_search_bar_button_action()
    search_page = SearchPage(project)
    keywords = kwargs["search_content"]
    # project.get_element(value=search_page._search_bar_button_tag).send_keys(keywords)
    project.driver.find_element_by_xpath(xpath=search_page._search_bar_button_tag).send_keys(keywords)
    # 点击搜索
    search_page.click_search_button_action()
    search_result_page = SearchResultPage(project)
    search_result_page.click_search_result_article_button_action()
    # 等待搜索结果出现
    project.wait_until(search_result_page._search_result_title_text_tag)
    articles = project.driver.find_elements_by_xpath(search_result_page._search_result_title_text_tag)
    # 点击第一条结果
    articles[0].click()
    article_detail_page = ArticleDetailPage(project)
    # 等待搜索结果出现
    project.wait_until(article_detail_page._article_detail_right_option_button_tag)
