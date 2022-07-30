class ineuron:
    def __init__(self):
        self.students1 = "Datascience"

    def students(self):
        print(self.students1)

i = ineuron()
i.students()
i.students1 = "Data analytics"   #override the value of variable in runtime
i.students()


class ineuron1:
    def __init__(self):
        self.__students1 = "Datascience"

    def students(self):
        print(self.__students1)

    def student_change(self):
        self.__students1 = "Big data by me"

i1 = ineuron1()
i1.students()
i1.__students1 = "Bigdata"
i1.student_change()
i1.students()


class ineuron1:
    def __init__(self):
        self.__students1 = "Datascience"

    def students(self):
        print(self.__students1)

    def student_change(self,new_value):
        self.__students1 = new_value

i1 = ineuron1()
i1.students()
i1.__students1 = "Big data"
i1.students()
i1.student_change("UDAY")
i1.students()

