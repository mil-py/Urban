class Group:
    def __init__(self, gr):
        self.group = gr


class Univer:
    def __init__(self, univer_name, group):
        self.univer_name = univer_name
        # Group.__init__(self, group)
        # super().__init__(self, group) TypeError: Group.__init__() takes 2 positional arguments but 3 were given
        super().__init__(group)  # OK


class Student(Univer, Group):
    def __init__(self, name, univer, group):
        Univer.__init__(self, univer, group)
        self.name = name


stud = Student('Ivan', "Urban", 'Python-1')
print(stud.group)
print(Student.__mro__)
print(Univer.__mro__)
