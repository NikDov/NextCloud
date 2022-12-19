import nextcloud_client


class Connector():

    
# == Connector to nextcloud
    def __init__(self, url, login, password):
        self.url = url
        self.login = login
        self.password = password
    
    
    def nextcloud_connect(self):
        nc = nextcloud_client.Client(self.url)
        nc.login(self.login, self.password)
        return nc



