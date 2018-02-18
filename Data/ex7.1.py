fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:',fname)
    exit()
for line in fhand:
    inp = fhand.read()
    new_inp = inp.upper()
    print(new_inp)