class Assignment:
    @staticmethod
    def is_grade(grade):
        if grade >= 90:
            print(f'Congratulations! Your grade of {grade} earns you an A in this course')
        else:
            print('Passed')

    @staticmethod
    def box_of(egg):
        box = egg // 6
        rem = egg % 6
        new_box = 6 - rem
        if rem == 0:
            print(f'{box} boxes are needed.')
        else:
            print(f'{box} boxes are needed with a remainder of {rem} eggs.')
            print(f'{new_box} eggs are needed to complete the box.')

    @staticmethod
    def bacteria_start_with(bacteria):
        print(f'Hour\t\tNumber of Bacteria')
        for hours in range(0, 20, 5):
            output = bacteria * 2 * hours
            print(f'{hours}\t\t\t{output}')

    @staticmethod
    def hourly_wage(good, bad, principal):
        good_new_hourly_wage = principal * ((1 + 0.03) ** good)
        print(f'After {good} years of good reviews, new hourly wage is ${good_new_hourly_wage : .2f}')
        bad_new_hourly_wage = principal * ((1 - 0.03) ** bad)
        print(f'After {bad} years of bad reviews, new hourly wage is ${bad_new_hourly_wage : .2f}')

    @staticmethod
    def heart_rate():
        age = int(input('Enter your age: '))
        maximum_heart_rate = 220 - age
        target_heart_rate = maximum_heart_rate / 2
        target_heart_rate_2 = 85 * maximum_heart_rate / 100
        print(f'Maximum heart rate: {maximum_heart_rate}bpm')
        print(f'Target heart rate is {target_heart_rate}bpm to {target_heart_rate_2}bpm.')

    @staticmethod
    def turing_test():
        problem = input('What is your problem? ')
        history = input(f'Have you had this problem {problem} before? (yes or no)')
        if history == 'yes':
            print('Then you have this problem again.')
        elif history == 'no':
            print('Well, you have it now.')
        elif history != 'yes' and history != 'no':
            while history != 'yes' and history != 'no':
                if history == 'yes' or history == 'no':
                    break
                else:
                    print('Please, enter yes or no')
                    history = input('Have you had this problem before?')
                    if history == 'yes':
                        print('Then you have this problem again.')
                    elif history == 'no':
                        print('Well, you have it now.')

    @staticmethod
    def flu():
        total_cases = 0
        smallest_case = 9999999
        largest_case = 0
        for i in range(0, 7):
            cases = int(input('Enter the number of cases for the day: '))
            if cases < smallest_case:
                smallest_case = cases
            elif cases > largest_case:
                largest_case = cases
            total_cases += cases
        average_of_all_cases = total_cases / 7
        print(f'Total cases for week is {total_cases}')
        print(f'Average cases for week is {average_of_all_cases}')
        print(f'Smallest case is {smallest_case}')
        print(f'Largest case is {largest_case}')

    @staticmethod
    def equilateral_triangle(side_1, side_2, side_3):
        if side_1 == side_2 and side_2 == side_3:
            print('Equilateral triangle')
        else:
            print('Not an equilateral triangle')

    @staticmethod
    def fibonacci(position):
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

    @staticmethod
    def palindrome(number):
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

    @staticmethod
    def extract(number):
        while number != 0:
            rem = number % 10
            number //= 10
            print(rem, end=' ')

    @staticmethod
    def multiplication_table():
        for number in range(1, 11):
            for multiply in range(1, 10):
                print(number * multiply, end=' ')
            print('\n')
