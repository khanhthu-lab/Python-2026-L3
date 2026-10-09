# output.py
# Module for curses output: everything that is drawn on the decorated screen.

import curses
from domains import find_course


def show_screen(stdscr, title, lines):
    """Draw a titled screen with a list of text lines, wait for a key."""
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


def screen_courses(stdscr, courses):
    lines = []
    for c in courses:
        lines.append(str(c))
    show_screen(stdscr, "Courses", lines)


def screen_students(stdscr, students, courses):
    """students is expected to be already sorted by GPA."""
    lines = []
    rank = 1
    for s in students:
        gpa = s.calculate_gpa(courses)
        lines.append(f"{rank}. {s}  |  GPA: {gpa:.2f}")
        rank += 1
    show_screen(stdscr, "Students (GPA high to low)", lines)


def screen_marks(stdscr, students, courses):
    stdscr.clear()
    stdscr.border()
    stdscr.addstr(1, 2, "Enter course id: ", curses.color_pair(2))
    curses.echo()                                      # show what the user types
    course_id = stdscr.getstr().decode("utf-8")
    curses.noecho()

    course = find_course(courses, course_id)
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


def menu(stdscr, students, courses):
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
            screen_courses(stdscr, courses)
        elif key == ord("2"):
            screen_students(stdscr, students, courses)
        elif key == ord("3"):
            screen_marks(stdscr, students, courses)
        elif key == ord("q"):
            break


def show(students, courses):
    """Start the curses screens."""
    curses.wrapper(menu, students, courses)
