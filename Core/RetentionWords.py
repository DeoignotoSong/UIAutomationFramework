from Core.Global import PrepareData
from Core.Global import Data
import re
import datetime
import random
import time
from Utils.Log import log
import threading


class RetentionWords:

    def replace_value_for_special_quote(self, scenario_name, input_str):
        """

        :rtype: object
        """
        output_str = input_str

        now = datetime.datetime.now()

        output_str = self._replace_value_from_config_prepare(output_str)

        output_str = self._special_quote_convert(scenario_name, output_str)

        output_str = self._replace_env_url(output_str)

        output_str = self._get_date(output_str, now)

        output_str = self._get_datetime(output_str)

        output_str = self._replace_time_stamp(output_str, now)

        output_str = self._get_datetime_by_now(output_str, now)

        output_str = self._get_rd_date(output_str, now)

        output_str = self._get_random(output_str)

        return output_str

    # 替换.$In/.$Out.$Expect.$value
    @staticmethod
    def _special_quote_convert(scenario_name, input_str):

        all_replace_strings = re.findall(r'\.\$\w.+\.\$In(?:\.\$\w+)+|'
                                         r'\.\$\w.+\.\$Out(?:\.\$\w+)+|'
                                         r'\.\$\w.+\.\$Expect(?:\.\$\w+)+',
                                         input_str)

        all_replace_strings.sort(key=lambda i: len(i), reverse=True)

        if len(all_replace_strings) > 0:
            # 遍历所有符合正则表达式的字符串
            for replace_string in all_replace_strings:
                # 按.$分割引用参数
                items = replace_string.split('.$')

                # 动态生成实际值的
                actual_value_str = "Data.TEST_DATA['" + scenario_name + "'][items[1]]"

                for index in range(2, len(items)):
                    if items[index].isdigit():
                        temp_str = '[int(items[' + str(index) + '])]'
                    else:
                        temp_str = '[items[' + str(index) + ']]'

                    actual_value_str += temp_str
                input_str = input_str.replace(str(replace_string), str(eval(actual_value_str)))

        return input_str

    # 替换.$config.$prepare_data
    @staticmethod
    def _replace_value_from_config_prepare(input_str):

        replace_config_strings = re.findall(r'\.\$config\.\$\w+',
                                            input_str)

        # 从config文件里获取需要替换的值
        if len(replace_config_strings) > 0:
            for replace_config_string in replace_config_strings:
                config_name = replace_config_string.replace('.$config.$', '')
                replace_string = None
                # 判断字段是否在
                if config_name in PrepareData.PREPARE_DATA.keys():
                    if len(PrepareData.PREPARE_DATA[config_name]) > 1:
                        # Get preparing data in scenario taken dict
                        replace_string = PrepareData.PREPARE_DATA[config_name].pop(0)
                        # 待优化，有重复代码！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！
                        if threading.current_thread().ident in PrepareData.USING_DATA.keys():
                            if config_name in PrepareData.USING_DATA[threading.current_thread().ident].keys():
                                PrepareData.USING_DATA[threading.current_thread().ident][config_name].append(
                                    replace_string
                                )
                            else:
                                PrepareData.USING_DATA[threading.current_thread().ident][config_name] = [replace_string]
                        else:
                            PrepareData.USING_DATA[threading.current_thread().ident] = {}
                            if config_name in PrepareData.USING_DATA[threading.current_thread().ident].keys():
                                PrepareData.USING_DATA[threading.current_thread().ident][config_name].append(
                                    replace_string
                                )
                            else:
                                PrepareData.USING_DATA[threading.current_thread().ident][config_name] = [replace_string]
                    else:
                        replace_string = PrepareData.PREPARE_DATA[config_name][0]
                else:
                    log('{} not in Prepare_data, please check config file'.format(config_name))

                if replace_string is not None:
                    input_str = input_str.replace(replace_config_string, replace_string)

        return input_str

    @staticmethod
    def _replace_env_url(original):
        """
        替换环境url
        :param original:
        :return:
        """
        for url in PrepareData.URL.keys():
            original = original.replace(url, PrepareData.URL[url])

        return original

    @staticmethod
    def _get_date(original_string, datetime_now):
        """
        按照指定偏移量计算时间
        时间偏移单位: 天
        保留字格式: get_date(days)
        :param original_string:
        :param datetime_now:
        :return:
        """
        date_replace_strings = re.findall(r'get_date\((?:-?\d+)\)', original_string)

        if len(date_replace_strings) > 0:
            for replace_string in date_replace_strings:
                date_offset_str = replace_string.replace('get_date(', '').replace(')', '')

                day_offset = int(date_offset_str)

                date_offset_result = (datetime_now + datetime.timedelta(days=day_offset)).strftime('%Y-%m-%d')

                original_string = original_string.replace(str(replace_string), date_offset_result)

        return original_string

    @staticmethod
    def _get_datetime(original_string):
        # 按照制定偏移量计算指定时间(原始时间格式：YYYY-mm-dd HH:MM:SS)
        # 时间偏移单位: 秒
        # 保留字格式: get_datetime('YYYY-mm-dd HH:MM:SS', seconds)
        datetime_replace_strings = re.findall(
            r'get_datetime\((?:[\'|\"]?\d{4}-\d{2}-\d{2}\s\d{2}:\d{2}:\d{2}[\'|\"]?,\s*-?\d+)\)', original_string)

        if len(datetime_replace_strings) > 0:
            for replace_string in datetime_replace_strings:
                datetime_offset_str = replace_string.split(',')[1].strip().replace(')', '')
                datetime_str = replace_string.split(',')[0].strip().replace('get_datetime(', '')

                seconds_offset = int(datetime_offset_str)

                datetime_offset_result = (datetime.datetime.strptime(datetime_str, '%Y-%m-%d %H:%M:%S') +
                                          datetime.timedelta(seconds=seconds_offset)).strftime('%Y-%m-%d %H:%M:%S')

                original_string = original_string.replace(str(replace_string), datetime_offset_result)

        return original_string

    @staticmethod
    def _get_datetime_by_now(original_string, datetime_now):
        # 按照指定偏移量计算时间
        # 时间偏移单位: 天
        # 保留字格式: get_date(days)
        date_replace_strings = re.findall(r'get_datetime_by_now\((?:-?\d+)\)', original_string)

        if len(date_replace_strings) > 0:
            for replace_string in date_replace_strings:
                datetime_offset_str = replace_string.replace('get_datetime_by_now(', '').replace(')', '')

                seconds_offset = int(datetime_offset_str)

                date_offset_result = (datetime_now + datetime.timedelta(seconds=seconds_offset)).strftime(
                    '%Y-%m-%d %H:%M:%S'
                )

                original_string = original_string.replace(str(replace_string), date_offset_result)

        return original_string

    @staticmethod
    def _replace_time_stamp(original_string, datetime_now):
        # 替换保留字hour()和year()
        year_str = datetime_now.strftime('%Y%m%d%H%M%S')
        month_str = datetime_now.strftime('%m%d%H%M%S')
        day_str = datetime_now.strftime('%d%H%M%S')
        minute_str = datetime_now.strftime('%M%S')
        hour_str = datetime_now.strftime('%H%M%S')
        second_str = datetime_now.strftime('%S')
        now_str = datetime_now.strftime('%Y-%m-%d %H:%M:%S')
        time_stamp_id = datetime_now.strftime('%H%M%S%Y%m%d') + '0000'
        year_day_str = datetime_now.strftime('%Y%m%d')
        if time_stamp_id.startswith('0'):
            time_stamp_id = '9' + time_stamp_id[1:]

        original_string = str(original_string).replace('replace_hour()', hour_str). \
            replace('replace_year()', year_str). \
            replace('replace_day()', day_str). \
            replace('replace_minute()', minute_str). \
            replace('replace_second()', second_str). \
            replace('replace_month()', month_str). \
            replace('generate_time_stamp_id()', time_stamp_id).\
            replace('get_now()', now_str). \
            replace('replace_year_day()', year_day_str)

        return original_string

    @staticmethod
    def _get_rd_date(original_string, datetime_now):
        # 按照指定偏移量计算随机时间
        # 时间偏移单位: 天
        # 保留字格式: get_date(days)
        date_replace_strings = re.findall(r'get_rddate\((?:-?\d+)\)', original_string)

        if len(date_replace_strings) > 0:
            for replace_string in date_replace_strings:
                date_offset_str = replace_string.replace('get_rddate(', '').replace(')', '')

                day_offset = random.randint(0, int(date_offset_str))

                date_offset_result = (datetime_now + datetime.timedelta(days=day_offset)).strftime('%Y-%m-%d')

                original_string = original_string.replace(str(replace_string), date_offset_result)

        return original_string

    @staticmethod
    def _get_random(original_string):
        """
        生成随机数值
        应用示例：get_random
        :param original_string:
        :return:
        """
        date_replace_strings = re.findall(r'get_random\((?:-?\d+)\)', original_string)

        if len(date_replace_strings) > 0:
            for replace_string in date_replace_strings:
                date_offset_str = replace_string.replace('get_random(', '').replace(')', '')

                length = str(date_offset_str).__len__()
                day_offset = str(random.randint(0, int(date_offset_str)))
                day_offset = day_offset.zfill(length)

                original_string = original_string.replace(str(replace_string), day_offset)

        return original_string

    @staticmethod
    def _get_time_stamp(original_string):
        """
        获取当前时间戳字符串---11位，用于注册手机号
        应用示例： get_time_stamp()
        结果示例：15862403419
        :param original_string:
        :return:
        """
        time_stamp = time.time() * 10
        time_stamp = str(time_stamp).split('.')[0]

        original_string = str(original_string).replace('get_time_stamp()', time_stamp)

        return original_string


