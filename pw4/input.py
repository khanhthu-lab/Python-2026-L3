# input.py
# Module for input: everything that asks the user to type something.

import math
from domains import Student, Course, find_course


def input_students(students):
    n = int(input("Number of students in the class: "))
    for i in range(n):
        print("Student", i + 1)
        s = Student()
        s.input()
        students.append(s)


def input_courses(courses):
    n = int(input("Number of courses: "))
    for i in range(n):
        print("Course", i + 1)
        c = Course()
        c.input()
        courses.append(c)


def list_courses(courses):
    print("\n--- Courses ---")
    for c in courses:
        c.list()


def input_marks(students, courses):
    """Select a course, then input a mark for every student."""
    if len(courses) == 0 or len(students) == 0:
        print("Please input students and courses first.")
        return

    list_courses(courses)
    course = find_course(courses, input("Select a course by id: "))
    if course is None:
        print("Course not found.")
        return

    for s in students:
        mark = float(input("  Mark of " + s.get_name() + ": "))
        mark = math.floor(mark * 10) / 10              # round DOWN to 1 decimal
        while not course.set_mark(s.get_id(), mark):
            mark = float(input("  Mark must be from 0 to 20, again: "))
            mark = math.floor(mark * 10) / 10


def input_all_marks(students, courses):
    """Keep inputting marks, course by course, until the user says no."""
    while True:
        input_marks(students, courses)
        again = input("Input marks for another course? (y/n): ")
        if again != "y":
            break
