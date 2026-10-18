student = {}

while True:
    print("\n-----STUDENT MANAGER APP-----")
    print("1. Add Student")
    print("2. View Students")
    print("3. Check Student Result")
    print("4. Exit")

    choice = input("Enter your choice: ")

    # Add Student
    if choice == '1':
        name = input("Enter student name: ")
        marks = float(input("Enter student marks: "))
        student[name] = marks
        print(f"Student {name} added successfully!")

    # View Students
    elif choice == "2":
        if not student:
            print("No student found!")
        else:
            for name, marks in student.items():
                print(name, ":", marks)

    # Check Result
    elif choice == "3":
        name = input("Enter student name to check result: ")
        if name in student:
            marks = student[name]
            if marks >= 30:
                print(f"{name} has passed with {marks} marks.")
            else:
                print(f"{name} has failed with {marks} marks.")
        else:
            print(f"Student {name} not found!")

    elif choice == "4":
        print("Exiting the program...")
        break

    else:
        print("Invalid choice! Please select a valid option.")




        


