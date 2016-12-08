# A program to calculate the credit card balance after one year if a person only pays the minimum monthly
# payment required by the credit card company each month.

# example
balance = 484
annualInterestRate = 0.2
monthlyPaymentRate = 0.04


def remainingBalance(balance, annualInterestRate, monthlyPaymentRate):
    for i in range(12):
        balance = (balance - balance * monthlyPaymentRate) + annualInterestRate/12 *\
                                                             (balance - balance * monthlyPaymentRate)
        print(str(round(balance, 2)))

remainingBalance(balance, annualInterestRate, monthlyPaymentRate)