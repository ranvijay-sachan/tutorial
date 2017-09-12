year = int(input("Enter year..."))

if year % 4 == 0:
    print '{} is Leap'.format(year)
else:
    print "{} is not Leap".format(year)