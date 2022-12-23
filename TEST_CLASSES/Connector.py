import nextcloud_client
import credentials

''' Connector to nextcloud '''
class Connector():
    
    def __init__(self, url, login, password):
        self.url = url
        self.login = login
        self.password = password
    
    def nextcloud_connect(self):
        nc = nextcloud_client.Client(self.url)
        nc.login(self.login, self.password)
        return nc

<<<<<<< HEAD
=======


# connector.put_file("testdir/", "/home/nik/Desktop/nc_test.txt")


connector = Connector(credentials.NEXTCLOUD_URL, credentials.NEXTCLOUD_USERNAME, credentials.NEXTCLOUD_PASSWORD).nextcloud_connect()
# connector.share_file_with_user('testdir/nc_test.txt', 'Nikita.Chel')
# print(connector.get_user("Nikita.Chel"))
>>>>>>> 91acc8468f7e1b10b836af65a0a7e5456a88aad9
