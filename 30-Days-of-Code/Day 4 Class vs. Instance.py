class Person:

    def __init__(self, initialAge):
        self.initialAge = initialAge
        if initialAge < 0:
            print('Age is not valid, setting age to 0.')
            age = 0

    def amIOld(self):
        # Do some computations in here and print out the correct statement to
        # the console
        if age < 13:
            print('You are young.')
        elif age in range(13, 18):
            print('You are a teenager.')
        else:
            print('You are old.')

    def yearPasses(self):
        initialAge += 1
t = int(input())
for i in range(0, t):
    age = int(input())
    p = Person(age)
    p.amIOld()
    print(age)
    p.yearPasses()
    p.amIOld()
    print("")
