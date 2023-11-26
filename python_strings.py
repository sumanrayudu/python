
#---------------------------------------------------------------
input_value = "This is a sentence that contains words"

# Split the input string into words
words = input_value.split()
print(words)

# Calculate the total number of words
num_words = len(words)
print("Total number of words:", num_words)

# Find the longest word
longest_word = max(words, key=len)
longest_word_length = len(max(words, key=len))

shortest_word = min(words, key=len)
shortest_word_length = len(min(words, key=len))
# Print the results
print("Total number of words:", num_words)
print("Longest word:", longest_word)
print("longest_word_length :", longest_word_length)
print("shortest word:", shortest_word)
print("shortest_word_length :", shortest_word_length)


#---------------------------------------------------------------
"""
first_name = input()
last_name = input()
full_name = first_name +' '+ last_name
fuller_name = first_name + last_name
print(full_name)
word = full_name.split()
print(word, type(word), len(word))
print(fuller_name)
word_char = fuller_name.split()
print(word_char, type(word_char), len(word_char))

full_namee = first_name +'|'+ last_name
words = full_name.split(sep = '|')
print('full_namee =', words, type(words), len(words))
#---------------------------------------------------------------
"""
#---------------------------------------------------------------
string1 = 'abcabc'
rev = string1[::-1]
print(rev)

[character for character in string1]

#---------------------------------------------------------------