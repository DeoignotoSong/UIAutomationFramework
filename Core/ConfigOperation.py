# -*- encoding: utf-8 -*-
from configparser import ConfigParser


class ConfigOperation(object):
    @staticmethod
    def load_config(config_path):
        config_file = ConfigParser()
        config_file.read(config_path, 'utf-8')

        return config_file
