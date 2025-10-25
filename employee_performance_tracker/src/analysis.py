def get_top_performers(employees, n=3):
    sorted_emps = sorted(employees, key=lambda e: e.performance_score(), reverse=True)
    return sorted_emps[:n]

def average_rating(employees):
    return sum(e.rating for e in employees) / len(employees)

def total_tasks(employees):
    return sum(e.tasks_completed for e in employees)
