# Задача 2: Найдите сумму цифр трехзначного числа.
# Пример:
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

# number = input("Enter your number: ")
# sum = 0
# for i in number:
#     sum = sum + int(i)
# print(sum)

# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов.
# Вместе они сделали S журавликов. Сколько журавликов сделал каждый ребенок,
# если известно, что Петя и Сережа сделали одинаковое количество журавликов,
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
# Пример:
# 6 -> 1  4  1
# 24 -> 4  16  4
# 60 -> 10  40  10

# numberS = int(input("Введите число журавликов: "))
# if numberS % 4 != 0:
#     print("Введено не верное число журавликов!")
# Katya = numberS // 2
# Petya = Katya // 2
# Sereza = Petya
# print("{}, {}, {}".format(Katya, Sereza, Petya))

# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали
# билет с номером. Счастливым билетом называют такой билет с шестизначным номером,
# где сумма первых трех цифр равна сумме последних трех. Т.е. билет с номером 385916 – счастливый,
# т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.
# Пример:
# 385916 -> yes
# 123456 -> no

numTicket = input("Ведите номер билета: ")
if len(numTicket) != 6:
    print("Некорректный номер билета!")
else:
    sum1 = int(numTicket[0])+int(numTicket[1])+ int(numTicket[2])
    sum2 = int(numTicket[3]) + int(numTicket[4])+int(numTicket[5])
    if sum1 == sum2:
        print("Счастливый билет!")
    else:
        print("Обычный билет!")