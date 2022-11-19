import nextcloud_client

nc = nextcloud_client.Client('http://nextcloud.pd16.com:8081')
nc.login('admin', '1996pd16')

def create_user(user_name, password):
    global nc
    nc.create_user(user_name, password)
    print("<>INFO<>Creating user:", user_name)
    
    try:
        print(nc.get_user(user_name)["displayname"])
        print("<>INFO<>User created")
    except Exception:
        print("Can not found user:", user_name)

create_user("Tom", "10021998@@@")