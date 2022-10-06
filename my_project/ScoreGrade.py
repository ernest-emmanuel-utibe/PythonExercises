if __name__ == '__main__':

    count = 1
    counter = 0
    while count <= 5:
        score = int(input('Enter a score: '))
        if score < 0 or score > 100:
            print('Enter a valid score.')
            counter += 1
        else:
            grade = 'Null'
            if 90 <= score <= 100:
                result = 'A'

            elif 70 <= score <= 100:
                result = 'B'

            elif 50 <= score <= 100:
                result = 'C'

            elif 40 <= score <= 100:
                result = 'D'

            elif 30 <= score <= 100:
                result = 'E'

            elif score < 30 < 100:
                result = 'F'
                print('YOU DON FAIL THIS ONE !!!!')
            count += 1
            print(f'Grade is {result}')

        if counter == 3:
            print('You have entered too many invalid score number')

        break