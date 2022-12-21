import nextcloud_client

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

# import os

# URL      = os.environ.get("NEXTCLOUD_URL")
# USERNAME = os.environ.get("NEXTCLOUD_USERNAME")
# PASSWORD = os.environ.get("NEXTCLOUD_PASSWORD")


# connector = Connector(URL, USERNAME, PASSWORD).nextcloud_connect()
# #connector.mkdir("testdir")
# connector.put_file("testdir/", "/home/nik/Desktop/nc_test.txt")
