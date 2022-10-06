if __name__ == '__main__':

        grade = int(input("Enter grade: "))
        if grade >= 90:
            print(f'Congratulations! Your grade of {grade} earns you an A in this course')

    # @staticmethod
    # def box_of(egg):
    #     box = egg // 6
    #     rem = egg % 6
    #     new_box = 6 - rem
    #     if rem == 0:
    #         print(f'{box} boxes are needed.')
    #     else:
    #         print(f'boxes are needed with a remainder of {rem} eggs')
    #         print(f'{new_box} eggs are needed to complete the box.')
    #
    # @staticmethod
    # def bacteria_start_with(bacteria):
    #     print(f'Hour\t\tNumber of Bacteria')
    #     for hours in range(0, 20, 5):
    #         output = bacteria * 2 * hours
    #         print(f'{hours}\t\t\t{output}')
    #
    #
    # @staticmethod
    # def hourly_wage(good , bad, principal):
    #     good_new_hourly_wage = principal * ((1 + 0.03) ** good)
    #     print(f'After {good} years of good reviews, new hourly wage is ${good_new_hourly_wage : .2f}')
    #     bad_new_hourly_wage = principal * ((1 - 0.03) ** bad)
    #     print(f'After {bad} years of bad reviews, ne hourly wage is ${bad_new_hourly_wage : .2f}')
    #
    #
