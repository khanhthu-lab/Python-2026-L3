# domains/entity.py

class Entity:
    """Base class: anything that has an id and a name (Student, Course)."""

    def __init__(self, entity_id="", name=""):
        self.__id = entity_id
        self.__name = name

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def input(self):
        self.__id = input("  Id: ")
        self.__name = input("  Name: ")

    def __str__(self):
        return self.__id + " | " + self.__name

    def list(self):
        print(self)                    # print() uses __str__
