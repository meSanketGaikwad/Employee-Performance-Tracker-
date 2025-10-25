class Employee:
    def __init__(self, name, department, hours_worked, tasks_completed, rating):
        self.name = name
        self.department = department
        self.hours_worked = float(hours_worked)
        self.tasks_completed = int(tasks_completed)
        self.rating = float(rating)

    def performance_score(self):
        return (self.tasks_completed * 0.6) + (self.rating * 0.4)

    def __str__(self):
        return f"{self.name} | {self.department} | Hours: {self.hours_worked} | Tasks: {self.tasks_completed} | Rating: {self.rating}"
