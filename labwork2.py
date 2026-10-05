# ---------- Classes ----------

class Entity:
    def __init__(self, entity_id="", name=""):
        self.__id = entity_id
        self.__name = name

    # getters / setters
    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def set_id(self, entity_id):
        self.__id = entity_id

    def set_name(self, name):
        self.__name = name

    def input(self):
        self.__id = input("Id: ")
        self.__name = input("Name: ")

    def list(self):
        print(self.__id, "|", self.__name)


class Student(Entity):
    def __init__(self, student_id="", name="", dob=""):
        super().__init__(student_id, name)
        self.__dob = dob

    def get_dob(self):
        return self.__dob

    def input(self):                   
        super().input()                
        self.__dob = input("  DoB (dd/mm/yyyy): ")

    def list(self):                    
        print(self.get_id(), "|", self.get_name(), "|", self.__dob)


class Course(Entity):
    def __init__(self, course_id="", name=""):
        super().__init__(course_id, name)
        self.__marks = {}              # {student_id: mark}

    def set_mark(self, student_id, mark):
        if mark < 0 or mark > 20:
            return False
        self.__marks[student_id] = mark
        return True

    def get_mark(self, student_id):
        return self.__marks.get(student_id)    # None if no mark yet


# ---------- Data ----------

students = []
courses = []


# ---------- Input functions ----------

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
        print("Course ", i + 1)
        c = Course()
        c.input()
        courses.append(c)


def find_course(course_id):
    for c in courses:
        if c.get_id() == course_id:
            return c
    return None


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
        while not course.set_mark(s.get_id(), mark):
            mark = float(input("  Mark must be from 0 to 20, again: "))


# ---------- Listing functions ----------

def list_courses():
    print("\n--- Courses ---")
    for c in courses:
        c.list()


def list_students():
    print("\n--- Students ---")
    for s in students:
        s.list()


def show_marks():
    course = find_course(input("Enter course id to show marks: "))
    if course is None:
        print("Course not found.")
        return

    print("\n--- Marks for course", course.get_id(), "---")
    for s in students:
        mark = course.get_mark(s.get_id())
        if mark is None:
            mark = "N/A"
        print(s.get_name(), "(" + s.get_id() + "):", mark)


# ---------- Main ----------

input_students()
input_courses()
input_marks()

list_courses()
list_students()
show_marks()