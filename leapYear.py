#enter in the two years as prompted, the driver code will display the results

#start of leap function
def leap(year):
    if(year%4==0):
        if(year%100==0):
            if(year%400==0):
                return 0
            else:
                return 1
        else:
            return 0
    else:
        return 1
#end of leap

#driver
year = int(input("Enter year 1: "))
year0 = int(input("Enter year 2: "))


if(leap(year)==0):
    print(year, " is a leap year!")
else:
    print(year, "is not a leap year")

if(leap(year0)==0):
    print(year0, "is a leap year!")
else:
    print(year0, "is not a leap year")
