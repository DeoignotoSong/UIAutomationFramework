from Core.Decorator import test_case
from Projects.Android.Pages.Common.LocationPage import LocationPage
from Projects.Android.Pages.Common.HomePage import HomePage


@test_case()
def set_city_location(*args, **kwargs):
    """
    设置城市位置
    :param args:
    :param kwargs:
    :return:
    """
    project = args[0]  # type: Base
    home_page = HomePage(project)
    home_page.click_city_address_button_action()
    city = '北京市'
    set_city(project, city)
    home_page.click_city_address_button_action()
    changed_city = '大连市'
    set_city(project, changed_city)


def set_city(project, city):
    """
    设置城市
    :param project:
    :param city:
    :return:
    """
    location_page = LocationPage(project)
    location_page.click_search_bar_button_action()
    project.get_element(value=location_page._search_bar_button_tag).send_keys(city)
    if project.element_is_exist(location_page._search_result_first_element_tag):
        project.click(location_page.search_result_first_element)
