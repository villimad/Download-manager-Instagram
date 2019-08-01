
with open('text.txt') as f:
    mylist = [line.rstrip('\n') for line in f]

print(mylist)