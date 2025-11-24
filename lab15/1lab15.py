students = {}

def enroll_student():
    roll = input("Enter Roll Number: ")
    name = input("Enter Student Name: ")
    
    print("Enter subjects (comma separated): ")
    subs = input("> ")
    
    # Convert "Maths,Physics" → ["Maths", "Physics"]
    subject_list = [s.strip() for s in subs.split(',')]
    
    students[roll] = {
        "name": name,
        "subjects": subject_list
    }
    
    print("\nStudent enrolled successfully!\n")

def display_student():
    roll = input("Enter Roll Number to view details: ")
    
    if roll in students:
        print("\n--- Student Details ---")
        print("Roll Number:", roll)
        print("Name:", students[roll]["name"])
        print("Enrolled Subjects:")
        for sub in students[roll]["subjects"]:
            print(" -", sub)
    else:
        print("No such student found!")

while True:
    print("\n1. Enroll Student")
    print("2. View Student Details")
    print("3. Exit")
    
    choice = input("Choose option: ")
    
    if choice == "1":
        enroll_student()
    elif choice == "2":
        display_student()
    elif choice == "3":
        break
    else:
        print("Invalid choice!")
