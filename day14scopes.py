class Difference:
    def __init__(self, a):
        self.__elements = a

    # Add your code here
    def computeDifference(self):
        elements=[]
        for i in self.__elements:
            for j in self.__elements:
                minus= abs(i-j)
                elements.append(minus)

        self.maximumDifference= max(elements)
        

# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)