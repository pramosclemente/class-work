def count(w,l):
    total = 0
    for letter in w:
        if letter == l:
            total = total + 1
    return total
word = input("Enter the word: ")
letter = input("Enter the letter: ")
tw = count(word,letter)
print("Total count of ",letter,"is: ", tw)

