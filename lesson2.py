#1
print('TASK #1')
type_list = [23, 'Text', [1, 2, 3, 4], {'name': 'Tom', 'age': '25'}, ('password', 'login')]
for element in type_list:
    print(type(element))
print('*' * 80)


#2
print('TASK #2')
user_list = list(input('Enter your list: '))
for i in range(0, len(user_list)-1, 2):
    user_list[i], user_list[i+1] = user_list[i+1], user_list[i]
print(user_list)
print('*' * 80)


#3
print('TASK #3')
user_number = int(input('Enter your month from 1 to 12: '))
list_season = {'winter': [12, 1, 2], 'spring': [3, 4, 5], 'summer': [6, 7, 8], 'autumn': [9, 10, 11]}
for el in list_season:
    if user_number in list_season[el]:
        print('Your month belongs to: ', el)
        break
print('*' * 80)


#4
print('TASK #4')
user_string = input('Enter some words separated by spaces: ').split()
for i, el in enumerate(user_string, 1):
    print(i, el[0:10])
print('*' * 80)


#5
print('TASK #5')
my_list = [8, 7, 5, 3, 2, 2]
user_number = int(input('Enter your number: '))
my_list.insert(0, user_number)
my_list.sort(reverse=True)
print(my_list)