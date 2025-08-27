"""Exercise 3: Build a class Employee with multiple constructors that can initialize an employee object in different ways."""

class Employee:
    def __init__(self,name="John Doe", age=21, company="N/A") -> None:
        self.name = name
        self.age = age
        self.company = company

    def __str__(self) -> str:
        return f"Hello my name is {self.name}, I am {self.age} years old, and I work for {self.company}"

print(Employee(name="Nico Collins",age=26,company=" Houston Texans"))
print(Employee())