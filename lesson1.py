#1
print('TASK #1')
name = input('Enter your name: ')
age = int(input('Enter your age: '))

print('Hello,', name )
print('Your age is: ', age)

print('*' * 80)

#2
print('TASK #2')
seconds = int(input('Enter the time in seconds: '))
hours = seconds // 3600
seconds %= 3600
minutes = seconds // 60
seconds %= 60
print(hours, minutes, seconds, sep=":")

print('*' * 80)

#3
print('TASK #3')
n = input('Enter your number: ')
sum = int(n) + int(n+n) + int(n+n+n)
print(sum)

print('*' * 80)

#4
print('TASK #4')
user_number = int(input('Enter your number: '))
max = 0
while user_number > 10:
    last = user_number % 10
    user_number //= 10
    if last > max:
        max = last
    break
print('The largest digit in your number is', max)

print('*' * 80)

#5-6
print('TASK #5-6')
proceeds = int(input('Enter your proceeds: '))
expenses = int(input('Enter your expenses: '))
profit = proceeds - expenses

if profit > 0:
    rentability = profit/proceeds
    n = int(input('Enter your numbers of employees: '))
    profit_one = profit/n
    print('You work profitably! Profit =',profit)
    print('Your rentability=', rentability, 'profit per employee=', profit_one)
elif profit == 0:
    print('Your profit = 0')
else:
    print('You are operating at a loss! Loss =',profit)

print('*' * 80)

#7
print('TASK #7')
a = int(input('Enter the result on the first day = '))
b = int(input('Enter the needed result = '))
days = 1

while a <= b:
    a = a + a * 0.1
    days += 1
    if a == b:
        break
print('You will achieve results оn the {}th day: {}'.format(days, a))
