def set_group_for_user(nc, user_name, group_name):
    quota_value = None
    if group_name == "золотая":
        quota_value = "10"
    elif group_name == "серебряная":
        quota_value = "5"
    elif group_name == "бронзовая":
        quota_value = "1"

    try:
        print("<>INFO<>Adding user:", user_name, "to group:", group_name)
        nc.add_user_to_group(user_name, group_name)
        print("<>INFO<>User added to group")
        
        print("<>INFO<>Setting quota:", quota_value, "for user:", user_name)
        nc.set_user_attribute(user_name, "quota", quota_value)
        print("<>INFO<>User:", user_name, "group:", group_name, "quota:", quota_value)
    except Exception:
        print("<>ERROR<>Can not update group for user:", user_name)
