# dictionary:
#
#     - key-value pair
#     - name:arya
#     - age:31
#     - empty dictionary: dic={}
#      - multiple values can be given to a key usin[]
dic1 = {'id':31,'name':'arya','age':[21,24]}
print(dic1)
print(len(dic1['age']))
dic1['age'].append(24)
print(dic1)

    # - supports heterogeneous data
    # - insertion order is preserved
    # - do not supports duplicate key, but  supports duplicate values
    # - is mutable

 # key can support multiple values as a list
