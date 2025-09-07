# Input a sentence
sentence = input("Enter a sentence: ")

# Remove extra spaces and split into words
words = sentence.strip().split()

# Get the last word
last_word = words[-1]

# Display result
print(f"The last word is: '{last_word}' and its length is {len(last_word)}")
