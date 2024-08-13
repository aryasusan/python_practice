salary = int(input("Enter your salary: "))
experience = int(input("Enter your years of experience: "))
if (experience >= 5):
    bonus = (salary * 5)/100
    print(bonus, "bonus")
else:
    print("No bonus")
