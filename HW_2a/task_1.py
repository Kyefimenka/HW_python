# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр. Учтите, что числа могут быть отрицательными

# print("Введите дробное число")
# number = input().replace(".","").replace("-","")
# total = 0
# for digit in number:
#     total += int(digit)
# print(f"Сумма цифр = {total}")

# numb = float(input())
# summ = 0
# for el in str(numb):
#     if el != '.':
#         summ += int(el)
# print(summ)

s = '0.56'
summ = 0
for i in s:
    if i.isdigit():
        summ += int(i)
print(summ)