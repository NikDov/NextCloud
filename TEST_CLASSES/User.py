class User():

    def __init__(self, name, group, quota, password):
        self.name     = name
        self.group    = group
        self.quota    = quota
        self.password = password
        print("Object for <<class User>> is created")


    def create_user(self):
        try:
            nc.create_user(self.name, self.password)
            print("<>INFO<>Creating user:", self.name)
            print("<>INFO<>Get user displayname:", nc.get_user(self.name)["displayname"])
            print("<>INFO<>User created")
        except Exception:
            print("<>ERROR<>Can not create user:", self.name)
            exit()


