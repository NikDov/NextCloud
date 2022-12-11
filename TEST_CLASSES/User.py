from Connector import Connector

class User():

    def __init__(self):
        pass
    

    def create_user(self, connector, name, password):
        self.name = name
        self.password = password
        try:
            connector.create_user(self.name, self.password)
            print("<>INFO<>Creating user:", self.name)
            print("<>INFO<>Get user displayname:", connector.get_user(self.name)["displayname"])
            print("<>INFO<>User created")
        except Exception:
            print("<>ERROR<>Can not create user:", self.name)
            exit()
    
    def add_user_to_group(self, connector, name, group):
        self.name = name
        self.group = group
        try:
            connector.add_user_to_group(self.name, self.group)
            print("<>INFO<>Adding user:", self.name, "to group:", self.group)
            print("<>INFO<>User added to group")
        except Exception:
            print("<>ERROR<>Can not add user to group:", self.group)
            exit()

    def remove_user_from_groups(self, connector, name):
        self.name = name
        if len(connector.get_user_groups(self.name)) == 0:
            print("<>INFO<>User has not got group")
        else:
            for group in connector.get_user_groups(self.name):
                try:
                    print("<>INFO<>Deleting group:", group)
                    connector.remove_user_from_group(self.name, group)
                except Exception:
                    print("<>ERROR<>Can not remowe user from group:", self.name)
                    exit()

#  изменить, что бы при смене квоты менялась и группа тк это должно быть взаимосвязано
    def update_quota_for_user(self, connector, group, name):
        self.group = group
        self.name = name
        quota_value = None
        if self.group == "золотая":
            quota_value = "10737418240"
        elif self.group == "серебряная":
            quota_value = "5368709120"
        elif self.group == "бронзовая":
            quota_value = "1073741824"

        try:
            connector.set_user_attribute(self.name, "quota", quota_value)
            print("<>INFO<>User:", self.name, "group:", self.group, "quota:", int(quota_value)/1024/1024/1024, "GB")
        except Exception:
            print("<>ERROR<>Can not update quota for user:", self.name)
            exit()



# create user from grup
# update quota

connector = Connector("http://nextcloud.pd16.com:8081", "admin", "1996pd16").nextcloud_connect()
user = User()
#user.create_user(connector, "FedFed", "Fedor1111100000!!!")
# user.add_user_to_group(connector, "FedFed", "золотая")
# user.remove_user_from_groups(connector, "FedFed")
user.update_quota_for_user(connector, "золотая", "FedFed")