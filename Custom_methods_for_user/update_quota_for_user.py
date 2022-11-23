# на выход принимает два аргумента: group_name и user_name
# group_name - это имя группы в системе nextcloud
# user_name - это имя пользователя в системе nextcloud
# например, update_quota_for_user("золотая", "Ivanov.Ivan.Ivanovic")
# quota_value измеряется в байтах (1ГБ = 1073741824 байт)

def update_quota_for_user(nc, group_name, user_name):
    quota_value = None
    if group_name == "золотая":
        quota_value = "10737418240"
    elif group_name == "серебряная":
        quota_value = "5368709120"
    elif group_name == "бронзовая":
        quota_value = "1073741824"

    try:
        nc.set_user_attribute(user_name, "quota", quota_value)
        print("<>INFO<>User:", user_name, "group:", group_name, "quota:", int(quota_value)/1024/1024/1024, "GB")
    except Exception:
        print("<>ERROR<>Can not update quota for user:", user_name)
        exit()