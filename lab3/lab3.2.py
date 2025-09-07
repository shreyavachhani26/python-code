
# Input a string
text = input("Enter a string: ")

cleaned_text = text.replace(" ", "").lower()

if cleaned_text == cleaned_text[::-1]:
    print(f"'{text}' is a Palindrome")
else:
    print(f"'{text}' is NOT a Palindrome")
