# student_marks.py
# Practical work 1: student mark management

students = []   # [{"id": ..., "name": ..., "dob": ...}, ...]
courses = []    # [{"id": ..., "name": ...}, ...]
marks = {}      # {course_id: {student_id: mark}}


# ---------- Input functions ----------

def input_number_of_students():
    return int(input("Number of students in the class: "))


def input_student_info():
    student_id = input("Student id: ")
    name = input("Student name: ")
    dob = input("Student DoB (dd/mm/yyyy): ")
    return {"id": student_id, "name": name, "dob": dob}


def input_number_of_courses():
    return int(input("Number of courses: "))


def input_course_info():
    course_id = input("Course id: ")
    name = input("Course name: ")
    return {"id": course_id, "name": name}


def input_marks_for_course():
    if not courses or not students:
        print("Please input students and courses first.")
        return

    list_courses()
    course_id = input("Select a course by id: ")

    # Check that the course really exists
    if course_id not in [c["id"] for c in courses]:
        print("Course not found.")
        return

    marks[course_id] = {}
    for s in students:
        mark = float(input(f"Mark of {s['name']} ({s['id']}): "))
        marks[course_id][s["id"]] = mark


# ---------- Listing functions ----------

def list_courses():
    print("\n--- Courses ---")
    for c in courses:
        print(f"{c['id']}: {c['name']}")


def list_students():
    print("\n--- Students ---")
    for s in students:
        print(f"{s['id']} | {s['name']} | {s['dob']}")


def show_student_marks():
    course_id = input("Enter course id to show marks: ")
    if course_id not in marks:
        print("No marks for this course yet.")
        return

    print(f"\n--- Marks for course {course_id} ---")
    for s in students:
        mark = marks[course_id].get(s["id"], "N/A")
        print(f"{s['name']} ({s['id']}): {mark}")


# ---------- Main program ----------

def main():
    n_students = input_number_of_students()
    for i in range(n_students):
        print(f"Student {i + 1}:")
        students.append(input_student_info())

    n_courses = input_number_of_courses()
    for i in range(n_courses):
        print(f"Course {i + 1}:")
        courses.append(input_course_info())

    input_marks_for_course()

    list_courses()
    list_students()
    show_student_marks()

main()