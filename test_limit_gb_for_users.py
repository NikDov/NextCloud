from audioop import add
import nextcloud_client
from update_group_for_user import set_group_for_user

nc = nextcloud_client.Client('http://nextcloud.pd16.com')
nc.login('admin', '1996pd16')


set_group_for_user(nc, "Maria", "бронзовая")

