n = int(input("enter the number of countries"))
countries = set()
for i in range(n):
    print("enter the country")
    countries.add(input())
print(len(countries),"unique countries")
