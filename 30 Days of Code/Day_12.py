

class Student(Person):
    #   Class Constructor
    #   
    #   Parameters:
    #   firstName - A string denoting the Person's first name.
    #   lastName - A string denoting the Person's last name.
    #   id - An integer denoting the Person's ID number.
    #   scores - An array of integers denoting the Person's test scores.
    #
    # Write your constructor here
    def __init__(self,firstName,lastName,id,scores):
        super().__init__(firstName,lastName,id)
        self.scores=scores

    #   Function Name: calculate
    #   Return: A character denoting the grade.
    #
    # Write your function here
    def calculate(self):
        total = 0
        for i in range(len(self.scores)):
            total = total+self.scores[i]
        avg = total/len(self.scores)
        if avg>=90 and avg<=100:
            return ('O')
        elif avg>=80 and avg<90:
            return ('E')
        elif avg>=70 and avg<80:
            return('A')
        elif avg>=55 and avg<70:
            return ('P')
        elif avg>=40 and avg<55:
            return ('D')
        else:
            return ('T')
    

