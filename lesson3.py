print('TASK #1')


def my_func(a, b):
    try:
        res = a / b
    except ZeroDivisionError:
        return 'cannot be divided by 0!'
    return res


print(my_func(int(input("Enter first number: ")), int(input("Enter second number: "))))
print('*' * 80)

print('TASK #2')      # Какой из вариантов более предпочтительный?


def personal_data():
    name = input("Enter your name: ")
    surname = input("Enter your surname: ")
    year_of_birth = input("Enter your year of birth: ")
    city = input("Enter you city of residence: ")
    email = input("Enter your email: ")
    telephone = input("Enter your telephone:")
    return name, surname, year_of_birth, city, email, telephone


print(personal_data())


print('TASK #2.1')


def personal_data2(name, surname, year_of_birth, city, email, telephone):
    print(name, surname, year_of_birth, city, email, telephone)


personal_data2(input("Enter your name: "),
               input("Enter your surname: "),
               input("Enter your year of birth: "),
               input("Enter you city of residence: "),
               input("Enter your email: "),
               input("Enter your telephone:"))
print('*' * 80)


print('TASK #3')


def my_func(a, b, c):
    result = max(a, b, c) + max(min(a, b), min(a, c), min(c, b))
    return result


print(my_func(5, 8, 3))
print('*' * 80)

print('TASK #4')


def my_func(x, y):
    res = x ** y
    return res


print(my_func(2, -3))

print('TASK #4.1')


def my_func(x, y):
    result = 1
    for i in range(abs(y)):
        result *= x
    return 1 / result


print(my_func(2, -3))
print('*' * 80)

print('TASK #5')
summa = 0
while True:
    try:
        user_list = list(input("Enter some numbers(enter non-numbers to exit): ").split())
        list1 = list(map(int, user_list))
        summa = summa + sum(list1)
        print(summa)
    except ValueError:
        break
print('*' * 80)

print('TASK #6-7')


def int_func():
    user_string = input('Enter your text: ')
    return user_string.title()


print(int_func())
