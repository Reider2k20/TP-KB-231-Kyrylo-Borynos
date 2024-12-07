import unittest
import unittest.mock
from io import StringIO
import sys
import os
import tempfile
import csv

from .Student import Student
from .Student_list import StudentList
from .File_in_out import FileInOut

class TestStudenList(unittest.TestCase):
    def setUp(self):
        self.test_file = tempfile.NamedTemporaryFile('w', encoding='utf-8',  newline='', delete=False)
        self.test_file_name = self.test_file.name
        self.test_file.close()
        self.students_list = StudentList()
        self.students_list.students = []


    def tearDown(self):
        if os.path.exists(self.test_file_name):
            os.remove(self.test_file_name)


    def test_addNewElement(self):
        input_data = Student(name="Test", phone="0662835915", group="KB-231", debt="1500")
        self.students_list.addNewElement(input_data)

        self.assertEqual(len(self.students_list.students), 1)
        self.assertEqual(self.students_list.students[0].name, "Test")
        self.assertEqual(self.students_list.students[0].phone, "0662835915")
        self.assertEqual(self.students_list.students[0].group, "KB-231")
        self.assertEqual(self.students_list.students[0].debt, "1500")


    def test_deleteElement(self):
        input_data = Student(name="Test", phone="0662835915", group="KB-231", debt="1500")
        self.students_list.addNewElement(input_data)

        self.students_list.deleteElement("Test")

        self.assertEqual(len(self.students_list.students), 0)


    def test_updateElement(self):
        input_data = Student(name="Test", phone="0662835915", group="KB-231", debt="1500")
        self.students_list.addNewElement(input_data)
        updated_data = Student(name="Test Updated", phone="0669999999", group="KB-232", debt="800")

        self.students_list.updateElement(0, updated_data)

        self.assertEqual(len(self.students_list.students), 1)
        self.assertEqual(self.students_list.students[0].name, "Test Updated")
        self.assertEqual(self.students_list.students[0].phone, "0669999999")
        self.assertEqual(self.students_list.students[0].group, "KB-232")
        self.assertEqual(self.students_list.students[0].debt, "800")
    

    def test_import_data(self):
        data = [
            {"name": "Alice", "phone": "0664682546", "group": "KB-231", "debt": "300"},
            {"name": "Bob", "phone": "0666483595", "group": "KB-232", "debt": "700"}
        ]
        with open(self.test_file_name, 'w', encoding='utf-8', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=["name", "phone", "group", "debt"])
            writer.writeheader()
            writer.writerows(data)

        students = FileInOut.import_data(self.test_file_name)

        self.assertEqual(len(students), 2)
        self.assertEqual(students[0].name, "Alice")
        self.assertEqual(students[1].name, "Bob")
        self.assertEqual(students[0].group, "KB-231")
        self.assertEqual(students[1].group, "KB-232")


    def test_save_data(self):
        student_list = [ Student(name="Chris", phone="0667777777", group="KB-232", debt="500") ]
        FileInOut.save_data(self.test_file_name, student_list)

        with open(self.test_file_name, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            rows = list(reader)

            self.assertEqual(len(rows), 1)
            self.assertEqual(rows[0]["name"], "Chris")
            self.assertEqual(rows[0]["phone"], "0667777777")
            self.assertEqual(rows[0]['group'], "KB-232")
            self.assertEqual(rows[0]['debt'], "500")


    def test_printAllList(self):
        input_data = Student(name="Test", phone="0667777777", group="KB-232", debt="100")
        self.students_list.addNewElement(input_data)

        captured_output = StringIO()
        sys.stdout = captured_output
        self.students_list.printAllList()
        sys.stdout = sys.__stdout__

        self.assertIn("Test", captured_output.getvalue())

if __name__ == '__main__':
    unittest.main()
