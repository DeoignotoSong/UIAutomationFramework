import re
import enum


class PageScriptAutoGenerator:
    def __init__(self, project_name, file_path):
        self.project_name = project_name
        self.properties_section = []
        self.actions_section = []
        self.fields_section = []
        self.origin_file_content = []
        self.file_path = file_path

        with open(file_path, 'r', encoding='utf8') as page_file:
            for line in page_file.readlines():
                self.origin_file_content.append(line.strip('\n\r'))
                if re.match('^# endregion Fields', line.strip()):
                    break

            self.origin_file_content.append('')

            is_fields = False
            for line_index in range(0, len(self.origin_file_content)):
                if re.match('^# region Fields', self.origin_file_content[line_index].strip()):
                    is_fields = True

                if is_fields:
                    self.fields_section.append(self.origin_file_content[line_index])

                if re.match('^# endregion Fields', self.origin_file_content[line_index].strip()):
                    break

    def generate_page_file(self, generate_path):
        self._generate_properties_section()
        self._generate_action_section()

        file_content = self.origin_file_content

        file_content.extend(self.properties_section)

        file_content.extend(self.actions_section)

        with open(generate_path, 'w', encoding='utf-8') as result_file:
            for item in file_content:
                result_file.write(item + '\n')

    def _generate_properties_section(self):
        region_count = 0
        index = 0
        try:
            while index < len(self.fields_section):
                # 获取当前行内容，去掉首尾换行符和空格
                line = self.fields_section[index]

                if re.match('^# region .*', line.strip(), re.I):
                    region_count += 1
                elif re.match('^# endregion.*', line.strip(), re.I):
                    region_count -= 1

                # 最后一个“# endregion”匹配“# region Fields”,无需添加
                if re.match('^# region.*', line.strip()):
                    self.properties_section.append('    # region Properties')
                # 修改处： endregion --> endregion Properties
                elif re.match('^# endregion.*', line.strip(), re.I):
                    self.properties_section.append('    # endregion Properties')
                    self.properties_section.append('')

                if re.match('self\\..+_tag.*', line.strip(), re.I):
                    self._property_section(line, index)
                elif re.match('self\\..+_tags.*', line.strip(), re.I):
                    self._property_section(line, index)
                index += 1
        except Exception as error:
            print(str(error))
            print('File path: ' + self.file_path)
            print('The line number: ' + str(index))


    def _generate_action_section(self):

        region_count = 0
        actions_count = 0
        is_sub_parameter = False
        index = 0

        while index < len(self.fields_section):
            # “动作”方法的注释
            self.current_action_comment = ''
            # “动作”方法的参数
            self.current_action_parameters = ''
            # “动作”方法的方法名
            self.current_action_name = ''
            # “动作”的内容
            self.current_action_content = ''
            # 获取当前行内容，去掉首尾换行符和空格
            line = self.fields_section[index]

            if index == 0:
                control = ''
            else:
                if not self.fields_section[index - 1].strip() == '':
                    control = self.fields_section[index - 1].strip().split(' ')[1]
                else:
                    control = ''

            if re.match('^# region .*', line.strip(), re.I):
                region_count += 1
            elif re.match('^# endregion.*', line.strip(), re.I):
                region_count -= 1

            # 匹配到region,添加region Actions
            if re.match('^# region.*', line.strip()):
                self.actions_section.append('    # region Actions')
            # 匹配到endregion,添加endregion Actions
            elif re.match('^# endregion.*', line.strip(), re.I):
                self.actions_section.append('    # endregion Actions')

            if re.match('# region .* section', line.strip(), re.I):
                is_sub_parameter = True
                self.current_action_parameters = ''
                self.current_action_content = ''
                self.current_action_name = '    def action_%d(self%%s):' % actions_count
                current_action_comment = '        """\n'
                current_action_comment += '        动作：设置%s\n' % self.fields_section[index].split('region')[1].split(
                    "section")[0].strip()
            elif re.match('# region .* line card', line.strip(), re.I):
                current_action_parameters = ''
                current_action_content = ''
                current_action_name = '    def set_line_card_action(self, row_index%s):'
                current_action_comment = '        """\n'
                current_action_comment += '        动作：设置%s\n%s\n' % (
                    self.fields_section[index].split('region')[1].split("line card")[0].strip(),
                    '        :param row_index: 卡片行号（计数从0开始）'
                )

                self.actions_section.append(current_action_name % current_action_parameters)
                self.actions_section.append(current_action_comment)
                self.actions_section.append(current_action_content)

                is_sub_parameter = False
                self.current_action_content = ''

                actions_count += 1
            elif is_sub_parameter and re.match('self\\..+_tag.*', line.strip(), re.I):
                self.current_action_parameters += ', ' + self.fields_section[index].split('self._')[1].split('_tag')[0]

                if re.match('self\\..+line_card_input_tag.*', line.strip(), re.I):
                    self.current_action_comment += '        :param %s: %s\n' % (
                        self._generate_property_method_name(line),
                        control
                    )

                    self.current_action_content += '        self.%s.clear_and_send_keys(self.%s.get_elements(self.%s)[%s], %s)\n\n' % (
                        self.project_name,
                        self.project_name,
                        self._generate_property_method_name(line),
                        'row_index',
                        self._generate_property_method_name(line)
                    )
                elif re.match('self\\..+_radio_tag.*', line.strip(), re.I):
                    self.current_action_comment += '        :param %s: %s\n' % (
                        self._generate_property_method_name(line),
                        control
                    )

                    self.current_action_content += '        self.%s.select_radio(self.%s, %s)\n\n' % (
                        self.project_name,
                        self._generate_property_method_name(line),
                        self._generate_property_method_name(line)
                    )
                elif re.match('self\\..+input_tag.*', line.strip(), re.I):
                    self.current_action_comment += '        :param %s: %s\n' % (
                        self._generate_property_method_name(line),
                        control
                    )

                    self.current_action_content += '        self.%s.clear_and_send_keys(self.%s, %s)\n\n' % (
                        self.project_name,
                        self._generate_property_method_name(line),
                        self._generate_property_method_name(line)
                    )
                elif re.match('self\\..+_select_tag.*', line.strip(), re.I):
                    self.current_action_comment += '        :param %s: %s\n' % (
                        self._generate_property_method_name(line),
                        control
                    )

                    self.current_action_content += '        self.%s.select_control(self.%s, self.%s, %s)\n\n' % (
                        self.project_name,
                        self._generate_property_method_name(line),
                        self._generate_property_method_name(self.fields_section[index + 1]),
                        self._generate_property_method_name(line)
                    )

                    index += 1
                elif re.match('self\\..+_single_date_tag.*', line.strip(), re.I):
                    self.current_action_comment += '        :param %s: %s\n' % (
                        self._generate_property_method_name(line),
                        control
                    )

                    self.current_action_content += '        self.%s.set_single_datetime(self.%s, %s)\n\n' % (
                        self.project_name,
                        self._generate_property_method_name(line),
                        self._generate_property_method_name(line)
                    )

            elif not is_sub_parameter and re.match('self\\..+_tag.*', line.strip(), re.I):
                if re.match('self\\..+_text_tag.*', line.strip(), re.I):
                    self._text_action(line, control)
                elif re.match('self\\..+line_card_button_tag.*', line.strip(), re.I):
                    self.current_action_name = '    def click_%s_action(self, row_index):' % (
                        line.split('self._')[1].split('_tag')[0],
                    )
                    self.current_action_comment = '        """\n'
                    self.current_action_comment += '        动作：点击%s\n' % control
                    self.current_action_content += '        :param row_index: 卡片行号（计数从0开始）'
                    self.current_action_comment += '        :return: 点击\'%s\'按钮后的页面\n' % control
                    self.current_action_comment += '        """'

                    self.current_action_content = '        self.%s.click(self.%s.get_elements(self.%s)[%s])\n' % (
                        self.project_name,
                        self.project_name,
                        self._generate_property_method_name(line),
                        'row_index'
                    )
                    self.current_action_content += '        return self.%s.get_current_page_source()\n' % self.project_name
                elif re.match('self\\.._radio_tag.*', line.strip(), re.I):
                    self.current_action_name = '    def select_%s_action(self, %s):' % (
                        line.split('self._')[1].split('_tag')[0],
                        self._generate_property_method_name(line)
                    )
                    self.current_action_comment = '        """\n'
                    self.current_action_comment += '        动作：选择%s\n' % control
                    self.current_action_comment += '        :param %s: %s\n' % (
                        self._generate_property_method_name(line),
                        control
                    )
                    self.current_action_comment += '        :return: 选择\'%s\'后的页面\n' % control
                    self.current_action_comment += '        """'

                    self.current_action_content = '        self.%s.select_radio(self.%s, %s)\n' % (
                        self.project_name,
                        self._generate_property_method_name(line),
                        self._generate_property_method_name(line)
                    )
                    self.current_action_content += '        return self.%s.get_current_page_source()\n' % self.project_name
                elif re.match('self\\..+_single_date_tag.*', line.strip(), re.I):
                    self.current_action_name = '    def set_%s_action(self, %s):' % (
                        line.split('self._')[1].split('_tag')[0],
                        self._generate_property_method_name(line)
                    )
                    self.current_action_comment = '        """\n'
                    self.current_action_comment += '        动作：设置%s\n' % control
                    self.current_action_comment += '        :param %s: %s\n' % (
                        self._generate_property_method_name(line),
                        control
                    )
                    self.current_action_comment += '        :return: 设置\'%s\'后的页面\n' % control
                    self.current_action_comment += '        """'

                    self.current_action_content = '        self.%s.set_single_datetime(self.%s, %s)\n' % (
                        self.project_name,
                        self._generate_property_method_name(line),
                        self._generate_property_method_name(line)
                    )
                    self.current_action_content += '        return self.%s.get_current_page_source()\n' % self.project_name
                # select_tag标签识别，生成section
                elif re.match('self\\..+_select_tag.*', line.strip(), re.I):
                    self._select_action(line, index, control)
                # input_tag标签识别，生成section
                elif re.match('self\\..+input_tag.*', line.strip(), re.I):
                    self._input_action(line, control)
                # button_tag标签识别，生成section
                elif re.match('self\\..+button_tag.*', line.strip(), re.I):
                    self._button_action(line, control)
                else:
                    index += 1

                    continue
                # 将当前生成action代码写入action_section
                self.actions_section.append(self.current_action_name)
                self.actions_section.append(self.current_action_comment)
                self.actions_section.append(self.current_action_content)

            index += 1

    @staticmethod
    def _generate_property_method_name(field):
        items = field.split('=')[0].strip().split('_')

        property_method_name = ''

        for index in range(1, len(items) - 1):
            if index == 1:
                property_method_name += items[index]
            else:
                property_method_name += '_' + items[index]

        return property_method_name

    # 生成_tag标签方法
    def _property_section(self, line, index):
        method_name = self._generate_property_method_name(self.fields_section[index].strip())
        self.properties_section.append('    @property')
        self.properties_section.append('    def %s(self):' % method_name)
        self.properties_section.append('        """')
        self.properties_section.append('        属性: %s' % self.fields_section[index - 1].split('# ')[1].strip())
        self.properties_section.append('        :return: %s' % self.fields_section[index - 1].split('# ')[1].strip())
        self.properties_section.append('        """')
        self.properties_section.append('        element = None')
        self.properties_section.append('        try:')
        self.properties_section.append('            element = self.%s.get_element(%s)' % (self.project_name, line.split('=')[0].strip()))
        self.properties_section.append('        except AttributeError as error:')
        self.properties_section.append('            log(error)')
        self.properties_section.append('        return element\n')

    # 生成_text_tag标签方法
    def _text_action(self, line, control):
        self.current_action_name = '    def get_%s_action(self):' % (
            line.split('self._')[1].split('_tag')[0],
        )
        self.current_action_comment = '        """\n'
        self.current_action_comment += '        动作：获取%s的文本\n' % control
        self.current_action_comment += '        :return: \'%s\'的文本\n' % control
        self.current_action_comment += '        """'

        self.current_action_content = '        control_content = self.%s.get_element_text(self.%s)\n' % (
            self.project_name, self._generate_property_method_name(line)
        )
        self.current_action_content += '        return control_content\n'

    # 生成_select_tag标签方法
    def _select_action(self, line, index, control):
        self.current_action_name = '    def get_select_%s_action(self, %s):' % (
            line.split('self._')[1].split('_select_tag')[0],
            self._generate_property_method_name(line)
        )
        self.current_action_comment = '        """\n'
        self.current_action_comment += '        动作：获取%s列表选中的文本\n' % control
        self.current_action_comment += '        :param %s: %s列表索引或文本\n' % (
            self._generate_property_method_name(line),
            control
        )
        self.current_action_comment += '        :return: \'%s\'的文本\n' % control
        self.current_action_comment += '        """'

        self.current_action_content = '        control_content = self.%s.get_select_content(self.%s, %s)\n' % (
            self.project_name,
            self._generate_property_method_name(line),
            self._generate_property_method_name(line)
        )
        self.current_action_content += '        return control_content\n'

        self.actions_section.append(self.current_action_name)
        self.actions_section.append(self.current_action_comment)
        self.actions_section.append(self.current_action_content)

        self.current_action_name = '    def select_%s_action(self, %s):' % (
            line.split('self._')[1].split('_select_tag')[0],
            self._generate_property_method_name(line)
        )
        self.current_action_comment = '        """\n'
        self.current_action_comment += '        动作：选择%s\n' % control
        self.current_action_comment += '        :param %s: %s列表索引或文本\n' % (
            self._generate_property_method_name(line),
            control
        )
        self.current_action_comment += '        :return: 选择\'%s\'选择器后的页面\n' % control
        self.current_action_comment += '        """'

        self.current_action_content = '        self.%s.select_control(self.%s, %s)\n' % (
            self.project_name,
            self._generate_property_method_name(line),
            self._generate_property_method_name(line)
        )
        self.current_action_content += '        return self.%s.get_current_page_source()\n' % self.project_name

        index += 1

    # 生成_input_tag标签方法
    def _input_action(self, line, control):
        self.current_action_name = '    def set_%s_action(self, %s):' % (
            line.split('self._')[1].split('_tag')[0],
            self._generate_property_method_name(line)
        )
        self.current_action_comment = '        """\n'
        self.current_action_comment += '        动作：设置%s\n' % control
        self.current_action_comment += '        :param %s: %s\n' % (
            self._generate_property_method_name(line),
            control
        )
        self.current_action_comment += '        :return: 设置\'%s\'文本后的页面\n' % control
        self.current_action_comment += '        """'

        self.current_action_content = '        self.%s.clear_and_send_keys(self.%s, %s)\n' % (
            self.project_name,
            self._generate_property_method_name(line),
            self._generate_property_method_name(line)
        )
        self.current_action_content += '        return self.%s.get_current_page_source()\n' % self.project_name

    # 生成_button_tag标签方法
    def _button_action(self, line, control):
        self.current_action_name = '    def click_%s_action(self):' % (
            line.split('self._')[1].split('_tag')[0],
        )
        self.current_action_comment = '        """\n'
        self.current_action_comment += '        动作：点击%s\n' % control
        self.current_action_comment += '        :return: 点击\'%s\'按钮后的页面\n' % control
        self.current_action_comment += '        """'

        self.current_action_content = '        self.%s.click(self.%s)\n' % (
            self.project_name,
            self._generate_property_method_name(line)
        )
        self.current_action_content += '        return self.%s.get_current_page_source()\n' % self.project_name