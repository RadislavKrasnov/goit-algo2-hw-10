class Teacher:
    def __init__(self, first_name, last_name, age, email, can_teach_subjects):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.can_teach_subjects = set(can_teach_subjects)
        self.assigned_subjects = set()


def create_schedule(subjects, teachers):
    uncovered = set(subjects)
    remaining_teachers = list(teachers)
    schedule = []

    while uncovered:
        best_teacher = None
        best_new_count = 0

        for t in remaining_teachers:
            new_subjects = t.can_teach_subjects & uncovered
            new_count = len(new_subjects)

            if new_count > best_new_count:
                best_new_count = new_count
                best_teacher = t
            elif new_count == best_new_count and new_count > 0:
                if best_teacher is None or t.age < best_teacher.age:
                    best_teacher = t
        
        if best_teacher is None or best_new_count == 0:
            return None
        
        assigned = best_teacher.can_teach_subjects & uncovered
        best_teacher.assigned_subjects = set(assigned)
        schedule.append(best_teacher)
        uncovered -= assigned
        remaining_teachers.remove(best_teacher)
    
    return schedule


if __name__ == '__main__':
    # Множина предметів
    subjects = {'Математика', 'Фізика', 'Хімія', 'Інформатика', 'Біологія'}
    # Створення списку викладачів
    teachers = [
        Teacher("Олександр", "Іваненко", 45, "o.ivanenko@example.com", {'Математика', 'Фізика'}),
        Teacher("Марія", "Петренко", 38, "m.petrenko@example.com", {'Хімія'}),
        Teacher("Сергій", "Коваленко", 50, "s.kovalenko@example.com", {'Інформатика', 'Математика'}),
        Teacher("Наталія", "Шевченко", 29, "n.shevchenko@example.com", {'Біологія', 'Хімія'}),
        Teacher("Дмитро", "Бондаренко", 35, "d.bondarenko@example.com", {'Фізика', 'Інформатика'}),
        Teacher("Олена", "Гриценко", 42, "o.grytsenko@example.com", {'Біологія'}),
    ]

    # Виклик функції створення розкладу
    schedule = create_schedule(subjects, teachers)

    # Виведення розкладу
    if schedule:
        print("Розклад занять:")
        for teacher in schedule:
            print(f"{teacher.first_name} {teacher.last_name}, {teacher.age} років, email: {teacher.email}")
            print(f"   Викладає предмети: {', '.join(teacher.assigned_subjects)}\\n")
    else:
        print("Неможливо покрити всі предмети наявними викладачами.")
