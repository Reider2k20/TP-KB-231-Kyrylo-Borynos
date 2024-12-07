from sys import argv
from Student import Student
from Student_list import StudentList
from File_in_out import FileInOut

DEF_NAME = "lab3_data.csv"

def main():

    if len(argv) == 1:
        data_file = DEF_NAME
    else:
        data_file = argv[1]
    
    print(f"File used '{data_file}'")
    students = FileInOut.import_data(data_file)
    student_list = StudentList(students)


    while True:
        chouse = input("Please specify the action [ C create, U update, D delete, P print,  X exit ] ")
        match chouse:
            case "C" | "c":
                name = input("Enter name: ") or "Unknown"
                phone = input("Enter phone: ") or "Unknown"
                group = input("Enter group: ") or "Unknown"
                debt = input("Enter debt: ") or "Unknown"
                student = Student(name=name, phone=phone, group=group, debt=debt)
                student_list.addNewElement(student)
            case "U" | "u":
                name = input("Enter name to update: ")
                index_update = student_list.findElement(name)
                if index_update == -1:
                    print ("Element was not found")
                    continue
                cur_inf = student_list.students[index_update]
                print(f"Student current iformation: {cur_inf}")

                name = input("Enter new name or press Enter to skip: ") or cur_inf.name
                phone = input("Enter new phone or press Enter to skip: ") or cur_inf.phone
                group = input("Enter new group or press Enter to skip: ") or cur_inf.group
                debt = input("Enter new debt or press Enter to skip: ") or cur_inf.debt

                new_data = Student(name=name, phone=phone, group=group, debt=debt)
                student_list.updateElement(index_update, new_data)
            case "D" | "d":
                name = input("Enter name to delete: ")
                student_list.deleteElement(name)
            case "P" | "p":
                student_list.printAllList()
            case "X" | "x":
                FileInOut.save_data(data_file, student_list.students)
                print("Exiting program.")
                break
            case _:
                print("Invalid choice.")

if __name__ == "__main__":
    main()
