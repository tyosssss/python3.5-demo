# -*- coding:utf-8 -*-
# iterator





class Students:
    def __init__(self, *args):
        self.students = args

    def __iter__(self):
        return StudentIterator(self.students)


class StudentIterator:
    def __init__(self, students):
        self.students = students
        self.index = 0
        self.count = len(students)

    def __next__(self):
        self.index += 1

        if self.index <= self.count:
            return self.students[self.index - 1]
        else:
            raise StopIteration


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return 'I\'m %s.My age is %d' % (self.name, self.age)


students = Students(Student('A', 1), Student('B', 2), Student('C', 3))

# for 循环迭代
for s in students:
    print(str(s))
else:
    print('done')

# 手动迭代
print('手动调用:')
student_iterator = students.__iter__()
while True:
    try:
        print(student_iterator.__next__())
    except StopIteration:
        print('done')
        break
