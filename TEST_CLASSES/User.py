from Connector import Connector

class User():

    def __init__(self, name, group, quota, password):
        self.name     = name
        self.group    = group
        self.quota    = quota
        self.password = password
        print("Object for <<class User>> is created")
    

    def create_user(self, connector):
        try:
            connector.create_user(self.name, self.password)
            print("<>INFO<>Creating user:", self.name)
            print("<>INFO<>Get user displayname:", connector.get_user(self.name)["displayname"])
            print("<>INFO<>User created")
        except Exception:
            print("<>ERROR<>Can not create user:", self.name)
            exit()

connector = Connector("http://nextcloud.pd16.com", "admin", "1996pd16").nextcloud_connect()
user = User("Igor.Ok", "золотая", "50000", "Fedor10021998!!!")
user.create_user(connector)
