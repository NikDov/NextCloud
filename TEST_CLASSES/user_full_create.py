''' кастом метод создающий пользователя с группой и квотой '''

''' WARNING !!! перед запуском вызови в теримнале файл.sh с логином и паролем админа, 
    далее запускай код'''

from Connector import Connector
from User import User
import os

URL      = os.environ.get("NEXTCLOUD_URL")
USERNAME = os.environ.get("NEXTCLOUD_USERNAME")
PASSWORD = os.environ.get("NEXTCLOUD_PASSWORD")

connector = Connector(URL, USERNAME, PASSWORD).nextcloud_connect()
user = User()
''' задать параметры для создания пользовтаеля '''
name = "Nikita"
password = "NiCloud!2020"
''' Впиши ниже: золотая, серебряная или бронзовая '''
group = 'золотая'
email = 'Nikita@mail.ru'

user.create_user(connector, name, password)
user.add_user_to_group(connector, name, group)
user.update_quota_for_user(connector, group, name)
user.add_user_mail(connector, name, email)