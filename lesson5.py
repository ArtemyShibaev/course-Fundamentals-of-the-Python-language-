print('TASK #1')
a = ''
with open('task1.txt', 'w') as f:
    while True:
        text = input('Your text:')
        f.write(f'{text}\n')
        print(text)
        if text == a:
            break
print('*' * 80)

print('TASK #2')
with open('task2.txt', 'r') as file:
    lines = 0
    for line in file:
        words = len(line.split())
        lines += 1
        print(f'in {lines} line - {words} word(s)')
print('*' * 80)


print('TASK #3')
with open('task3.txt', 'r') as file:
    my_dict = {line.split()[0]: int(line.split()[1]) for line in file}
    average = sum(my_dict.values()) / len(my_dict.values())
    print('Average income = ', average)
    for i in my_dict:
        if my_dict[i] < 20000:
            print('The employee', i, 'have a salary of less than 20,000')

print('*' * 80)

print('TASK #4')

new_dict = ['Один', 'Два', 'Три', 'Четыре']
with open('task4.txt', 'r') as f:
    text = list(f.read().replace('-', '').split())
    number_list = text[1::2]
    dict_res = dict(zip(new_dict, number_list))
    with open('task4_1.txt', 'w', encoding='UTF-8') as file:
        for key, val in dict_res.items():
            file.write('{} - {}\n'.format(key,val))
print('*' * 80)


print('TASK #5')
import random
from functools import reduce
with open('task5.txt', 'w', encoding='UTF-8') as f:
    numbers = [random.randint(1,100) for x in range(10)]
    f.write(" ".join(map(str, numbers)))
    new_li = reduce(lambda x, y: x + y, numbers)
    print(numbers)
    print(new_li)
print('*' * 80)


print('TASK #6')
import re
new_dict = ['Информатика','Физика','Физкультура']
new_list = []
my_dict = {}
with open('task6.txt', 'r', encoding='UTF-8') as f:
    lines = f.readlines()
    for line in lines:
        li = re.sub('[()-]',' ', line)
        numb_sum = sum([int(num) for num in filter(
                   lambda num: num.isnumeric(), li.split())])
        new_list.append(numb_sum)
    for i in range(0,len(new_dict)):
        my_dict[new_dict[i]] = new_list[i]
    with open('task6_1.txt', 'w',encoding='UTF-8') as file:
        for key, val in my_dict.items():
            file.write('{}:{}\n'.format(key, val))
print('*' * 80)


print('TASK #7')

import json
profit_list = []
average = []
firm_list = []
count = 0
with open('task7.txt', 'r', encoding='UTF-8') as f:
    lines = f.readlines()
    for line in lines:
        count += 1
        numb = [int(num) for num in filter(
               lambda num: num.isnumeric(), line.split())]
        profit = numb[0] - numb[1]
        profit_list.append(profit)
        if profit > 0:
            average = sum(profit_list) / count
        firm = line.split(' ')[0]
        firm_list.append(firm)
    dict1 = dict(zip(firm_list, profit_list))
    my_list = [dict1, {'average_profit': average}]
    with open('task7.json', 'w', encoding="UTF-8") as file:
        json.dump(my_list, file)
    print(my_list)