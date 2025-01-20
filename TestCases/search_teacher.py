from Core.Decorator import test_case
from Core.Base import Base
from Projects.Android.Pages.Common.SearchPage import SearchPage
from Projects.Android.Pages.Common.SearchResultPage import SearchResultPage
from Projects.Android.Pages.Common.HomePage import HomePage


@test_case
def search_teacher(*args, **kwargs):
    """
    综合搜索-搜索老师
    :param args:
    :param kwargs:
    :return:
    """
    project = args[0]  # type: Base
    home_page = HomePage(project)
    home_page.click_search_bar_button_action()
    search_page = SearchPage(project)
    keywords = kwargs["lecturer_name"]
    project.get_element(value=search_page._search_bar_button_tag).send_keys(keywords)
    # 点击搜索
    search_page.click_search_button_action()
    search_result_page = SearchResultPage(project)
    # 点击找问答
    search_result_page.click_search_result_lecture_button_action()
    # 点击找学校
    search_result_page.click_search_result_college_button_action()
    # 点击找老师
    search_result_page.click_search_result_teacher_button_action()
    project.wait_until(search_result_page._search_result_teacher_first_item_tag)
    # 点击搜索结果第一条结果
    project.click(search_result_page.search_result_teacher_first_item)
