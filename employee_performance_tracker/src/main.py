from src.storage import load_employees, save_employee
from src.analysis import get_top_performers, average_rating, total_tasks
from src.visualize import show_tasks_vs_rating
from src.employee import Employee

def main_menu():
    while True:
        print("\n=== Employee Performance Tracker ===")
        print("1. View All Employees")
        print("2. Add New Employee")
        print("3. Analyze Top Performers")
        print("4. Visualize Performance")
        print("5. Exit")

        choice = input("Enter your choice: ")

        employees = load_employees()

        if choice == '1':
            for e in employees:
                print(e)

        elif choice == '2':
            name = input("Enter name: ")
            dept = input("Enter department: ")
            hours = input("Enter hours worked: ")
            tasks = input("Enter tasks completed: ")
            rating = input("Enter rating (1-10): ")

            new_emp = Employee(name, dept, hours, tasks, rating)
            save_employee(new_emp)
            print("✅ Employee added successfully!")

        elif choice == '3':
            top = get_top_performers(employees)
            print("\nTop Performers:")
            for e in top:
                print(f"{e.name} - Score: {e.performance_score():.2f}")

        elif choice == '4':
            show_tasks_vs_rating(employees)

        elif choice == '5':
            print("Exiting... Goodbye!")
            break

        else:
            print("Invalid choice! Try again.")

if __name__ == "__main__":
    main_menu()
