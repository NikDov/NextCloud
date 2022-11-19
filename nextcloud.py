import nextcloud_client

nc = nextcloud_client.Client('http://nextcloud.pd16.com:8081')

nc.login('admin', '1996pd16')

nc.get_users()