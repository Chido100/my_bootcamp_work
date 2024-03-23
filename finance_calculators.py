'''
Start


Create a program that allows a user to access two different financial calculators ('Investment' and 'Bond')

Ask user to enter what type of calculations they want

Do a calculation using provided formulas depending on the user's entry

Display result of calculations


Stop
'''



import math

# Display calculation options for the user
print(
    "investment - to calculate the amount of interest you'll earn on your investment\n"
    "bond       - to calculate the amount you'll have to pay on a home loan\n"
)

# Ask user to enter the type of calculations they want from the above information
while True:
    # Both lower and upper case letters of the calculation options above are accepted 
    calculation = input("Enter either 'investment' or 'bond' from the menu above to proceed: ").lower()

    # Check that program only accepts calculation options provided
    if calculation != 'investment' and calculation != 'bond':
        print("Invalid input! Please enter a valid entry of either 'investment' or 'bond' to proceed.")
        continue

    # Do a 'simple' or 'compound' interest calculation if a user enters 'investment' as calculation option
    elif calculation == 'investment':
        deposit_amount = float(input("Enter amount you are depositing: "))
        interest_rate = float(input("Enter interest rate in percentage (without the '%' sign.): "))
        number_of_years_to_invest = int(input("Enter number of years you plan on investing: "))
        interest = input("Enter 'simple' or 'compound' to calculate interest: ").lower()

        if interest == 'simple':
            # Simple interest formula
            r = interest_rate / 100
            P = deposit_amount
            t = number_of_years_to_invest
            A = P *(1 + r*t)

            # Display simple interest calculation and round the result up to 2 decimal places
            print(f"\nTotal amount after simple interest has been applied ------ £{round(A, 2)}")
            break

        elif interest == 'compound':
            # Compound interest formula
            r = interest_rate / 100
            P = deposit_amount
            t = number_of_years_to_invest
            A = P * math.pow((1 + r), t)
            
            # Display compound interest calculation and round the result up to 2 decimal places
            print(f"\nTotal amount after compound interest has been applied ------ £{round(A, 2)}")
            break


    # Do a bond calculation if user entered 'bond' as option
    elif calculation == 'bond':
        present_value_of_house = float(input("Enter present value of the house: "))
        interest_rate = float(input("Enter the interest rate: "))
        number_of_months_to_repay_bond = int(input("Enter number of months planned to repay the bond: "))

        # Bond repayment formula
        P = present_value_of_house
        i_r = interest_rate / 100
        i = i_r / 12
        n = number_of_months_to_repay_bond
        repayment = (i * P)/(1 - (1 + i)**(-n))

        # Display how much user has to be pay monthly
        print(f"\nAmount to repay each month ----- £{round(repayment, 2)}")
        break





