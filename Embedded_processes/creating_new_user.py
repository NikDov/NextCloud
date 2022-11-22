import sys
sys.path.insert(0, "/home/niko/Documents/GitHub/NextCloud/Custom_methods_for_user/")
import create_user
import nextcloud_connect
import add_user_to_group
import update_quota_for_user

USER_NAME = "Ksenia"
PASSWORD = "12390Mart!"
GROUP_NAME = "золотая"

nc = nextcloud_connect.nextcloud_connect()

create_user.create_user(nc, USER_NAME, PASSWORD)

add_user_to_group.add_user_to_group(nc, USER_NAME, GROUP_NAME)

update_quota_for_user.update_quota_for_user(nc, GROUP_NAME, USER_NAME)