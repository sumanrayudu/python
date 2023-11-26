
list1 = [10,20,30,40,50]
list2 = [15,25,42,100]

combined_list = list1 + list2

n = len(combined_list)
for i in range(n):
    for j in range(0, n-i-1):
        if combined_list[j] > combined_list[j+1]:
            combined_list[j], combined_list[j+1] = combined_list[j+1], combined_list[j]

print(combined_list) 


