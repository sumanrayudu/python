Data ={"Name": "ABC","Employer": "CVS","Address": {"city" :"Dallas,Texas","zip":"75044"},"version": "v1"}

# Extract the zip value from the Data dictionary
zip_value = Data["Address"]["zip"]

Name = Data["Name"]

# Print the zip value
print(zip_value)
print(Name)


dict1 = {"name":"rahul","age":23,"city":"hyd"}

for k, v in dict1.items():
    print(k, v)
    print(dict1.items)






"""
d1={"name":"Steve","age":25, "marks":60}
d2={"name":"Anil","age":23, "marks":75}
d3={"name":"Asha", "age":20, "marks":70}
print(d1.keys)


def returnSum(dict):
 
    sum = 0
    for i in dict.values():
        sum = sum + i
 
    return sum
 
 
# Driver Function
dict = {'a': 100, 'b': 200, 'c': 300}
dict1 = input()
print("Sum :", returnSum(dict))
print("Sum :", returnSum(dict1))


print(dict)
"""

dict1 = {'Jessa': 70, 'Arul': 80, 'Emma': 55}
dict2 = {'Kelly': 68, 'Harry': 50, 'Emma': 66}

# join two dictionaries with some common items
dict1.update(dict2)
dict1.update({'Sam': 32})
print("After Adding dict1", dict1)


Data ={"Name": "ABC","Employer": "CVS","Address": {"city" :"Dallas,Texas","zip":"75044"},"version": "v1"}
print(Data.keys())
print(Data['Address'].keys())
print(Data.items())
print(Data.items())
print(Data['Address'].items())
