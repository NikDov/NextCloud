import nextcloud_client

nc = nextcloud_client.Client('http://nextcloud.pd16.com:8081')
nc.login('admin', '1996pd16')

# на вход функция принимает два аргумента: user_name и password
# user_name должен иметь вид --> Ivanov.Ivan.Ivanovich
# пароль должен "быть сложным"
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
