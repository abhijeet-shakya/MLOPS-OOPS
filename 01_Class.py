# Initiate a class

class Employee:
    # special method/magic method/dunder method - constructor
    
    def __init__(self) -> None:
        print("Starting executing attributes")
        self.id = 123
        self.salary = 50000
        self.designation = "SDE"
        print("Attributes/Data have been initiated")

    def travel(self, destination):
        print("This travel method was called manually")
        print(f"Employee is now travelling to {destination}")

# creating an obj/instance of the class
sam = Employee()

# printing the attributes
# print(f"{sam.id} {sam.salary} {sam.designation}")

# calling a method
# sam.travel("Assam")

print(type(sam))
