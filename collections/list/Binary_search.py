# Binary search algorithm
#     sort list in ascending order
#     declare 2 variables: start=0,end=len(lst)-1
#     calculate mid value: mid=(start+end)//2
#         search_element>lst[mid] -- search_element will be in right of mid,
#             so search only in right of mid
#             start = mid+1
#         search_element<lst[mid] -- search_element will be in left of mid,
#             so search only in left of mid
#             end = mid-1
#         search_element==lst[mid] -- found

lst = [10,15,11,8,6,5,25,30,40,50,31,29]
number = int(input("enter the number"))
lst.sort()
start = 0
end= len(lst)-1
found=False
while(start<=end):
    mid = (start + end) // 2
    if(number>lst[mid]):
        start=mid+1
    elif(number<lst[mid]):
        end=mid-1
    elif(number==lst[mid]):
        found=True
        break
if(found):
    print("element found")
else:
    print("Element not found")