from nextcloud import NextCloud
NEXTCLOUD_URL = "http://nextcloud.pd16.com:8081"
NEXTCLOUD_USERNAME = "admin"
NEXTCLOUD_PASSWORD = "1996pd16"

to_js = True
nxc = NextCloud(endpoint=NEXTCLOUD_URL, user=NEXTCLOUD_USERNAME, password=NEXTCLOUD_PASSWORD, json_output=to_js)
# Quick start
print(nxc.get_users())         
