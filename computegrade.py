def computegrade(score):
    if score >= 0.9:
        print('A')
    elif score >= 0.8:
        print('B')
    elif score >= 0.7:
        print('C')
    elif score >= 0.6:
        print('D')
    else:
        print('F')
while True:
    entry = float(input("Enter Score between 0.0 and 1: "))
    if entry >= 0.0 and entry <= 1.0:
        computegrade(entry)
    if entry == " ":
        print("Enter Score between 0.0 and 1")
    else:
        print("Bad Score")
        quit()


