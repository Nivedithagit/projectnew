#5. Write a Person class with an instance variable “age” and a constructor that takes an integer as a
#parameter. The constructor must assign the integer value to the age variable after confirming the
#argument passed is not negative; if a negative argument is passed then the constructor should set
#age to 0 and print “Age is not valid, setting age to 0”. In addition, you must write the following instance
#methods:

class Person:
    def __init__(self,age):
        if age<=0:
              print("Age is not valid, setting age to 0")
              self.age=0
        else:
              self.age=age
    
    def amIOld(self):
        if self.age<13:
            print("you are young")
        elif self.age >= 13 and self.age < 18:
            print("you are teenager")
        else:
            print("you are old")
    
    def yearPasses(self):
        self.age+=1
        t= int(input())
        for i in range(0,t):
              age=int(input())
              p=Person(age)
              p.amIOld()
              for j in range(0,3):
                     p.yearPasses()
                     p.amIOld()
                  
obj=Person(-1)


