# Input a sentence
sentence = input("Enter a sentence: ")

# Split the sentence into words
words = sentence.split()

# Find the longest word using max() with key = len
longest_word = max(words, key=len)

# Display result
print(f"The longest word is: '{longest_word}' with length {len(longest_word)}")
