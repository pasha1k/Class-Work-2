class Student:
    group = "C2019"
    gender = "Male"
    education = "MKA STEP"

    def __init__(self):
        # print(id(self))
        self.name = "Oleg"
        self.age = 15

st1 = Student()
print(st1.name)
print(st1.age)
print(id(st1))
st2 = Student()

print (st1.group)
print (st2.group)
