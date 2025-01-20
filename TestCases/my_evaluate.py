from Core.Decorator import test_case
from Core.Base import Base
from Projects.Android.Pages.Common.EvaluatePage import EvaluatePage
from Projects.Android.Pages.Common.UserCenterPage import UserCenterPage
from Projects.Android.Pages.Common.EvaluateWriteSuccessPage import EvaluateWriteSuccessPage
from Projects.Android.Pages.Common.EvaluateWritePage import EvaluateWritePage
from Projects.Android.Pages.Common.HomePage import HomePage
from Core.Assert import Assert


@test_case
def my_evaluate(*args, **kwargs):
    """
    我的评价
    :param args:
    :param kwargs:
    :return:
    """
    project = args[0]  # type: Base
    home_page = HomePage(project)
    # 点击我的icon
    home_page.click_footer_nav_my_button_action()
    user_center_page = UserCenterPage(project)
    # 点击我的评价
    user_center_page.click_evaluate_icon_button_action()
    course_name = kwargs['course_name']
    evaluate_page = EvaluatePage(project)
    # 页面校验
    page_title = evaluate_page.title.get_attribute('text')
    Assert.is_equal(expected_value='我的评价', actual_value=page_title)
    # 等待页面元素展示
    project.wait_until(evaluate_page._title_tag)
    title_elements = project.driver.find_elements_by_xpath(evaluate_page._title_tag)
    item_index = 0
    for element in title_elements:
        if element.get_attribute('text') == course_name:
            break
        item_index += 1
    # 等待页面元素展示
    project.wait_until(evaluate_page._evaluate_write_tag)
    evaluate_writes = project.driver.find_elements_by_xpath(evaluate_page._evaluate_write_tag)
    # 点击评价
    evaluate_writes[item_index].click()
    evaluate_write = EvaluateWritePage(project)
    # 等待搜索结果出现
    project.wait_until(evaluate_write._evaluate_user_rating_button_tag)
    # 用户5星
    evaluate_write.click_evaluate_user_rating_button_action()
    # 课程5星
    evaluate_write.click_evaluate_course_rating_button_action()
    # 填写评价内容
    import time
    content = str(time.time()).replace('.', '')
    evaluate_write.write_evaluate.send_keys(content)
    # 提交
    project.click(evaluate_write.evaluate_write)
    evaluate_write_success = EvaluateWriteSuccessPage(project)
    # 等待搜索结果出现
    project.wait_until(evaluate_write_success._title_tag)
    actual_title = evaluate_write_success.title.get_attribute('text')
    Assert.is_equal(expected_value='评价成功', actual_value=actual_title)
    # 返回前一页
    evaluate_write_success.click_back_button_action()
    # 点击已评价
    evaluate_page.click_evaluatelist_also_text_button_action()
    # 等待搜索结果出现
    project.wait_until(evaluate_page._title_tag)
    evaluate_xpath = '//*[@text="{}"]'.format(content)
    is_exist = project.element_is_exist(evaluate_xpath)
    Assert.is_equal(expected_value=True, actual_value=is_exist)
