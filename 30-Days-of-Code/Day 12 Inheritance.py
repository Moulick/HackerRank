class Student(Person):

    def __init__(self, firstName, lastName, idNumber, scores):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber
        self.scores = scores
# Moulick

    def calculate(self):

        x = 0
        x = (sum(self.scores) / len(self.scores))
        if 90 <= x <= 100:
            return 'O'
        elif 80 <= x < 90:
            return 'E'
        elif 70 <= x < 80:
            return 'A'
        elif 55 <= x < 70:
            return 'P'
        elif 40 <= x < 55:
            return 'D'
        elif x < 40:
            return 'T'
