# Напишите функцию check_password, которая проверяет переданный ей пароль на
# сложность и печатает на экран результат проверки.
#
# Сложным паролем будет считаться комбинация символов, в которой :
#
# Есть хотя бы 3 цифры
# Есть хотя бы одна заглавная буква
# Есть хотя бы один символ из следующего набора "!@#$%*"
# Общая длина не менее 10 символов
# Если пароль прошел все проверки, функция должна вывести на экран фразу
# "Perfect password", в противном случае - "Easy peasy"
#
# Вам необходимо написать только определение функции

def check_password(p):
    l1 = [i for i in p if i.isdigit()]
    l2 = [i for i in p if i.isupper()]
    l3 = [i for i in p if i in "!@#$%*"]
    print("Perfect password" if len(l1) >= 3 and len(l2) >= 1 and len(l3) >= 1 and len(p) >= 10 else "Easy peasy")