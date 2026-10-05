import math
import numpy as np
import curses


# ---------- Classes ----------

class Entity:
    def __init__(self, entity_id="", name=""):
        self.__id = entity_id
        self.__name = name

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def input(self):
        self.__id = input("Id: ")
        self.__name = input("Name: ")

    def __str__(self):
        return self.__id + " | " + self.__name

    def list(self):
        print(self)                    # print() uses __str__


class Student(Entity):
    def __init__(self, student_id="", name="", dob=""):
        super().__init__(student_id, name)
        self.__dob = dob

    def input(self):
        super().input()
        self.__dob = input("DoB (dd/mm/yyyy): ")

    def __str__(self):
        return super().__str__() + " | " + self.__dob


class Course(Entity):
    def __init__(self, course_id="", name="", credit=0):
        super().__init__(course_id, name)
        self.__credit = credit
        self.__marks = {}              # {student_id: mark}

    def get_credit(self):
        return self.__credit

    def input(self):
        super().input()
        self.__credit = int(input("Credits: "))

    def __str__(self):
        return super().__str__() + " | " + str(self.__credit) + " credits"

    def set_mark(self, student_id, mark):
        if mark < 0 or mark > 20:
            return False
        self.__marks[student_id] = mark
        return True

    def get_mark(self, student_id):
        return self.__marks.get(student_id)


# ---------- Data ----------

students = []
courses = []


# ---------- Input functions (normal terminal) ----------

def input_students():
    n = int(input("Number of students in the class: "))
    for i in range(n):
        print("Student ", i + 1)
        s = Student()
        s.input()
        students.append(s)


def input_courses():
    n = int(input("Number of courses: "))
    for i in range(n):
        print("Course", i + 1)
        c = Course()
        c.input()
        courses.append(c)


def find_course(course_id):
    for c in courses:
        if c.get_id() == course_id:
            return c
    return None


def list_courses():
    print("\n--- Courses ---")
    for c in courses:
        c.list()


def input_marks():
    if len(courses) == 0 or len(students) == 0:
        print("Please input students and courses first.")
        return

    list_courses()
    course = find_course(input("Select a course by id: "))
    if course is None:
        print("Course not found.")
        return

    for s in students:
        mark = float(input("  Mark of " + s.get_name() + ": "))
        mark = math.floor(mark * 10) / 10             
        while not course.set_mark(s.get_id(), mark):
            mark = float(input("  Mark must be from 0 to 20, again: "))
            mark = math.floor(mark * 10) / 10


# ---------- numpy: GPA and sorting ----------

def calculate_gpa(student):
    mark_list = []
    credit_list = []
    for c in courses:
        mark = c.get_mark(student.get_id())
        if mark is not None:
            mark_list.append(mark)
            credit_list.append(c.get_credit())

    if len(mark_list) == 0:
        return 0.0

    mark_array = np.array(mark_list)
    credit_array = np.array(credit_list)
    return float(np.sum(mark_array * credit_array) / np.sum(credit_array))


def sort_students_by_gpa():
    gpa_list = []
    for s in students:
        gpa_list.append(calculate_gpa(s))

    gpa_array = np.array(gpa_list)
    order = np.argsort(-gpa_array, kind="stable")      # indexes, GPA descending

    result = []
    for i in order:
        result.append(students[i])
    return result


# ---------- curses: decorated output ----------

def show_screen(stdscr, title, lines):
    height, width = stdscr.getmaxyx()
    stdscr.clear()
    stdscr.border()
    stdscr.addstr(1, 2, "=== " + title + " ===", curses.color_pair(1) | curses.A_BOLD)

    row = 3
    for line in lines:
        if row >= height - 3:
            break                                      # do not draw outside the window
        stdscr.addstr(row, 2, line[:width - 4], curses.color_pair(3))
        row += 1

    stdscr.addstr(height - 2, 2, "Press any key to go back...", curses.color_pair(2))
    stdscr.refresh()
    stdscr.getch()


def screen_courses(stdscr):
    lines = []
    for c in courses:
        lines.append(str(c))
    show_screen(stdscr, "Courses", lines)


def screen_students(stdscr):
    lines = []
    rank = 1
    for s in sort_students_by_gpa():
        gpa = calculate_gpa(s)
        lines.append(f"{rank}. {s}  |  GPA: {gpa:.2f}")
        rank += 1
    show_screen(stdscr, "Students (GPA high to low)", lines)


def screen_marks(stdscr):
    stdscr.clear()
    stdscr.border()
    stdscr.addstr(1, 2, "Enter course id: ", curses.color_pair(2))
    curses.echo()                                      # show what the user types
    course_id = stdscr.getstr().decode("utf-8")
    curses.noecho()

    course = find_course(course_id)
    if course is None:
        show_screen(stdscr, "Marks", ["Course not found."])
        return

    lines = []
    for s in students:
        mark = course.get_mark(s.get_id())
        if mark is None:
            mark = "N/A"
        lines.append(s.get_name() + " (" + s.get_id() + "): " + str(mark))
    show_screen(stdscr, "Marks of " + course.get_name(), lines)


def menu(stdscr):
    curses.start_color()
    curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)     # titles
    curses.init_pair(2, curses.COLOR_YELLOW, curses.COLOR_BLACK)   # hints
    curses.init_pair(3, curses.COLOR_GREEN, curses.COLOR_BLACK)    # content

    while True:
        stdscr.clear()
        stdscr.border()
        stdscr.addstr(1, 2, "STUDENT MARK MANAGEMENT", curses.color_pair(1) | curses.A_BOLD)
        stdscr.addstr(3, 4, "1. List courses", curses.color_pair(3))
        stdscr.addstr(4, 4, "2. List students (sorted by GPA)", curses.color_pair(3))
        stdscr.addstr(5, 4, "3. Show marks of a course", curses.color_pair(3))
        stdscr.addstr(6, 4, "q. Quit", curses.color_pair(3))
        stdscr.refresh()

        key = stdscr.getch()
        if key == ord("1"):
            screen_courses(stdscr)
        elif key == ord("2"):
            screen_students(stdscr)
        elif key == ord("3"):
            screen_marks(stdscr)
        elif key == ord("q"):
            break


# ---------- Main ----------

input_students()
input_courses()

while True:
    input_marks()
    again = input("Input marks for another course? (y/n): ")
    if again != "y":
        break

curses.wrapper(menu)                 