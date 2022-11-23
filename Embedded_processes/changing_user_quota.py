# изменение квоты для существующего пользователя
    # удаляет пользовтаеля из группы
    # добавляет пользователя в др группу (задать нужную группу в GROUP_NAME)
    # изменяет квоту пользователю

import sys
sys.path.insert(0, "/home/niko/Documents/GitHub/NextCloud/Custom_methods_for_user/")
import nextcloud_connect
import remove_user_from_groups
import add_user_to_group
import update_quota_for_user

USER_NAME = "Anton"
GROUP_NAME = "бронзовая"

nc = nextcloud_connect.nextcloud_connect()

remove_user_from_groups.remove_user_from_groups(nc, USER_NAME)

add_user_to_group.add_user_to_group(nc, USER_NAME, GROUP_NAME)

update_quota_for_user.update_quota_for_user(nc, GROUP_NAME, USER_NAME)