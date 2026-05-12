student = {}

while True:
    print("student manager app-----")
    print("1-add student")
    print("2-view student")
    print("3-check result")
    print("4-exit")

    choice = input("enter your input: ")

    if choice == ("1"):
        name = input("enter name: ")
        marks = int(input("enter marks: "))
        student [name] = marks
        print(f"{name} added sucessfully")
        file = open("student.txt" , "w")
        file.write(str(student))
        file.close()
    
    elif choice == ("2"):
        
        if not student :
            print("no student found")

        else:
            for name ,marks in student.items():
                print(name , ":" , marks )

    elif choice == ("3"):
        name = input("enter student name: ")

        if name in student:
            marks == student[name]
            if marks >= 33:
                print(marks,"%..pass")
            else:
                print("fail")
        
        else:
            print("no student found")

    elif choice == ("4"):
        print("thank you , exiting")

        break
else :
        print("invalid input")
         