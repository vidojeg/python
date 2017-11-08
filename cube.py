from random import *

mini = 1
maxi = 6


def randomly():
    x = randint(mini, maxi)
    print x


while (1):
    print ("Would you like run again:")
    text = raw_input("")

    if text == "":
        randomly()
    elif text == "no":
        print "Good bye"
        break
