from Core.Decorator import test_case
from Projects.Android.Pages.Common.SecurityVerifyPage import SecurityVerifyPage
from appium.webdriver.common.touch_action import TouchAction
from DB.DBFactory import DBFactory
from Core.ConfigOperation import ConfigOperation


@test_case()
def security_verify_operation(*args, **kwargs):
    """
    验证码操作
    :param args:
    :param kwargs:
    :return:
    """
    project = args[0]  # type: Base
    config = ConfigOperation.load_config('Projects/Android_2021/Base/config.ini')
    db = DBFactory.get_db_instances('mysql', config, 'AUTO')
    security_verify_page = SecurityVerifyPage(project)
    project.wait_until(security_verify_page._slider)
    # 通过位置
    distance_x = 0
    location = project.driver.find_element_by_xpath(security_verify_page._slider).location
    x = location['x']
    y = location['y']
    # 取值范围
    to_x = [760, 780, 800]
    # to_x = [1030, 1050, 1170]
    to_y = 1492
    # 验证图片连续失败3次更换一次
    # 尝试3轮
    for i in range(12):
        try:
            action = TouchAction(driver=project.driver)
            action.long_press(el=project.driver.find_element_by_xpath(security_verify_page._slider)).wait(3 * 1000)
            action.move_to(x=to_x[i % 3], y=to_y)
            action.release()
            action.perform()
        except Exception as e:
            print(e)
        if not project.element_is_exist(value=security_verify_page._slider, timeout=1):
            break
    import time
    time.sleep(2)
    data = db.execute_select_sql("SELECT * FROM `dxz_lan`.`dxz_system_sms` ORDER BY created_at desc LIMIT 0,1")
    message = data[0]['message']
    return {
        'message': message
    }
