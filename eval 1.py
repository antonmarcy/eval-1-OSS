students = {}

def add_student(student_id, name, student_class):
    students[student_id] = {
        'name': name,
        'class': student_class,
        'grades': []
    }

def update_grades(student_id, new_grades):
    if student_id in students:
        students[student_id]['grades'].extend(new_grades)

def calculate_average(student_id):
    if student_id in students:
        grades = students[student_id]['grades']
        return sum(grades) / len(grades) if grades else 0

def generate_top_students_report():
    class_top_students = {}
    for student_id, details in students.items():
        student_class = details['class']
        average = calculate_average(student_id)
        if student_class not in class_top_students or average > class_top_students[student_class]['average']:
            class_top_students[student_class] = {
                'student_id': student_id,
                'name': details['name'],
                'average': average
            }
    return class_top_students

add_student('001', 'Alice', '10A')
add_student('002', 'Bob', '10A')
add_student('003', 'Charlie', '10B')

update_grades('001', [88, 92, 85])
update_grades('002', [75, 80, 78])
update_grades('003', [90, 93, 89])

top_students_report = generate_top_students_report()

print(top_students_report)


