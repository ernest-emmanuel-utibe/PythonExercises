if __name__ == '__main__':

    number = 5
    rem = 0
    while number != 0:
        rem = number % 10
        number //= 10
        print(rem, end=' ')
