# Prints today's date with help
# of datetime library
import datetime
#1
today = datetime.datetime.today()
print(f"{today:%B %d, %Y}")
#2

# Python program showing how to use
# string modulo operator(%) to print
# fancier output

# print integer and float value
print("vivaan : %2d, Portal : %5.2f" % (1, 05.333))

# print integer value
print("total : %3d, hours : %2d" % (240, 120))

# print octal value
print("%7.3o" % (25))

# print exponential value
print("%10.3E" % (356.08977))
#3

# Python program showing
# use of format() method

# using format() method
print('I love {} for "{}!"'.format('cse', 'dsa'))

# using format() method and referring
# a position of the object
print('{0} and {1}'.format('cse', 'dsa'))

print('{1} and {0}'.format('cse', 'dsa'))


# the above formatting can also be done by using f-Strings
# Although, this features work only with python 3.6 or above.

print(f"I love {'cse'} for \"{'dsa'}!\"")

# using format() method and referring
# a position of the object
print(f"{'cse'} and {'dsa'}")
