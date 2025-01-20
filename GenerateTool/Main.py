from Projects.PC.GenerateTool.PageScriptAutoGenerator import PageScriptAutoGenerator
import os

# 项目名称
project = 'project'
# 项目Pages根路径
pages_path = './Projects/PC/Pages'
# Generate Pages 根路径
generator_source_path = './Projects/PC/GenerateTool/GeneratedPages/'


def build_pages(file_dir):
    """
    页面文件生成
    :param file_dir:
    :return:
    """
    file_list = os.listdir(file_dir)
    for filename in file_list:
        file_path = os.path.join(file_dir, filename)
        generator_path = generator_source_path + str(file_path.split('/')[-1])
        # 如果是文件夹就进行递归
        if os.path.isdir(file_path):
            if not os.path.exists(generator_path):
                os.makedirs(generator_path)
            build_pages(file_path)
        # 如果是py文件就进行生成器生成
        if file_path[-3:].upper() == '.PY':
            print(file_path)
            generator = PageScriptAutoGenerator(project, file_path)
            generator.generate_page_file(generator_path)


def set_execute_path():
    """
    设置文件工作路径
    :return:
    """
    current_file_path = os.path.realpath(__file__)
    execute_path = current_file_path.split('\\Projects')[0]
    os.chdir(execute_path)


if __name__ == '__main__':
    set_execute_path()
    build_pages(pages_path)
