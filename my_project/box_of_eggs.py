def box_of(egg):
    box = egg // 6
    rem = egg % 6
    new_box = 6 - rem
    if rem == 0:
        print(f'{box} boxes are needed.')
    else:
        print(f'boxes are needed with a remainder of {rem} eggs')
        print(f'{new_box} eggs are needed to complete the box.')


if __name__ == '__main__':
    egg = int(input("Enter number of eggs: "))
    box_of(egg)
