from Core.Decorator import test_case
from Core.Base import Base
from Projects.Android.Pages.Common.HomePage import HomePage
from Projects.Android.Pages.Common.UserCenterPage import UserCenterPage
from Projects.Android.Pages.Common.OrderMyPage import OrderMyPage
from Projects.Android.Pages.Common.CourseDetailPage import CourseDetailPage
from Core.Assert import Assert


@test_case
def my_order(*args, **kwargs):
    """
    我的订单-课程详情
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
    # 点击我的订单
    user_center_page.click_order_icon_button_action()
    order_my_page = OrderMyPage(project)
    # 点击已完成标签
    order_my_page.click_finished_button_action()
    # 等待搜索结果出现
    project.wait_until(order_my_page._order_goods_name_text_tag)
    course_name = kwargs['course_name']
    title_name_xpath = "//*[@text='{}']".format(course_name)
    project.driver.find_element_by_xpath(title_name_xpath).click()
    course_detail_page = CourseDetailPage(project)
    # 等待搜索结果出现
    project.wait_until(course_detail_page._course_detail_title_text_tag)
    course_detail_title = course_detail_page.course_detail_title_text.get_attribute('text')
    Assert.is_equal(expected_value=course_name, actual_value=course_detail_title)
    back_home_page(project)


def back_home_page(project: Base):
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
