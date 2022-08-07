from datetime import date, timedelta
import datetime
from unittest import TestCase
from university import Course, Mentor, Teacher, Student, University
import main

class courseTestCase(TestCase):
    def setUp(self):
        test_student = Student("Test_name", "Test_last_name", date(1995, 7, 8))
        python_course = Course("Python", datetime.now(), datetime.now() + timedelta(days=30))
    def test_is_active(self):
        
