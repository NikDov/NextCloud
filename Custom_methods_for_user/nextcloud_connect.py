# Подключение к облаку с админки

import nextcloud_client

def nextcloud_connect():
    nc = nextcloud_client.Client('http://nextcloud.pd16.com')
    nc.login('admin', '1996pd16')
    return nc