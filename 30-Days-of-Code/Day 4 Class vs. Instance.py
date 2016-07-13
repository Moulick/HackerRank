class Person:

    def __init__(self, InitialAge):
        self.InitialAge = InitialAge
        if InitialAge > 0:
            age = InitialAge
        else:
            age = 0
            print('Age is not valid, setting age to 0.')

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
        global age
        age += 1
