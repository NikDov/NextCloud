# кастом метод создающий пользователя FULL.
# WARNING !!! перед запуском вызови в теримнале файл.sh с логином и паролем админа, далее запускай код.

from Connector import Connector
from User import User
import credentials
from File import File

connector = Connector(credentials.NEXTCLOUD_URL, credentials.NEXTCLOUD_USERNAME, credentials.NEXTCLOUD_PASSWORD).nextcloud_connect()
user = User()
file = File()

name = "Nikita.Chelll"     # задать параметры для создания пользовтаеля
password = "MsK2022Ears!"
group = 'золотая'   # Впиши : золотая, серебряная или бронзовая
email = 'Nikita@mail.ru'

user.create_user(connector, name, password)
# user.add_user_to_group(connector, name, group)
# user.update_quota_for_user(connector, group, name)
# user.add_user_email(connector, name, email)
# file.share_file_for_user(connector, name)