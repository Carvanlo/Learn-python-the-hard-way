x = "There are %d types of people." % 10  # signed integer decimal
binary = "binary"
do_not = "dont't"
y = "Those who know %s and those who %s." % (binary, do_not)  # first places

print x
print y

print "I said: %r." % x   # second places
print "I also said: '%s'." % y  # third places

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious    # fourth places

w = "This is the left side of..."
e = "a string with a right side."

print w + e
