import nextcloud_client


class Connector():

    def __init__(self, login, password):
        self.login    = login
        self.password = password
    
    
    def nextcloud_connect(self):
        nc = nextcloud_client.Client('http://nextcloud.pd16.com')
        nc.login(self.login, self.password)
        return nc


connector = Connector("admin", "1996pd16")
