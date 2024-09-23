# вариант 1 задача 2
"""z = [int(x) for x in input().split()]
sorted_z = sorted(z)
print(sorted_z)
print(sorted_z[-1] - sorted_z[0])
"""

# вариант 1 задача 1
numbers = [int(x) for x in input().split()] #изначальный список
result = [] #итоговый список
l = len(numbers) #длина списка
if l == 1:
    result = numbers
else:
    for i in range(l):
        if i == 0: # случай, когда нужно найти соседей первого элемента списка
            result.append(numbers[1] + numbers[-1]) # складываем второй элемент и последний
        elif i == l - 1: # случай, когда нужно найти соседей последнего элемента списка
            result.append(numbers[0] + numbers[-2]) #складываем первый элемент и предпоследний
        else:
            result.append(numbers[i-1] + numbers[i+1]) # тут мы ищем соседей всех остальных элементов списка

res = ' '.join(str(x) for x in result) # переводим из int в str через пробел все элеменры списка
print(res)

