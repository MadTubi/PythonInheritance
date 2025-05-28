#Recreation of Java file that calculated a student's hours in college

#parent class
class Student(object):

    #constructor
    def __init__(self,name,idNum,yearAdmitted):
        self.name = name
        self.idNum = idNum
        self.yearAdmitted = yearAdmitted

    #method
    def Display(self):
        print("Name", self.name)
        print("ID Number: ", self.idNum)
        print("Year Admitted: ", self.yearAdmitted)

#child class
class CompSciStudent(Student):

    #constructor
    def __init__(self, name, idNum, YearAdmitted, mathHours, csHours, genEDHours):
      #call variables from parent class
      super().__init__(name,idNum,YearAdmitted)  

      self.mathHours = mathHours
      self.csHours = csHours
      self.genEDHours = genEDHours

    #methods
    def remainingHours(self):
        #variables
        MATH_HOURS = 20
        CS_HOURS = 40
        GEN_EDHOURS = 60

        reqHours = (MATH_HOURS + CS_HOURS+GEN_EDHOURS)
        leftOverHours = reqHours - (self.mathHours + self.csHours+self.genEDHours)

        print("Total Hours: ",reqHours)
        print("Remaining Hours: ",leftOverHours)

def main():
    #CompSciStudent Object
    St = CompSciStudent("Jane Doe","1234","2013",12,20,40)
    St.Display()
    print()
    St.remainingHours()

main()