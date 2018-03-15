class Difference:
    def __init__(self, a):
        self.__elements = a
    def computeDifference(self):
        a = sorted(self.__elements)
        self.maximumDifference = abs(a[-1] - a[0])
# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)