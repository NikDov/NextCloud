def remove_user_from_groups(nc, user_name):
    if len(nc.get_user_groups(user_name)) == 0:
        print("<>INFO<>User has not got group")
    else:
        for group in nc.get_user_groups(user_name):
            try:
                 print("<>INFO<>Deleting group:", group)
                 nc.remove_user_from_group(user_name, group)
            except Exception:
                print("<>ERROR<>Can not remowe user from group:", user_name)
                exit()