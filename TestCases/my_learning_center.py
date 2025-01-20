from Core.Decorator import test_case
from Core.Base import Base
from Projects.Android.Pages.Common.LearningCenterPage import LearningCenterPage
from Projects.Android.Pages.Common.UserCenterPage import UserCenterPage
from Projects.Android.Pages.Common.CourseLiveDetailPage import CourseLiveDetailPage
from Projects.Android.Pages.Common.HomePage import HomePage
from Core.Assert import Assert


@test_case
def my_learning_center(*args, **kwargs):
    """
    我的学习中心
    :param args:
    :param kwargs:
    :return:
    """
    project = args[0]  # type: Base
    home_page = HomePage(project)
    # 点击我的icon
    home_page.click_footer_nav_my_button_action()
    user_center_page = UserCenterPage(project)
    # 点击学习中心
    user_center_page.click_learning_center_text_button_action()
    course_name = kwargs['course_name']
    learning_center_page = LearningCenterPage(project)
    # 等待搜索结果出现
    project.wait_until(learning_center_page._result_title_page_tag)
    title_elements = project.driver.find_elements_by_xpath(learning_center_page._result_title_page_tag)
    title_map = {}
    for element in title_elements:
        title_map[element.get_attribute('text')] = element
    Assert.is_equal(expected_value=True, actual_value=title_map.__contains__(course_name))
    # 课程学习详情页面
    title_map.get(course_name).click()
    # 进入教室
    course_live_detail_page = CourseLiveDetailPage(project)
    # 等待搜索结果出现
    # project.wait_until(course_live_detail_page._in_class_room_tag)
    # 点击进入教室
    # project.click(course_live_detail_page.in_class_room)
    # 返回MainActivity
    back_main_activity_page(project)


def back_main_activity_page(project: Base):
    """
    递归返回到Main Activity
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
    back_main_activity_page(project)
