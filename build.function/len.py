class Students:
    def __init__(self):
        self._students = []

    def add(self, student):
        self._students.append(student)

    def __len__(self):
        return len(self._students)


students = Students()
students.add({"name": "A"})
students.add({"name": "B"})

print(len("haha"))
print(len([1, 2, 3]))
print(len(students))
