class Loan():
    def __init__(self):
        user_input = []
        try:
            user_input.append(float(input("Please enter the total sum of the loan.\n")))
        except ValueError:
            cause_variable = "sum"
            error_handling(cause_variable)
        try:
            user_input.append(float(input("Please enter the duration time of the loan in years.\n")))
        except ValueError:
            cause_variable = "years"
            error_handling(cause_variable)
        try:
            user_input.append(float(input("Please enter the percentage of the loan (per year).\n")))
        except ValueError:
            cause_variable = "percentage"
            error_handling(cause_variable)

        user_input.append(input("Please specify the rate type of the loan: type 'A' for decreasing rates,"
                                "\nand 'B' for increasing rates.\n"))

        self.sum = user_input[0]
        self.years = user_input[1]
        self.percent_per_year = user_input[2]
        self.rate_type = user_input[3]

        if user_input[3] != 'A' and user_input[3] != 'B':
            cause_variable = "rate_type"
            error_handling(cause_variable)
        else:
            self.rate_type = user_input[3]

    def calculate_rates(self):
        try:
            user_rate_month = int(input("Which month would you like to calculate the rate for? Type a number between 1 and 12.\n"
                                   "Type 0 to terminate the program.\n"))
            if user_rate_month == 0:
                print("See you soon!")
            elif user_rate_month > 0 and user_rate_month < 13:
                if self.rate_type == 'A':
                    rates = []
                    for rate_month in range(1, 13):
                        rate = self.sum / (self.years * 12) * (
                                    1 + (self.years * 12 - rate_month + 1) * (self.percent_per_year/100))
                        rates.append(rate)
                    capital_rate = self.sum / (self.years * 12)
                    interest_rate = self.sum * self.percent_per_year / self.years
                    left_to_pay = self.sum
                    for i in range(0, user_rate_month+1):
                        left_to_pay -= rates[i]
                    print(f"Value of rate nr {user_rate_month}: {rate}")
                    print(f"Capital rate: {capital_rate}")
                    print(f"Interest rate: {interest_rate}")
                    print(f"Still left to pay: {left_to_pay}")
                elif self.rate_type == 'B':
                    q = 1 + (self.percent_per_year/100)/12
                    rates = []
                    for rate_month in range(1, 13):
                        rate = self.sum * q**(self.years * 12) * ((q-1)/(q**(self.years*12)-1))
                        rates.append(rate)
                    capital_rate = self.sum / (self.years * 12)
                    interest_rate = self.sum * self.percent_per_year / self.years
                    left_to_pay = self.sum
                    for i in range(0, user_rate_month):
                        left_to_pay -= rates[i]
                    print(f"Value of rate nr {user_rate_month}: {rate}")
                    print(f"Capital rate: {capital_rate}")
                    print(f"Interest rate: {interest_rate}")
                    print(f"Still left to pay: {left_to_pay}")
                else:
                    raise ValueError(f"Invalid rate_type: {self.rate_type}")

            else:
                raise ValueError()
        except ValueError:
            print("Wrong value for the month, please try again.")
            self.calculate_rates()

def error_handling(cause_variable):
    input_decision = input(
        f"Invalid input for the {cause_variable} variable. Would you like to try again? Type 'yes' or 'no'.\n").lower()
    if input_decision == 'yes':
        user_loan = Loan()
    elif input_decision == 'no':
        print("See you soon!")
    else:
        input_decision = input("Invalid input. Please try again. Type 'yes' to continue or 'no' to exit.\n").lower()
        if input_decision == 'yes':
            user_loan = Loan()
        elif input_decision == 'no':
            print("See you soon!")
        else:
            print('Invalid input once again. Terminating the program.')

def calculate_loan():
    user_loan = Loan()
    if 'user_loan' in locals():
        user_loan.calculate_rates()

calculate_loan()













