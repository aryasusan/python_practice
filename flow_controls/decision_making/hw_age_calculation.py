# birth year
# birth month corresponding number
# birth date
#
# current year
# current month number
# current date
#
# calculate age without month

birth_year = int(input("Enter birth year"))
birth_month = int(input("Enter birth month"))
birth_date = int(input("Enter birth date"))

current_year = int(input("Enter current year"))
current_month = int(input("Enter current month"))
current_date = int(input("Enter current date"))

if(birth_year <= current_year):
    if(birth_month < current_month):
        age = current_year - birth_year
    elif(birth_month == current_month):
        if(birth_date <= current_date):
            age = current_year - birth_year
        else:
            age = (current_year-1) - birth_year
    else:
        age = (current_year - 1) - birth_year

    print("Age is", age)

else:
    print("Age is 0")