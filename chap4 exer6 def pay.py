def computepay(rrate,hhours):
    rate = float(rrate)
    hours = float(hhours)
    if hours > 40:
        pay = 40 * rate + (hours - 40) * (rate * 1.5)
    else:
        pay = hours * rate

    print(pay)


computepay(1,41)