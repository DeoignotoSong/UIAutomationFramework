import threading

from Core.Enum import TestStatus
from Utils.Log import log
from Core.Global import TestResult


class Assert:
    # 期待值等于实际值
    @staticmethod
    def is_equal(expected_value, actual_value, position=None):
        result_detail = 'Expected value: {}\nActual value: {}'.format(str(expected_value), str(actual_value))

        if str(expected_value) != str(actual_value):
            if position is not None:
                result_detail += position
            else:
                result_detail += '\nExpected value and Actual value are not equal'

            assert_status = TestStatus.Failed
        else:
            assert_status = TestStatus.Pass

        log(result_detail)

        Assert.__append_test_result__('is_equal', result_detail, assert_status=assert_status)

    # 期待值不等于实际值
    @staticmethod
    def is_not_equal(expected_value, actual_value, position=None):
        result_detail = 'Expected value: {}\nActual value: {}'.format(str(expected_value), str(actual_value))

        if str(expected_value) == str(actual_value):
            if position is not None:
                result_detail += position
            else:
                result_detail += '\nExpected value and Actual value are equal'

            assert_status = TestStatus.Failed
        else:
            assert_status = TestStatus.Pass

        log(result_detail)

        Assert.__append_test_result__('is_not_equal', result_detail, assert_status=assert_status)

    # 期待值包含实际值
    @staticmethod
    def is_containing(expected_value, actual_value, position=None):
        result_detail = 'Expected value: {}\nActual value: {}'.format(str(expected_value), str(actual_value))

        if type(actual_value) is list:
            if expected_value not in actual_value:
                if position is not None:
                    result_detail += position
                else:
                    result_detail += '\nExpected list values are not in Actual values.'

                assert_status = TestStatus.Failed
            else:
                assert_status = TestStatus.Pass

            log(result_detail)

            Assert.__append_test_result__('is_containing', result_detail, assert_status=assert_status)
        else:
            if not str(actual_value).__contains__(str(expected_value)):
                if position is not None:
                    result_detail += position
                else:
                    result_detail += '\nExpected string value is not in Actual string value.'

                assert_status = TestStatus.Failed
            else:
                assert_status = TestStatus.Pass

            log(result_detail)

            Assert.__append_test_result__('is_containing', result_detail, assert_status=assert_status)

    # 期待值不包含实际值
    @staticmethod
    def is_not_containing(expected_value, actual_value, position=None):
        result_detail = 'Expected value: {}\nActual value: {}'.format(str(expected_value), str(actual_value))

        if type(actual_value) is list:
            if expected_value in actual_value:
                if position is not None:
                    result_detail += position
                else:
                    result_detail += '\nExpected list values are in Actual list values.'

                assert_status = TestStatus.Failed
            else:
                assert_status = TestStatus.Pass

            log(result_detail)

            Assert.__append_test_result__('is_not_containing', result_detail, assert_status=assert_status)
        else:
            if str(actual_value).__contains__(str(expected_value)):
                if position is not None:
                    result_detail += position
                else:
                    result_detail += '\nExpected string value is in Actual string value.'

                assert_status = TestStatus.Failed
            else:
                assert_status = TestStatus.Pass

            log(result_detail)

            Assert.__append_test_result__('is_not_containing', result_detail, assert_status=assert_status)

    # 期待值大于实际值
    @staticmethod
    def is_greater_than(expected_value, actual_value, position=None):
        result_detail = 'Expected value: {}\nActual value: {}'.format(expected_value, actual_value)

        if expected_value < actual_value:
            if position is not None:
                result_detail += position
            else:
                result_detail += '\nExpected value is not greater then Actual value'

            assert_status = TestStatus.Failed
        else:
            assert_status = TestStatus.Pass

        log(result_detail)

        Assert.__append_test_result__('is_greater_than', result_detail, assert_status=assert_status)

    # 期待值小于实际值
    @staticmethod
    def is_less_than(expected_value, actual_value, position=None):
        result_detail = 'Expected value: {}\nActual value: {}'.format(expected_value, actual_value)

        if expected_value > actual_value:
            if position is not None:
                result_detail += str(position)
            else:
                result_detail += '\nExpected value is not less then Actual value'

            assert_status = TestStatus.Failed
        else:
            assert_status = TestStatus.Pass

        log(result_detail)

        Assert.__append_test_result__('is_less_than', result_detail, assert_status=assert_status)

    @staticmethod
    def __append_test_result__(assert_type, result_detail='', assert_status=TestStatus.Pass):
        if assert_status == TestStatus.Failed:
            TestResult.CURRENT_TEST_SCENARIO_RESULT[threading.current_thread().ident] = TestStatus.Failed

        TestResult.TEST_RESULTS[TestResult.CURRENT_TEST_SCENARIO[threading.current_thread().ident]]['test_case_details'].append(
            dict(test_step_name=assert_type, test_result=assert_status, result_detail=result_detail))
