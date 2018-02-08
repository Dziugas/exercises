import datetime

name = str(input("Please tell me your name: "))
age = int(input("Now please tell me your age: "))
how_many = int(input("How many times do you want us to print this?"))


def year_100():
    now = datetime.datetime.now()
    now_year = now.year
    year_100 = now_year - age + 100
    return year_100


def print_name():
    for i in range(0, how_many):
        print('\nIf you say your name is {0} and your age is {1}, then you\'re gonna be 100 in {2}'.format(str(name),
                                                                                                           str(age),
                                                                                                           str(
                                                                                                               year_100())))

print_name()
