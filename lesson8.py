 #Task 1
class Date:
    def __init__(self, day_month_year):
        self.day_month_year = str(day_month_year)


    @classmethod
    def extractor(cls, day_month_year):
        date = []

        for i in day_month_year.split():
            if i != '-': date.append(i)

        return int(date[0]), int(date[1]), int(date[2])

    @staticmethod
    def valid(day, month, year):

        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 0 <= year <= 2022:
                    return f'All right'
                else:
                    return f'Wrong year'
            else:
                return f'Wrong month'
        else:
            return f'Wrong day'


    def __str__(self):
        return f'The current date {Date.extractor(self.day_month_year)}'


today = Date('22 - 04 - 2022')
print(today)
print(today.valid(1, 12, 2022))
print(Date.valid(1, 12, 2002))
print(today.extractor('22 - 04 - 2022'))
print(Date.extractor('22 - 04 - 2022'))


# Task 2
class DivisionByZero(Exception):
    def __init__(self, txt):
        self.text = txt


number1 = input('Enter first number: ')
number2 = input('Enter second number: ')
try:
    number1 = int(number1)
    number2 = int(number2)

    if number2 == 0:
        raise DivisionByZero("can't divide by zero")
except ValueError:
    print('should be integer')
except DivisionByZero as err:
    print(err)
else:
    print('result = ', number1 / number2)
finally:
    print('End')

# Task 3
class MyError(Exception):
    def __init__(self):
        self. my_list = []

    def user_input(self):

        while True:
            try:
                user_value = int(input('Enter your value(s) and push "Enter" - '))
                self.my_list.append(user_value)
                print(f' Сurrent list - {self.my_list} \n ')

            except ValueError:
                print('invalid value - string')
                question = input('Try again? Y/N ')
                if question == 'Y' or question == 'y':
                    print(err.user_input())
                else:
                    return f'You got out'
            finally:
                print('-----')

err = MyError()
print(err.user_input())


# Task 4-6
class OfficeEquipmentWarehouse:

    def __init__(self, name, price, amount):
        self.name = name
        self.price = price
        self.amount = amount
        self.my_store_full = []
        self.my_store = []
        self.my_unit = {'device model': self.name, 'unit price': self.price, 'amount': self.amount}

    def __str__(self):
        return f'{self.name} price {self.price} amount {self.amount}'

    def acceptance_of_goods(self):
        try:
            unit_name = input('enter name ')
            unit_price = int(input('enter unit price '))
            unit_amount = int(input('enter amount '))
            unique = {'device model': unit_name, 'unit price': unit_price, 'amount': unit_amount}
            self.my_unit.update(unique)
            self.my_store.append(self.my_unit)
            print(f'current list -\n {self.my_store}')
        except:
            return f'Data entry error'

        print(f'To exit - Q, continue - Enter')
        q = input('...')
        if q == 'Q' or q == 'q':
            self.my_store_full.append(self.my_store)
            print(f'Whole warehouse -\n {self.my_store_full}')
            return f'Exit'
        else:
            return OfficeEquipmentWarehouse.acceptance_of_goods(self)



class Printer(OfficeEquipmentWarehouse):
    def info_printer(self):
        return f'the number of {self.name} is {self.amount}'


class Scanner(OfficeEquipmentWarehouse):
    def info_scanner(self):
        return f'the number of {self.name} is {self.amount}'


class Copier(OfficeEquipmentWarehouse):
    def info_copier(self):
        return f'the number of {self.name} is {self.amount}'


P = Printer('hp', 1250, 25)
S = Scanner('Canon', 1200, 20)
C = Copier('Xerox', 900, 15)
print(P.acceptance_of_goods())
print(S.acceptance_of_goods())
print(C.acceptance_of_goods())
print(P.info_printer())
print(S.info_scanner())
print(C.info_copier())



# Task7
class ComplexNumber:
    def __init__(self, a, b, *args):
        self.a = a
        self.b = b
        self.c = 'a + b * i'

    def __add__(self, other):
        # print(f'T ')
        return f'The sum of c1 and c2 = {self.a + other.a} + {self.b + other.b} * i'

    def __mul__(self, other):
        # print(f'T')
        return f'The product of numbers с1 and с2 =  = {self.a * other.a - (self.b * other.b)} + {self.b * other.a} * i'


c1 = ComplexNumber(2, -4)
c2 = ComplexNumber(4, 8)
print(c1 + c2)
print(c1 * c2)
