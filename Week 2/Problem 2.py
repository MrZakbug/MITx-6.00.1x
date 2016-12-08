# A program that calculates the minimum fixed monthly payment needed in order pay off a credit card balance within 12
# months. By a fixed monthly payment, we mean a single number which does not change each month, but instead is a
# constant amount that will be paid each month.

# example
balance = 3329
annualInterestRate = 0.2


def count_balance(minimum_payment, balance, annual_interest_rate):
    for i in range(12):
        unpaidbalance = balance - minimum_payment
        balance = unpaidbalance + unpaidbalance * annual_interest_rate / 12
    return balance


def monthly_payment_needed(balance, annual_interest_rate):
    minimum_payment = round(balance/12, -1)

    while count_balance(minimum_payment, balance, annual_interest_rate) > 0:
        minimum_payment += 10
    print('Lowest Payment: ' + str(minimum_payment))

monthly_payment_needed(balance, annualInterestRate)