import nextcloud_client

nc = nextcloud_client.Client('http://nextcloud.pd16.com:8081')

nc.login('admin', '1996pd16')

# users = nc.get_users()
# for user in users:
#     print("hello,", (user))

# просмотр методов
#print(dir(nc))

#nc.create_user('Maria', '120612PdMsk')

print('nc.get_users')
print("Hello, Nik")

