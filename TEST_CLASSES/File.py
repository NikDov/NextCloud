    # кастомные методы для класса ФАЙЛЫ.

class File():

    def __init__(self):
        pass

    
    def share_file_for_user(self, connector, name):
        try:
            connector.share_file_with_user('testdir/nc_test.txt', name)
            print("<>INFO<>File is shared for user:", name)
        except Exception as err:
            print("<>ERROR<>File can not share for user:", name, "error:", err)
            exit()
