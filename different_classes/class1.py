class Student(object):
    def __init__(self, name: str, age: int, number_brothers: int):
        self.name = name
        self.age = age
        self.number_brothers = number_brothers
        self.data = {
            'Name': self.name,
            'Age': self.age,
            'Brothers': self.number_brothers
        }

    def __enter__(self):
        print('We are entering into Context Manager')
        print('The student data are:')
        return list(self.data.values())

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('Now that you know data from the student, we are exiting from Context Manager')
        return 0
