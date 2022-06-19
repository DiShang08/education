# Напишите функцию, которая имя и возраст водителя. Функция должна распечатать
# на экран заключение, может ли данный водитель управлять транспортом и определять
# она должна это по возрасту водителя: он должен быть больше или равен MIN_DRIVING_AGE
#
# Если водитель может управлять, выведите фразу "<name> может водить> " ,
# в противном случае "<name> еще рано садиться за руль"
#
# MIN_DRIVING_AGE = 18
# allowed_driving('tim', 17) # выведет "tim еще рано садиться за руль"
# allowed_driving('bob', 18) # выведет "bob может водить"

# 1

MIN_DRIVING_AGE = 18


def allowed_driving(name, age):
    if age < MIN_DRIVING_AGE:
        print(name, "еще рано садиться за руль")
    else:
        print(name, "может водить")


# print(allowed_driving('tim', 27))

# 2

MIN_DRIVING_AGE = 18

def allowed_driving(name, age):
    print(name,["еще рано садиться за руль", "может водить"][age>=MIN_DRIVING_AGE])
    # если внутри функции принта встречается:
    # [ вариант1, вариант2, вариант3, вариант4][тут указываем какой вариант необходимо печатать]
    # поскольку у нас возраст больше или равен, то выполняется ТРУ, а это один.
    # Если фолс, то это ноль.