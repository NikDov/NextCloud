from audioop import add
import nextcloud_client

nc = nextcloud_client.Client('http://nextcloud.pd16.com')
nc.login('admin', '1996pd16')

#Изменяет гвоту доступной памяти для пользовтаеля
print(nc.set_user_attribute("Maria", "quota", "5"))
#Золотая группа 10гб, серебрянная 5гб, бронзовая 1гб