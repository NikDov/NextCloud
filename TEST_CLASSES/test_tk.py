import nextcloud_client
import credentials

''' Connector to nextcloud '''
class Connector():
    
    def __init__(self):
        URL = credentials.NEXTCLOUD_URL
        USERNAME = credentials.NEXTCLOUD_USERNAME
        PASSWORD = credentials.NEXTCLOUD_PASSWORD
        nextcloud_client.Client(URL).login(USERNAME, PASSWORD)
        

connector = Connector()
connector.


