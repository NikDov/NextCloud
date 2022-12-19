'''
кастомные методы для класса ПОЛЬЗОВАТЕЛЬ
'''

from Connector import Connector

class User():

    """ class for users in nextcloud"""
    def __init__(self):
        pass
    

    """ method for create user """
    def create_user(self, connector, name, password):

        print("<>INFO<>Checking user exists")
        if name in connector.get_users():
            print("<>INFO<>User allready exists:", name)
            exit()
        else:
            try:
                connector.create_user(name, password)
                print("<>INFO<>Creating user:", name)
                print("<>INFO<>Get user displayname:", connector.get_user(name)["displayname"])
                print("<>INFO<>User created")
            except Exception:
                print("<>ERROR<>Can not create user:", name)
                exit()
        
       
    """ method for remove user """
    def remove_user(self, connector, name):

        print("<>INFO<>Checking user exists")
        if name not in connector.get_users():
            print("<>INFO<>User allredy not exists:", name)
            exit()
        else:
            try:
                connector.delete_user(name)
                print("<>INFO<>Removing user:", name)
                print("<>INFO<>User removed")
            except Exception:
                print("<>INFO<>Can not remove user:", name)
                exit()


    """ method for add user to group"""
    def add_user_to_group(self, connector, name, group):
        
        try:
            connector.add_user_to_group(name, group)
            print("<>INFO<>Adding user:", name, "to group:", group)
            print("<>INFO<>User added to group")
        except Exception:
            print("<>ERROR<>Can not add user to group:", group)
            exit()


    """ method for remove user from groups for change quota """
    def remove_user_from_groups(self, connector, name):
        
        if len(connector.get_user_groups(name)) == 0:
            print("<>INFO<>User has not got group")
        else:
            for group in connector.get_user_groups(name):
                try:
                    print("<>INFO<>Deleting group:", group)
                    connector.remove_user_from_group(name, group)
                except Exception:
                    print("<>ERROR<>Can not remowe user from group:", name)
                    exit()

    """ method for update quota for user """
    def update_quota_for_user(self, connector, group, name):
        
        quota_value = None
        if group == "золотая":
            quota_value = "10737418240"
        elif group == "серебряная":
            quota_value = "5368709120"
        elif group == "бронзовая":
            quota_value = "1073741824"
        try:
            connector.set_user_attribute(name, "quota", quota_value)
            print("<>INFO<>User:", name, "group:", group, "quota:", int(quota_value)/1024/1024/1024, "GB")
        except Exception:
            print("<>ERROR<>Can not update quota for user:", name)
            exit()

    """ methods for add user e-mail """
    def add_user_mail(self, connector, name, email):
        try:
            connector.set_user_attribute(name, "email", email)
            print("<>INFO<>User:", name, "email:", email)
        except Exception:
            print("<>ERROR<>Can not set email for user:", name)
            exit()
            



#connector = Connector("http://nextcloud.pd16.com", "admin", "1996pd16").nextcloud_connect()
#user = User()


# == ВЫЗОВ КАСТОМ МЕТОДОВ
# user.create_user(connector, "Ksenia", "Fedor1111100000!!!")
# user.remove_user(connector, "Nik12")
# user.add_user_to_group(connector, "FedFed", "золотая")
# user.remove_user_from_groups(connector, "FedFed")
# user.update_quota_for_user(connector, "золотая", "FedFed")
# user.add_user_mail(connector, "Ksenia", "Kseni@mail.ru")