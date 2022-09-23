""" Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным. 
Пример: - 6 -> да - 7 -> да - 1 -> нет  """

def InputNumbers(inputText):
    OK = False
    while not OK:
        try:
            number = int(input(f"{inputText}"))
            OK = True
        except ValueError:
            print("Это не число!")
    return number

def checkNumber(num):
    if 6 <= num <= 7:
        print("Да, это выходной день")
    elif 0 < num < 6:
        print("Нет, это рабочий день")
    else:
        print("В неделе только 7 дней!")

num = InputNumbers("Введите число обозначающий день недели: ")
checkNumber(num)
