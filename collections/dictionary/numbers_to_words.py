num = int(input("Enter the number between 0 and 999"))
if not 0<=num<=999:
    print("Number out of range")

if num==0:
    print("zero")

ones = {
        0:"",1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",
        8:"eight",9:"nine"
    }
teens = {
        11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen", 15: "fifteen",
        16: "sixteen", 17: "seventeen", 18: "eighteen", 19: "nineteen"
    }
tens = {
        10: "ten", 20: "twenty", 30: "thirty", 40: "forty", 50: "fifty", 60: "sixty",
        70: "seventy", 80: "eighty", 90: "ninety"
    }

words = []

if(num//100 >0):
    words.append(ones[num//100])
    words.append('hundred')
    num%=100
if(10<num<20):
    words.append(teens[num])
else:
    if(num//10>0):
        words.append(tens[(num//10)*10])
        num%=10
    if(num>0):
        words.append(ones[num])
print(" ".join(words))