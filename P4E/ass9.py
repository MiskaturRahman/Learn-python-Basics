name = input("enter file: ")
if len(name) < 1:
    name = 'mbox-short.txt'
handle = open(name)
counts = dict()

for line in handle:
    if line.startswith('From '):
        line.split()
        counts[line[1]] = counts.get[line[1], 0] + 1

bigword = none
bigcount = 0

for key, val in counts.items():
    if bigcount == 0 or val > bigcount:
        bigcount = val
        bigword = key
print(bigword, bigcount)
