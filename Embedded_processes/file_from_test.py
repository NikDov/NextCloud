from audioop import add
import nextcloud_client
# from update_group_for_user import set_group_for_user

nc = nextcloud_client.Client('http://nextcloud.pd16.com')
nc.login('admin', '1996pd16')


# set_group_for_user(nc, "Maria", "бронзовая")

# nc.remove_user_from_group()

if len(nc.get_user_groups("Maria")) == 0:
    print("<>INFO<>User has not got group")
else:
    for group in nc.get_user_groups("Maria"):
        print("<>INFO<>Deleting group:", group)
        nc.remove_user_from_group("Maria", group)