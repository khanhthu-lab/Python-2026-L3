# main.py
# Main script: only coordinates the other modules.
# Run it with:  python main.py

import numpy as np
import input as inp          # alias! plain "import input" would hide the built-in input()
import output as out


def sort_students_by_gpa(students, courses):
    """Return a new list of students, highest GPA first."""
    gpa_list = []
    for s in students:
        gpa_list.append(s.calculate_gpa(courses))

    gpa_array = np.array(gpa_list)
    order = np.argsort(-gpa_array, kind="stable")      # indexes, GPA descending

    result = []
    for i in order:
        result.append(students[i])
    return result


def main():
    students = []
    courses = []

    inp.input_students(students)
    inp.input_courses(courses)
    inp.input_all_marks(students, courses)

    sorted_students = sort_students_by_gpa(students, courses)
    out.show(sorted_students, courses)


if __name__ == "__main__":
    main()
