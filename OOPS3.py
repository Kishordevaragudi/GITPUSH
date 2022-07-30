class ineuron:
    def student(self):          #ex of method overriding
        print("the details of all the students")

    def achievers(self):
        print("print the list of all achievers")

    def hall_of_fame(self):
        print("print everyone from hall of fame")

class ineuron_vision(ineuron):

    def student(self):      #method overriding
        print("these are the filters of student list")

iv = ineuron_vision()
iv.student()