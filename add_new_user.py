from audioop import add
import nextcloud_client

nc = nextcloud_client.Client('http://nextcloud.pd16.com')
nc.login('admin', '1996pd16')

# на вход функция принимает два аргумента: user_name и password
# user_name должен иметь вид --> Ivanov.Ivan.Ivanovich
# пароль должен быть "сложным" --> passHard1999@@@cool
# например, create_user("Ivanov.Ivan.Ivanovich", "passHard1999@@@cool")

def create_user(user_name, password):
    global nc
    try:
        nc.create_user(user_name, password)
        print("<>INFO<>Creating user:", user_name)
        print("<>INFO<>Get user displayname:", nc.get_user(user_name)["displayname"])
        print("<>INFO<>User created")
    except Exception:
        print("<>ERROR<>Can not create user:", user_name)

# на вход функция принимает два аргумента: user_name и group_name
# user_name - это имя пользователя в системе nextcloud
# group_name - это имя группы в системе nextcloud
# например, add_user_to_group("Ivanov.Ivan.Ivanovich", "золотая")

def add_user_to_group(user_name, group_name):
    global nc
    try:
        nc.add_user_to_group(user_name, group_name)
        print("<>INFO<>Adding user:", user_name, "to group:", group_name)
        print("<>INFO<>User added to group")
    except Exception:
        print("<>ERROR<>Can not add user to group:", group_name)

# на выход принимает два аргумента: group_name и user_name
# group_name - это имя группы в системе nextcloud
# user_name - это имя пользователя в системе nextcloud
# например, update_quota_for_user("золотая", "Ivanov.Ivan.Ivanovic")
# quota_value измеряется в байтах (1ГБ = 1073741824 байт)

def update_quota_for_user(group_name, user_name):
    global nc
    quota_value = None
    if group_name == "золотая":
        quota_value = "10"
    elif group_name == "серебряная":
        quota_value = "5"
    elif group_name == "бронзовая":
        quota_value = "1"

    try:
        nc.set_user_attribute(user_name, "quota", quota_value)
        print("<>INFO<>User:", user_name, "group:", group_name, "quota:", quota_value)
    except Exception:
        print("<>ERROR<>Can not update quota for user:", user_name)
    




def main():
    user_name = "Ivanov.Ilia.Antonovich"
    password = "12No2022Septr"
    group_name = "золотая"
    create_user(user_name, password)
    add_user_to_group(user_name, group_name)
    update_quota_for_user(group_name, user_name)
if __name__== "__main__" :
    main()