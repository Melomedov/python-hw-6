from datetime import date, datetime, timedelta
from typing import List
from university import Course, Mentor, Teacher, Student, University, UniversityEmployee

python_course = Course("Python", datetime.now(), datetime.now() + timedelta(days=30))
js_course = Course("JavaScript", datetime.now(), datetime.now() + timedelta(days=60))

alex_student = Student("Alex", "Stp", date(1995, 7, 8))
nik_student = Student("Nik", "Fial", date(1998, 10, 22))

bred_teacher = Teacher("Bred", "Cmp", date(1974, 6, 25), 2000, python_course)

koli_mentor = Mentor("Koli", "Key", date(1987, 3, 13), 1200, [python_course, js_course])

harvard_university = University(
    "Harvard",
    [python_course, js_course],
    [bred_teacher, koli_mentor],
    [alex_student, nik_student],
)
# print(Course.is_active(python_course))
# print(UniversityEmployee.get_yearly_salary(bred_teacher))
# print(Teacher.answer_question(bred_teacher, python_course, 'wazzap'))
# print(Teacher.answer_question(bred_teacher, js_course, 'wazzap'))
# print(Teacher.change_course(bred_teacher,js_course))
# print(Teacher.change_course(bred_teacher,python_course))
# print(Mentor.answer_question(koli_mentor, [python_course, js_course], "Wazzap"  ))
# print(Mentor.answer_question(koli_mentor, [python_course, js_course], "Wazzap"  ))  
# print(Mentor.answer_question(koli_mentor, [python_course, js_course], "Wazzapv"  )) 
# print(Mentor.answer_question(koli_mentor, [python_course, js_course], "Wazzv"  ))
# print(Mentor.answer_question(koli_mentor, [python_course, js_course], "Wazza"  ))  
# print (Mentor.change_courses(koli_mentor, [js_course, python_course]))
# print(Student.add_mark(nik_student, 11))
# print(Student.add_mark(nik_student, 13))
# print(Student.add_mark(nik_student, 9))
# print(Student.add_mark(alex_student, 11))
# print(Student.get_all_marks(nik_student))
# print(Student.get_avarage_mark(nik_student))
# print(Student.get_average_by_last_n_marks(nik_student,2))
# print(University.get_average_salary(harvard_university))
# print(University.get_average_marks(harvard_university))
print(University.get_active_courses(harvard_university))