from audioop import add
import nextcloud_client

nc = nextcloud_client.Client('http://nextcloud.pd16.com')
nc.login('admin', '1996pd16')





def main():
    user_name = "Ivanov.Ilia.Antonovich"
    password = "12No2022Septr"
    group_name = "золотая"
    create_user(user_name, password)
    add_user_to_group(user_name, group_name)
    update_quota_for_user(group_name, user_name)
if __name__== "__main__" :
    main()