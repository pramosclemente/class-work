fname = input('Enter the file name: ')
count = 0
try:
    fhand = open(fname)
except:
    if fname == 'na na boo boo':
        print("NA NA BOO BBO TO YOU. You have been punked")
    else:
        print('File cannot be opened:',fname)
    exit()
for line in fhand:
    if line.startswith('Subject'):
        count = count + 1
print("There were {0} subject lines in {1}.".format(str(count), fname))
