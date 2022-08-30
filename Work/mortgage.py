# mortgage.py
#
# Exercise 1.7

death = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
month = 1

# extra_payment_start_month = input('extra_payment_start_month : ')
# extra_payment_end_month = input('extra_payment_end_month : ')
# extra_payment = input('extra_payment : ')

extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000

while death > 0:
    # if month <= 12:
    #     rp = payment + int(extra_payment)
    # else:
    #     rp = payment
    if int(extra_payment_start_month) < month <= int(extra_payment_end_month):
        rp = payment + int(extra_payment)
    else:
        rp = payment
    if rp > death:
        rp = death * (1 + rate / 12)

    death = death * (1 + rate / 12) - rp
    total_paid = total_paid + rp
    month += 1
    nowStatus = f'{month-1} {rp} {death}'
    print(nowStatus)
print('Total paid', round(total_paid, 2))
print('Total month', month - 1)


