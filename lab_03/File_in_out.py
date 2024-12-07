import csv
from .Student import Student

class FileInOut:
    @staticmethod
    def import_data(file_name):
        students = []
        try:
            with open(file_name, 'r', encoding = 'utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    student = Student(
                        name = row.get("name", "Unknown"), 
                        phone = row.get("phone", "Unknown"), 
                        group = row.get("group", "Unknown"), 
                        debt = row.get("debt", "Unknown")
                    )
                    students.append(student)

        except FileNotFoundError:
            print(f"File '{file_name}' not found \nThe initial list will be empty")
        except Exception as e:
            print(f"File loading error: {e}")
        return students


    @staticmethod
    def save_data(file_name, students):
        students_str = []
        for elem in students:
            students_str.append({
                    "name": elem.name, 
                    "phone": elem.phone, 
                    "group": elem.group, 
                    "debt": elem.debt
                    })
        try:
            with open(file_name, 'w', encoding = 'utf-8', newline = '') as file:
                fieldnames = ["name", "phone", "group", "debt"]
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(students_str)
            print(f"Data successfully saved to '{file_name}'")
        except Exception as e:
            print(f"File saving error: {e}")