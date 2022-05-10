# Создайте функцию, которая выводит приветствие для пользователя с заданным именем. Если имя не указано, она должна
# выводить приветствие для пользователя с Вашим именем.
def hello():
    print ("If you dont want input your name, input number 1- ")
    my_name = "Yuriy"
    your_name = input("Input your name - ", )
    if your_name != "1":
        print("Hello", your_name, "!")
    else:
        print("Nobody here, so that - Hello me,", my_name,"!")

hello()


