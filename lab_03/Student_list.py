
class StudentList:
    def __init__(self, students = []):
        self.students = students


    def addNewElement(self, student_add):
        insertPosition = 0
        for item in self.students:
            if student_add.name > item.name:
                insertPosition += 1
            else:
                break
        self.students.insert(insertPosition, student_add)

        print("New element has been added")
        return


    def findElement(self, name):
        for item in self.students:
            if name == item.name:
                return self.students.index(item)
        return -1
    
    
    def deleteElement(self, name):
        index_delete = self.findElement(name)
        if index_delete == -1:
                    print ("Element was not found")
                    return
        print("Delete position " + str(index_delete))
        del self.students[index_delete]
        print("The student was Deleted")
        return


    def updateElement(self, index, new_data):
        element = self.students[index]
        if element.name == new_data.name and element.phone == new_data.phone and element.group == new_data.group and element.debt == new_data.debt:
            print("you haven`t updated student information")
            return
        elif element.name == new_data.name:
            element.phone = new_data.phone
            element.group = new_data.group
            element.debt = new_data.debt
        else:
            
            del self.students[index]
            insertPosition = 0
            for item in self.students:
                if new_data.name > item.name:
                    insertPosition += 1
                else:
                    break
            self.students.insert(insertPosition, new_data)
            print("information has been updated")
        return


    def printAllList(self):
        if not self.students:
            print("The list of students is empty.")
            return
        for student in self.students:
            print(student)
        return
