import random
from functools import reduce
from itertools import count, cycle
from math import factorial


print('TASK #1')
from sys import argv

print(argv)

productivity, rate, premium = map(int, argv[1:])
res = (productivity * rate) + premium
print(f'result: {res}')
print('*' * 80)


print('TASK #2')
# долго решал эту задачу, пока google не поддсказал функцию zip
# другого решения, к сожалению, не придумал
li = [random.randint(1, 200) for x in range(20)]
new_li = [j for i, j in zip(li, li[1:]) if j > i]
print(li)
print(new_li)
print('*' * 80)


print('TASK #3')
new_li = [el for el in range(20, 240) if el % 20 == 0 or el % 21 == 0]
print(new_li)
print('*' * 80)


print('TASK #4')
li = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
new_li = [el for el in li if li.count(el) == 1]
print(new_li)
print('*' * 80)


print('TASK #5')
li = [el for el in range(100, 1001) if el % 2 == 0]
new_li = reduce(lambda x, y: x * y, li)
print(new_li)
print('*' * 80)


print('TASK #6')
n = int(input('Enter your number: '))
for el in count(n):
    if el > 10:
        break
    print(el)

n = int(input('Enter your number of iterations: '))
i = 0
for el in cycle(input('Enter your text: ')):
    print(el)
    i += 1
    if i == n:
        break
print('*' * 80)


print('TASK #7')
n = int(input('Enter your number: '))
i = 0


def fact():
    for el in (factorial(i) for i in range(1, n + 1)):
        yield el


for el in fact():
    i += 1
    print(f"factorial {i} = {el}")