'''
кастом метод создающий пользователя с группой и квотой
'''

from Connector import Connector
from User_all_methods import User
import os

URL      = os.environ.get("NEXTCLOUD_URL")
USERNAME = os.environ.get("NEXTCLOUD_USERNAME")
PASSWORD = os.environ.get("NEXTCLOUD_PASSWORD")


connector = Connector(URL, USERNAME, PASSWORD).nextcloud_connect()
user = User()

'''
задать параметры для создания пользовтаеля
'''
user_name = "Ksenia"
user_password = "NiCloud!2016"
''' 
Впиши ниже: золотая, серебряная или бронзовая 
'''
user_group = "золотая"
user_email = "ksuuuu@mail.ru"

#user.create_user(connector, user_name, user_password)
#user.add_user_to_group(connector, user_name, user_group)
#user.update_quota_for_user(connector, user_group, user_name)
user.add_user_mail(connector, user_name, user_email)