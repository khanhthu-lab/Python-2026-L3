# domains/student.py

import numpy as np
from domains.entity import Entity


class Student(Entity):
    def __init__(self, student_id="", name="", dob=""):
        super().__init__(student_id, name)
        self.__dob = dob

    def input(self):
        super().input()
        self.__dob = input("  DoB (dd/mm/yyyy): ")

    def __str__(self):
        return super().__str__() + " | " + self.__dob

    def calculate_gpa(self, courses):
        """GPA = sum(credit * mark) / sum(credit), over courses that have a mark."""
        mark_list = []
        credit_list = []
        for c in courses:
            mark = c.get_mark(self.get_id())
            if mark is not None:
                mark_list.append(mark)
                credit_list.append(c.get_credit())

        if len(mark_list) == 0:
            return 0.0

        mark_array = np.array(mark_list)
        credit_array = np.array(credit_list)
        return float(np.sum(mark_array * credit_array) / np.sum(credit_array))
