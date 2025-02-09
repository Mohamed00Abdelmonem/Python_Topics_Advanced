class Employee:
    def _init_(self, id, name, salary):
        self.id = id
        self.name = name
        self.salary = salary

class Developer(Employee):
    def _init_(self, id, name, salary, is_developer):
        Employee._init_(self, id, name, salary) 
        self.is_developer = is_developer
        if is_developer:
            print(f"Hello Developer {self.name}, your id = {self.id} and your salary = {self.salary}")
        else:
            print(f"Hello Employee {self.name}, your id = {self.id} and your salary = {self.salary}")

class Manager(Employee):
    def _init_(self, id, name, salary, is_manager):
        Employee._init_(self, id, name, salary)  
        self.is_manager = is_manager
        if is_manager:
            print(f"Hello Manager {self.name}, your id = {self.id} and your salary = {self.salary}")
        else:
            print(f"Hello Employee {self.name}, your id = {self.id} and your salary = {self.salary}")

class TeamLeader(Developer, Manager):
    def __init__(self, id, name, salary, is_developer, is_manager):
        Developer._init_(self, id, name, salary, is_developer)
        Manager._init_(self, id, name, salary, is_manager)
        print(f"Hello Team Leader {self.name}, your id = {self.id} and your salary = {self.salary}")


team_leader = TeamLeader(11, "Abdo", 2000, True, True)