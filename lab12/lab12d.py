file1 = r"D:\Python\ict.txt"
file2 = r"D:\Python\data-1.csv"
merged_file = r"D:\Python\merged.txt"

try:
    with open(file1, "r") as f1:
        data1 = f1.read()

    with open(file2, "r") as f2:
        data2 = f2.read()

    with open(merged_file, "w") as mf:
        mf.write(data1 + "\n" + data2)

    print("Merged ict.txt and data-1.csv successfully!")

except FileNotFoundError:
    print("One of the files was not found. Check file paths.")
