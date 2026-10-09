# domains/course.py

from domains.entity import Entity


class Course(Entity):
    def __init__(self, course_id="", name="", credit=0):
        super().__init__(course_id, name)
        self.__credit = credit
        self.__marks = {}              # {student_id: mark}

    def get_credit(self):
        return self.__credit

    def input(self):
        super().input()
        self.__credit = int(input("  Credits: "))

    def __str__(self):
        return super().__str__() + " | " + str(self.__credit) + " credits"

    def set_mark(self, student_id, mark):
        """Save the mark if it is valid. Return True if saved, else False."""
        if mark < 0 or mark > 20:
            return False
        self.__marks[student_id] = mark
        return True

    def get_mark(self, student_id):
        return self.__marks.get(student_id)    # None if no mark yet


def find_course(courses, course_id):
    """Return the course with this id, or None if there is none."""
    for c in courses:
        if c.get_id() == course_id:
            return c
    return None
