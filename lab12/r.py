filename = r"D:\Python\data-1.csv"

try:
    with open(filename, "r") as file:
        content = file.read()

        # Count lines
        with open(filename, "r") as f:
            lines = f.readlines()
        
        line_count = len(lines)

        # Word count = number of items separated by commas or spaces
        word_count = len(content.replace(",", " ").split())

        # Character count
        char_count = len(content)

        print("Lines:", line_count)
        print("Words:", word_count)
        print("Characters:", char_count)

except FileNotFoundError:
    print("The file was not found. Please check the path.")
