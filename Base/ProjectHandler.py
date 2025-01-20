from Core.Global import DataBaseName
from Utils.Log import log


def reset_calendar(db, mobile):
    """
    重置讲师日历时间
    :param db:
    :param mobile:
    :return:
    """
    user_id = get_user_id_from_mobile(db, mobile)

    reset_sql = 'UPDATE {}.dxz_user_calendar SET {}, {}, {} WHERE user_id = "{}"'.format(
        DataBaseName.DATABASE_NAME['dxz_lan'],
        'work_date = "2019-10-01"',
        'start_date_all = "2019-10-01 07:00:00"',
        'end_date_all = "2019-10-01 07:45:00"',
        user_id
    )

    log(reset_sql)
    db.execute_modify_sql(reset_sql)

    return user_id


def get_user_id_from_mobile(db, mobile):
    """
    通过mobile从数据库查找user_id
    :param db:
    :param mobile:
    """
    mobile_cipher = parse_encrypt_base64(db, mobile)
    user_id_sql = 'SELECT * FROM {}.dxz_user WHERE mobile_cipher = "{}"'.format(
        DataBaseName.DATABASE_NAME['dxz_lan'],
        mobile_cipher
    )

    log(user_id_sql)
    user_id = db.execute_select_sql(user_id_sql)[0]['id']

    return user_id


def parse_encrypt_base64(db, cipher):
    """
    数据库加密字段解析
    :param db:
    :param cipher:
    :return:
    """
    result_sql = 'SELECT to_base64(aes_encrypt("{}", "dxz1234567890123")) as result'.format(
        cipher
    )

    result = db.execute_select_sql(result_sql)[0]['result']
    print(result)

    return result
