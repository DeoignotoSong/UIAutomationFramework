"""
框架工厂模式
动态执行project
"""
import importlib

from Utils.Log import log


class ProjectFactory:
    @staticmethod
    def get_instance(*args, **kwargs):
        instance = None
        try:
            project = importlib.import_module(
                'Projects.{project}.Base.{project}'.format(project=kwargs['project'])
            )

            instance = eval('project.{}(*args, **kwargs)'.format(kwargs['project']))
        except AttributeError as e:
            log('module name error')
            raise
        except Exception as Me:
            log('Project {} is not existent.'.format(kwargs['project']))
            raise

        return instance

