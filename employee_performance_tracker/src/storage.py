import csv
from src.employee import Employee

DATA_FILE = "data/employees.csv"

def load_employees():
    employees = []
    with open(DATA_FILE, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            employees.append(Employee(**row))
    return employees

def save_employee(employee):
    with open(DATA_FILE, "a", newline='') as file:
        writer = csv.writer(file)
        writer.writerow([employee.name, employee.department, employee.hours_worked, employee.tasks_completed, employee.rating])
