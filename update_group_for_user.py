def remove_user_from_groups(nc, user_name):
    if len(nc.get_user_groups(user_name)) == 0:
        print("<>INFO<>User has not got group")
    else:
        for group in nc.get_user_groups(user_name):
            print("<>INFO<>Deleting group:", group)
            nc.remove_user_from_group(user_name, group)


def add_user_to_group(nc, user_name, group_name):
    try:
        nc.add_user_to_group(user_name, group_name)
        print("<>INFO<>Adding user:", user_name, "to group:", group_name)
        print("<>INFO<>User added to group")
    except Exception:
        print("<>ERROR<>Can not add user to group:", group_name)


def update_quota_for_user(nc, group_name, user_name):
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