# Namenjen za testiranje test_student.py

import unittest
from student_result import StudentResult

class TestStudentResult(unittest.TestCase):

    def test_add_grade_valid(self):
        student = StudentResult("Petar")
        student.add_grade(8)
        self.assertEqual(student.grades, [8])

    def test_add_grade_invalid_low(self):
        student = StudentResult("Ana")
        with self.assertRaises(ValueError):
            student.add_grade(5)

    def test_add_grade_invalid_high(self):
        student = StudentResult("Marko")
        with self.assertRaises(ValueError):
            student.add_grade(11)

    def test_average_no_grades(self):
        student = StudentResult("Jovan")
        self.assertIsNone(student.average())

    def test_average_some_grades(self):
        student = StudentResult("Ivana")
        student.add_grade(8)
        student.add_grade(9)
        self.assertEqual(student.average(), 8.5)

    def test_average_all_grades_same(self):
        student = StudentResult("Maja")
        student.add_grade(7)
        student.add_grade(7)
        self.assertEqual(student.average(), 7.0)

    def test_all_passed_true(self):
        student = StudentResult("Petra")
        student.add_grade(6)
        student.add_grade(7)
        student.add_grade(9)
        self.assertTrue(student.all_passed())

    def test_all_passed_false(self):
        student = StudentResult("Stefan")
        student.add_grade(6)
        with self.assertRaises(ValueError):  # Očekujemo grešku prilikom dodavanja nevalidne ocene
            student.add_grade(5)  # Ova ocena treba da baci ValueError
        self.assertTrue(student.all_passed())  # Nakon toga, student je položio jer ima samo validnu ocenu


    def test_all_passed_empty(self):
        student = StudentResult("Luka")
        self.assertFalse(student.all_passed())

    def test_add_multiple_grades(self):
        student = StudentResult("Teodora")
        student.add_grade(8)
        student.add_grade(9)
        student.add_grade(7)
        self.assertEqual(student.grades, [8, 9, 7])

if __name__ == '__main__':
    unittest.main()
