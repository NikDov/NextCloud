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

connector = Connector(credentials.NEXTCLOUD_URL, 
                      credentials.NEXTCLOUD_USERNAME, 
                      credentials.NEXTCLOUD_PASSWORD)
connector.get_users()