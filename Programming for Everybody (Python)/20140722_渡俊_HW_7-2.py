# Use the file name mbox-short.txt as the file name
fname = raw_input("Enter file name: ")
fh = open(fname,'r')


totalnumber = 0.0
N = 0
numbers = []
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    numbers.append(line)
    totalnumber = totalnumber + float(numbers[N].strip('X-DSPAM-Confidence:    ').rstrip())
    print totalnumber
    N += 1
    
averagenumber = round(totalnumber /N,12)

print ('Average spam confidence: %f'%averagenumber)
fh.close()
