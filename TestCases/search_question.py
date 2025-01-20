from Core.Decorator import test_case
from Core.Base import Base
from Projects.Android.Pages.Common.SearchPage import SearchPage
from Projects.Android.Pages.Common.SearchResultPage import SearchResultPage
from Projects.Android.Pages.Common.HomePage import HomePage


@test_case
def search_question(*args, **kwargs):
    """
    综合搜索-搜索问答-进入到问答详情页面
    :param args:
    :param kwargs:
    :return:
    """
    project = args[0]  # type: Base
    home_page = HomePage(project)
    home_page.click_search_bar_button_action()
    search_page = SearchPage(project)
    keywords = kwargs["question_title"]
    project.get_element(value=search_page._search_bar_button_tag).send_keys(keywords)
    # 点击搜索
    search_page.click_search_button_action()
    search_result_page = SearchResultPage(project)
    project.wait_until(search_result_page._search_result_question_button_tag)
    # 点击找问答
    search_result_page.click_search_result_question_button_action()
    project.wait_until(search_result_page._search_result_question_first_item_tag)
    # 点击搜索结果第一条结果
    project.click(search_result_page.search_result_question_first_item)
