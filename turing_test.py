if __name__ == '__main__':

    position = int(input('Enter number: '))
    total = 0
    count = 0
    number_before_1 = 0
    number_before_2 = 1
    if position == 1:
        print(f'The number in position {position} is 0')
    elif position == 2:
        print(f'The number in position {position} is 1')
    elif position >= 3:
        while count < position - 2:
            total = number_before_1 + number_before_2
            number_before_1 = number_before_2
            number_before_2 = total
            count += 1
    print(f'The number in position {position} is {total}')
