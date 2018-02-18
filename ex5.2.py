count = 0
total = 0
smallest = None
largest = None
while True:
    number = input("Enter a number: ")
    if number == "done" :
        break
    try:
        num = float(number)
    except:
        print("Invalid input")
        continue
    count = count + 1
    total = total + num
    if smallest is None or num < smallest:
            smallest = num
    if largest is None or num > largest:
            largest = num
print("")
print("Sum =", total)
print("Count =", count)
print("Maximum =", largest)
print("Minimum =", smallest)