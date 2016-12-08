# A program that uses these bounds and bisection search (for more info check out the Wikipedia page on bisection search)
#  to find the smallest monthly payment to the cent (no more multiples of $10) such that we can pay off the debt within
#  a year

# example
balance = 320000
annual_interest_rate = 0.2


def monthly_payment_needed(balance, annual_interest_rate):
    b = balance
    a = annual_interest_rate
    lower_bound = balance / 12
    upper_bound = (balance * (1 + annual_interest_rate / 12) ** 12) / 12.0
    fixed_monthly_payment = round((lower_bound + upper_bound) / 2, 2)
    while True:
        for i in range(1, 13):
            remaining_balance = balance - fixed_monthly_payment
            balance = round(
                (remaining_balance + remaining_balance * annual_interest_rate / 12.0), 2)
        if (abs(balance - 0)) < 0.1:
            print("Lowest Payment: " + str(round((fixed_monthly_payment), 2)))
            break
        else:
            if balance < 0:
                upper_bound = fixed_monthly_payment
            elif balance > 0:
                lower_bound = fixed_monthly_payment
            fixed_monthly_payment = (lower_bound + upper_bound) / 2
            balance = b
            annual_interest_rate = a


monthly_payment_needed(balance, annual_interest_rate)