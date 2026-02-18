# super_function.py

class Person:
    def __init__(self, name):
        self.name = name
        print("Person constructor called")


class Student(Person):
    def __init__(self, name, grade):
        super().__init__(name)   # Calling parent constructor
        self.grade = grade
        print("Student constructor called")


if __name__ == "__main__":
    s = Student("Alice", "A")
    print(s.name, s.grade)
