class Person:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def display(self) -> str:
        return f"{self.name} is {self.age} years old"


class Student(Person):
    def __init__(self, name: str, age: int, course: str) -> None:
        super().__init__(name, age)
        self.course = course

    def display(self) -> str:
        return f"{self.name} studies {self.course} and is {self.age} years old"


if __name__ == "__main__":
    student = Student("Aman", 21, "Python OOP")
    print(student.display())
