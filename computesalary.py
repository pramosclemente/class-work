def computepay(h, r):
    if h > 40:
        pay = (40 * r) + (h - 40) * (r * 1.5)
    else:
        pay = h * r
    return pay
try:
    hours = float(input('Enter Hours: '))
    rate = float(input('Enter Rate: '))
except:
    print ("")
    print ("Enter a number")
    quit()
total = computepay(h,r)
print("")
print ("Pay: $",total)



