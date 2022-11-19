import nextcloud_client

nc = nextcloud_client.Client('http://nextcloud.pd16.com:8081')
nc.login('admin', '1996pd16')

def create_user(user_name, password):
    global nc
    try:
        nc.create_user(user_name, password)
        print("<>INFO<>Creating user:", user_name)
        print("<>INFO<>Get user displayname:", nc.get_user(user_name)["displayname"])
        print("<>INFO<>User created")
    except Exception:
        print("<>ERROR<>Can not create user:", user_name)

create_user("Fedor.Chesnokov", "10021998@@@")