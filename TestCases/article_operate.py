from Core.Decorator import test_case
from Projects.Android.Pages.Common.ArticleDetailPage import ArticleDetailPage
from Projects.Android.Pages.Common.AppCommonDialogPage import AppCommonDialogPage
from Core.Assert import Assert
from Utils.Log import log


@test_case()
def article_operate(*args, **kwargs):
    """
    文章相关操作（评论、收藏、评论点赞等）
    :param args:
    :param kwargs:
    :return:
    """
    project = args[0]  # type: Base
    article_detail_page = ArticleDetailPage(project)
    # 等待搜索结果出现
    project.wait_until(article_detail_page._article_detail_comment_input_tag)
    # 点击评论框
    project.click(article_detail_page.article_detail_comment_input)
    # 输入评论内容
    import time
    content = str(time.time()).replace('.', '')
    article_detail_page.article_detail_comment_input_content.send_keys(content)
    # 点击发送按钮
    article_detail_page.click_article_detail_comment_send_button_action()
    app_common_dialog = AppCommonDialogPage(project)
    # 等待loading对话框消失
    project.wait_until(article_detail_page._article_detail_comment_button_tag)
    # 点击文章评论按钮
    article_detail_page.click_article_detail_comment_button_action()
    # 评论点赞
    zan_xpath = "//*[@text='{}']/preceding-sibling::android.view.View[1]".format(content)
    project.wait_until_not(zan_xpath)
    project.driver.find_element_by_xpath(zan_xpath).click()
    # 等待点赞成功对话框显示
    project.wait_until(article_detail_page._article_detail_collection_button_tag)
    # 点击收藏1次
    article_detail_page.click_article_detail_collection_button_action()
    if project.is_exist_element(app_common_dialog.article_dialog_prompt_describe):
        text = app_common_dialog.article_dialog_prompt_describe.get_attribute('text')
        log(text)
        Assert.is_equal(expected_value=True, actual_value=True, position=' {}'.format(text))
    else:
        Assert.is_equal(expected_value=True, actual_value=False, position=' {}'.format('收藏提示框未显示'))
    # 等待提示框消失
    project.wait_until(article_detail_page._article_detail_collection_button_tag)
    # 点击收藏2次
    article_detail_page.click_article_detail_collection_button_action()
    if project.is_exist_element(app_common_dialog.article_dialog_prompt_describe):
        text = app_common_dialog.article_dialog_prompt_describe.get_attribute('text')
        log(text)
        Assert.is_equal(expected_value=True, actual_value=True, position=' {}'.format(text))
    else:
        Assert.is_equal(expected_value=True, actual_value=False, position=' {}'.format('收藏提示框未显示'))
    # 等待提示框消失
    project.wait_until(article_detail_page._article_detail_like_button_tag)
    # 点赞1次
    article_detail_page.click_article_detail_like_button_action()
    if project.is_exist_element(app_common_dialog.article_dialog_prompt_describe):
        text = app_common_dialog.article_dialog_prompt_describe.get_attribute('text')
        log(text)
        Assert.is_equal(expected_value=True, actual_value=True, position=' {}'.format(text))
    else:
        Assert.is_equal(expected_value=True, actual_value=False, position=' {}'.format('点赞提示框未显示'))
    # 等待提示框消失
    project.wait_until(article_detail_page._article_detail_like_button_tag)
    # 点赞2次
    article_detail_page.click_article_detail_like_button_action()
    if project.is_exist_element(app_common_dialog.article_dialog_prompt_describe):
        text = app_common_dialog.article_dialog_prompt_describe.get_attribute('text')
        log(text)
        Assert.is_equal(expected_value=True, actual_value=True, position=' {}'.format(text))
    else:
        Assert.is_equal(expected_value=True, actual_value=False, position=' {}'.format('点赞提示框未显示'))
