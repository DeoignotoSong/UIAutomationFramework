from Core.ConfigOperation import ConfigOperation
from DB.MysqlDB import MysqlDB

"""
重置讲师日历表
"""
project = 'PC'
env = 'LAN'
config = ConfigOperation.load_config('./Projects/{project}/Base/config.ini'.format(project=project))
db = MysqlDB(config, env)
data = ''

for key, value in config.items(env + '.PrepareData'):
    if key.__contains__('teacher') and not key.__contains__('password') and value:
        if data:
            data = data + ',' + value
        else:
            data = value

users = data.split(',')

for user in users:
    mobile_cipher_sql = 'SELECT to_base64(aes_encrypt("{}", "dxz1234567890123")) as result'.format(user)
    mobile_cipher = db.execute_select_sql(mobile_cipher_sql)[0]['result']
    print(mobile_cipher)

    user_id_sql = 'SELECT * FROM dxz_user WHERE mobile_cipher = "{}"'.format(mobile_cipher)
    print(user_id_sql)
    user_id = db.execute_select_sql(user_id_sql)[0]['id']

    reset_sql = 'UPDATE dxz_user_calendar SET work_date = "2019-10-01", start_date_all = "2019-10-01 07:00:00", end_date_all = "2019-10-01 07:45:00"  WHERE user_id = "{}"'.format(user_id)
    print(reset_sql)
    db.execute_modify_sql(reset_sql)







