count = 0
total = 0
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
print("")
print("Sum =", total)
print("Count =", count)
print("Average =", total/count)
