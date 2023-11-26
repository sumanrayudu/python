
# Len, Append and Pop 


data = [1,5,2,4,7,11,10,15]
data_value = [18,15,32,24,17,11,510,715]
string_list = ['a', 'b','c','f','d','e','z']

x = len(data)
y = len(string_list)

print(x,y)
print(data[1:5])
print(data[::-1])
#print(data(1))
sorted_list = sorted(data)
max_value = max(data)
min_value = min(data)
print(sorted_list)
print(max_value, min_value)

print("data",data)
print("new list ",data.append(data_value))



input = "Hello World , I Am Here"
Output = "Here Am I , Hello World"
sentence  = "Hello World , I Am Here"
words = sentence.split(",")
word = words[1].split(" ")
rev_words = word[::-1]

print(rev_words,words[0])








