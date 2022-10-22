a = int(input('Enter the number: '))
print(a)
negofibonacci = [1,-1]
fibonacci = [1,1]

for i in range(2,a):
    list = fibonacci[i-1]+fibonacci[i-2]
    fibonacci.append(list)
    list_nego = negofibonacci[i-2] - negofibonacci[i-1]
    negofibonacci.append(list_nego)

negofibonacci.reverse()
negofibonacci.append(0)

print(f' for a = {a} =>{negofibonacci+fibonacci}')


fib = int(input('5# введите число for fib = '))
res_5 = []
for i in range(fib+1):
    if i==0:
        res_5.append(i)
    elif i==1:
        res_5.append(i)
        res_5.insert(0, i)
    else:
        res_5.append(res_5[len(res_5)-1]+res_5[len(res_5)-2])
        res_5.insert(0, (-1)**(i-1)*res_5[len(res_5)-1])
print(res_5)