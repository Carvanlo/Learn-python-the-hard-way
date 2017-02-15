numbers = []

def add_num(x, y):
    i = 0
    while i < x:
        print "At the top i is %d" % i
        numbers.append(i)

        i = i + y
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i

    print "The numbers: "

    for num in numbers:
        print num

# second version

for i in range(0,6):
    print "At the top i is %d" % i
    numbers.append(i)

print "The numbers: "
for num in numbers:
    print num
