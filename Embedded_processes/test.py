# dell = [1, 5, 7, 10, 4, 22, 22, 33, 44]


# print(dell[1:8:1])  # откуда: до куда (не включительно): шаг

#_____________________________________________________________________________________

# dell = [1, 5, 7, 10, 4, 22, 22, 33, 44]     # сложение чисел массива

# answer = 0
# for i in dell:
#     answer += i
# print(answer)







# class Human():

#     def __init__(self, name, age, work):
#         self.name = name
#         self.age = age
#         self.work = work
#         print('Человек создан')

#     def sit():
#         print("Human is sitting")



# chel = Human("igor", 30, "devops")

# print(chel.work)








def func():

    a = 10
    b = None
    if a == 10:
        b = "a == 10" 
    else:
        b = "a != 10"
    print(b)
    return b


def func2(string):

    if string == "a != 10":
        print("OK")
    else:
        print("NOT OK")


string = func()

func2(string)





