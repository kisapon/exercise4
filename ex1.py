import random
arr = []
for i in range(15):
    arr.append(random.randint(-100, 100))
for i in arr:
    print(i, end = " ")