count = 0
total = 0.0
fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:',fname)
    exit()
for line in fhand:
    if line.startswith('X-DSPAM-Confidence:'):
        num = float(line[20:])
        count = count + 1
        total = total + num
print("Average spam confidence= ", total/count)