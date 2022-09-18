# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности. 

sequence = [1,1,1,1,2,2,2,3,3,3,4,8,7,4,3,6,8,5,5,5,12]
result = [] 
for item in sequence:
    if item not in result:
        result.append(item)
print(sorted(result))