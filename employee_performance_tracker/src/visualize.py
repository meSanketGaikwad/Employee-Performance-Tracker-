import matplotlib.pyplot as plt

def show_tasks_vs_rating(employees):
    names = [e.name for e in employees]
    tasks = [e.tasks_completed for e in employees]
    ratings = [e.rating for e in employees]

    plt.bar(names, tasks, color='skyblue', label="Tasks Completed")
    plt.plot(names, ratings, color='orange', marker='o', label="Rating")
    plt.xlabel("Employees")
    plt.ylabel("Tasks / Ratings")
    plt.title("Employee Performance Comparison")
    plt.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
