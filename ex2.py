arr = []
for i in range(1, 15):
    num = int(input(f"Введите {i}-e число: "))
    arr.append(num)
sum_even = sum(arr)
arr.append (sum_even)
for i in arr:
    print(i, end = " ")