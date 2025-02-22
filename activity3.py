# Original string
text = "   Python is awesome!   "

# 1. Using lower() to convert to lowercase
lower_text = text.lower()

# 2. Using replace() to change a word in the string
replaced_text = "I like apples".replace("apples", "oranges")

# 3. Using strip() to remove leading and trailing whitespace
stripped_text = text.strip()

# 4. Using find() to locate the position of a substring
sentence = "The quick brown fox"
index_of_fox = sentence.find("fox")

# 5. Using split() to split a string by a delimiter
fruits = "apple,banana,cherry"
split_fruits = fruits.split(",")

# Output results
print("Lowercase Text:", lower_text)
print("Replaced Text:", replaced_text)
print("Stripped Text:", stripped_text)
print("Index of 'fox':", index_of_fox)
print("Split Fruits:", split_fruits)
