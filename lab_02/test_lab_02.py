import unittest
import unittest.mock
from io import StringIO
import sys
import os
import tempfile
import csv


from .lab_02 import students, addNewElement, deleteElement, updateElement, import_data, save_data, printAllList


class TestStudenList(unittest.TestCase):
    def setUp(self):
        self.test_file = tempfile.NamedTemporaryFile('w', encoding='utf-8',  newline='', delete=False)
        self.test_file_name = self.test_file.name
        self.test_file.close()
        students.clear()

    def tearDown(self):
        if os.path.exists(self.test_file_name):
            os.remove(self.test_file_name)

    def test_addNewElement(self):
        input_data = ["Test Student", "0662835915", "KB-231", "1500"]

        with unittest.mock.patch('builtins.input', side_effect=input_data):
            addNewElement()

        self.assertEqual(len(students), 1)
        self.assertEqual(students[0]['name'], "Test Student")
        self.assertEqual(students[0]['phone'], "0662835915")
        self.assertEqual(students[0]['group'], "KB-231")
        self.assertEqual(students[0]['debt'], "1500")

    def test_deleteElement(self):
        students.append({"name": "Test Student", "phone": "0662835915", "group": "KB-231", "debt": "1500"})

        with unittest.mock.patch('builtins.input', return_value="Test Student"):
            deleteElement()

        self.assertEqual(len(students), 0)

    def test_updateElement(self):
        students.append({"name": "Test Student", "phone": "0662835915", "group": "KB-231", "debt": "1500"})
        input_data = ["Test Student", "Updated Student", "0669999999", "KB-232", "800"]

        with unittest.mock.patch('builtins.input', side_effect=input_data):
            updateElement()

        self.assertEqual(len(students), 1)
        self.assertEqual(students[0]['name'], "Updated Student")
        self.assertEqual(students[0]['phone'], "0669999999")
        self.assertEqual(students[0]['group'], "KB-232")
        self.assertEqual(students[0]['debt'], "800")

    def test_import_data(self):
        data = [
            {"name": "Alice", "phone": "0664682546", "group": "KB-231", "debt": "300"},
            {"name": "Bob", "phone": "0666483595", "group": "KB-232", "debt": "700"}
        ]

        with open(self.test_file_name, 'w', encoding='utf-8', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=["name", "phone", "group", "debt"])
            writer.writeheader()
            writer.writerows(data)

        import_data(self.test_file_name)
        
        self.assertEqual(len(students), 2)
        self.assertEqual(students[0]['name'], "Alice")
        self.assertEqual(students[1]['name'], "Bob")
        self.assertEqual(students[0]['group'], "KB-231")
        self.assertEqual(students[1]['group'], "KB-232")

    def test_save_data(self):
        students.append({"name": "Chris", "phone": "0667777777", "group": "KB-232", "debt": "500"})
        save_data(self.test_file_name)

        with open(self.test_file_name, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            rows = list(reader)

            self.assertEqual(len(rows), 1)
            self.assertEqual(rows[0]["name"], "Chris")
            self.assertEqual(rows[0]['phone'], "0667777777")
            self.assertEqual(rows[0]['group'], "KB-232")
            self.assertEqual(rows[0]['debt'], "500")

    def test_printAllList(self):
        students.append({"name": "Test Student", "phone": "0667777777", "group": "KB-232", "debt": "100"})
        captured_output = StringIO()
        sys.stdout = captured_output
        printAllList()
        sys.stdout = sys.__stdout__

        self.assertIn("Test Student", captured_output.getvalue())


if __name__ == '__main__':
    unittest.main()
