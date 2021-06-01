class Person:
    def __init__(self,initialAge):
        if initialAge<0:
            print("Age is not valid, setting age to 0.")
            self.age1=0
        else:
            self.age1=initialAge
    def amIOld(self):
        if self.age1<13:
            print('You are young.')
        elif self.age1>=13 and self.age1<18:
            print('You are a teenager.')
        else :
            print("You are old.")

    def yearPasses(self):
        self.age1+=1



t = int(input())
for i in range(0, t):
    age = int(input())         
    p = Person(age)  
    p.amIOld()
    for j in range(0, 3):
        p.yearPasses()       
    p.amIOld()
    print("")