import os


class ProjectGenerator(object):
    @staticmethod
    def generator(project_name, whether_cover_existing_project=False):
        """
        初始化项目文件夹及基础文件
        :param project_name: 需要初始化的项目名称
        :param whether_cover_existing_project: 如果项目存在，是否要覆盖原有项目:
                                                True: 删除已经存在的该项目（使用TRUE需谨慎，删除操作会删除Projects目录下，
                                                      project_name目录及目录下的所有内容）
                                                False: 不删除已经存在的该项目
        """
        project_path = '../../Projects/'
        if whether_cover_existing_project:
            try:
                os.removedirs(project_path + project_name)
            except FileNotFoundError as error:
                print(str(error))
                print('No this projects.')

        if not os.path.exists(project_path + project_name):
            os.mkdir(project_path + project_name)

        if not os.path.exists(project_path + project_name + '/Base'):
            os.mkdir(project_path + project_name + '/Base')

        if not os.path.exists(project_path + project_name + '/GenerateTool'):
            os.mkdir(project_path + project_name + '/GenerateTool')

        if not os.path.exists(project_path + project_name + '/Pages'):
            os.mkdir(project_path + project_name + '/Pages')

        if not os.path.exists(project_path + project_name + '/TestCases'):
            os.mkdir(project_path + project_name + '/TestCases')

        if not os.path.exists(project_path + project_name + '/TestScenario'):
            os.mkdir(project_path + project_name + '/TestScenario')

        if not os.path.exists(project_path + project_name + '/TestReport'):
            os.mkdir(project_path + project_name + '/TestReport')

        if not os.path.exists(project_path + project_name + '/Base/' + project_name + '.py'):
            with open(project_path + project_name + '/Base/' + project_name + '.py', 'w') as base_file:
                with open('./FileTemplates/BaseTemplate', 'r') as base_template:
                    for template_content in base_template:
                        base_file.write(template_content.replace('{project}', project_name))

        if not os.path.exists(project_path + project_name + '/Base/config.ini'):
            with open(project_path + project_name + '/Base/config.ini', 'w') as base_file:
                with open('./FileTemplates/ConfigTemplate', 'r') as base_template:
                    for template_content in base_template:
                        base_file.write(template_content.replace('{project}', project_name))


generator = ProjectGenerator()
generator.generator('FrameworkDemo', True)
