import math


def sum_digits(number):
    ret_value = 0
    n = number
    while n > 0:
        ret_value += n % 10
        n = math.floor(n/10)
    return ret_value


def calculate_digit(s_number):
    length = len(s_number)
    even_position = True
    sum_even = 0
    sum_odd = 0
    for i in range(length):
        d = ord(s_number[length-1-i]) - ord("0")
        if even_position:
            d = d*2
            sum_even += sum_digits(d)
        else:
            sum_odd += d
        even_position = not even_position

    sum = sum_odd + sum_even
    remainder = sum % 10
    if remainder == 0:
        return 0
    else:
        return 10 - remainder


def do_testcase():
    line = input()
    number_list = line.split(" ")
    for str_number in number_list:
        digit = calculate_digit(str_number)
        print(str(digit), end="")
    print()


for i in range(5):
    do_testcase()
