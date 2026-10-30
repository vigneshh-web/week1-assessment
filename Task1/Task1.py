def bonus(salary, rate=0.1, *extras, **options):

    total = salary * rate + sum(extras)

    if "cap" in options:
        total = min(total, options["cap"])

    return total

# print(bonus(50000, 0.1, 500))
print(bonus(50000, 0.1, 500, cap=5000))

class InvalidSalaryError(Exception):
    pass

class Employee:
    def __init__(self, name, salary):
        if salary < 0:
            raise InvalidSalaryError(f"Invalid salary: {salary}")
        self.name = name
        self.salary = salary    

    def annual_salary(self):
        return self.salary * 12

    def get_details(self):
        return f"Name: {self.name}, Salary: {self.salary}"

class Manager(Employee):
    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)
        self.team_size = team_size

    def get_details(self):
        return f"Name: {self.name}, Salary: {self.salary}, Team Size: {self.team_size}"

emp1 = Employee("Arun", 30000)
mgr1 = Manager("Priya", 80000, 5)

print(emp1.get_details())
print(mgr1.get_details())
print(mgr1.annual_salary())
try:
    emp=Employee("Arun",-5000)
except InvalidSalaryError as e:
    print ("Error :",e)
finally:
    print("Transaction Processed")

employes = [
    {"name": "Arun", "salary": 30000},
    {"name": "Priya", "salary": 45000},
    {"name": "Rahul", "salary": 60000},
    {"name": "Divya", "salary": 75000},
    {"name": "Karthik", "salary": 90000},
    {"name": "Meena", "salary": 52000},
    {"name": "Suresh", "salary": 68000},
    {"name": "Anitha", "salary": 48000}
]

high_earners = [
    emp["name"] for emp in employes if emp["salary"] > 50000
]

print("Above 50000:", high_earners)

salaries = [30000, 45000, 60000, 75000]
new_salaries=list(map(lambda salary : round(salary * 1.10,2),salaries))
print(new_salaries)

employees = [
    {"name": "Arun", "salary": 30000, "city": "Chennai"},
    {"name": "Priya", "salary": 45000, "city": "Chennai"},
    {"name": "Rahul", "salary": 60000, "city": "Bangalore"},
    {"name": "Divya", "salary": 75000, "city": "Chennai"},
    {"name": "Karthik", "salary": 90000, "city": "Mumbai"},
    {"name": "Meena", "salary": 52000, "city": "Bangalore"},
    {"name": "Suresh", "salary": 68000, "city": "Chennai"},
    {"name": "Anitha", "salary": 48000, "city": "Mumbai"}
]

chennai_employees = list(
    filter(lambda emp: emp["city"] == "Chennai", employees)
)

chennai_names = list(map(lambda emp: emp["name"], chennai_employees))

print("Chennai:", chennai_names)

sallaries = [30000, 0, 45000, 60000, 90000, 52000]
sallaries_list=[]
for sal in salaries:
    if sal == 0:
        continue
    if sal > 85000:
        break
    sallaries_list.append(sal)

print(sallaries_list)
