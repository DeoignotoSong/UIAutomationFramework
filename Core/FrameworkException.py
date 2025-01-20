"""
框架异常
"""


class ValidateException(Exception):
    def __init__(self, expected_value, actual_value, message):
        message += '\n期待值: %s\n实际值: %s' % (
            str(expected_value),
            str(actual_value)
        )
        Exception.__init__(self, message)
        self.expected_value = expected_value
        self.actual_value = actual_value
        self.message = message


class MissStartupKeyException(Exception):
    def __init__(self, parameter_keys):
        Exception.__init__(self, '缺少必填启动参数:{}'.format(str(parameter_keys)))
