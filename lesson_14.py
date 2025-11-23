class GroupError(Exception):
    """Custom exception raised when trying to add more than 10 students to a group."""
    pass


class Human:

    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f'{self.first_name} {self.last_name}, {self.gender}, {self.age} y.o.'


class Student(Human):

    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return (f'{self.first_name} {self.last_name}, {self.gender}, '
                f'{self.age} y.o., record book: {self.record_book}')


class Group:

    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student):
        """Add a student to the group. Raise GroupLimitError if there are already 10 students."""
        if len(self.group) >= 10:
            raise GroupError(f'Group {self.number} already has 10 students!')
        self.group.add(student)

    def find_student(self, last_name):
        """Return a student instance with the given last name, or none if not found."""
        for student in self.group:
            if student.last_name == last_name:
                return student
        return None

    def delete_student(self, last_name):
        """Delete a student by last name, if they are in the group."""
        student = self.find_student(last_name)
        if student is not None:
            self.group.remove(student)

    def __str__(self):
        all_students = ''
        for student in self.group:
            all_students += str(student) + '\n'
        all_students = all_students.strip()
        return f'Group number: {self.number}\n{all_students}'





students = [
    Student('Male', 20, f'Name{i}', f'Surname{i}', f'RB{i:03d}')
    for i in range(1, 12)
]

group = Group('PD1')


for i in range(10):
    group.add_student(students[i])

print('Number of students in group now:', len(group.group))

try:
    group.add_student(students[10])
except GroupError as e:
    print('Caught exception:', e)

print('Number of students in group after attempt:', len(group.group))
