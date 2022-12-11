from Connector import Connector


connector = Connector("http://nextcloud.pd16.com:8081", "admin", "1996pd16")
x = connector.connection
x.get_user("Fedor")