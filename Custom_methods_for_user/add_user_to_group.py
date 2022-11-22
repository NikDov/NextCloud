# на вход функция принимает два аргумента: user_name и group_name
# user_name - это имя пользователя в системе nextcloud
# group_name - это имя группы в системе nextcloud
# например, add_user_to_group("Ivanov.Ivan.Ivanovich", "золотая")

def add_user_to_group(nc, user_name, group_name):
    try:
        nc.add_user_to_group(user_name, group_name)
        print("<>INFO<>Adding user:", user_name, "to group:", group_name)
        print("<>INFO<>User added to group")
    except Exception:
        print("<>ERROR<>Can not add user to group:", group_name)
        exit()