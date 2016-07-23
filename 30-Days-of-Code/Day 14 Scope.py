class Difference:

    def __init__(self, a):
        self.__elements = a
#------------Only-this-part-is-needed------------#

    def computeDifference(self):
        # Moulick
        self.maximumDifference = abs(
            min(self.__elements) - max(self.__elements))
#------------Only-this-part-is-needed------------#

# End of Difference class
_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)
