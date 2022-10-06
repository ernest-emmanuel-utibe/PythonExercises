if __name__ == '__main__':

    number = 1
    temp = 0
    temp = number
    summation = 0
    while number != 0:
        rem = number % 10
        summation = (summation * 10) + rem
        number //= 10
    if summation == temp:
        print('It is a palindrome number')
    else:
        print('It is not a palindrome number')