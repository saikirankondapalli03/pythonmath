class Student:
    '''
    this is used for initializing the instance of class ==> constructor 
    constructor ===> means , it is a method where you initialize the values of instance(age,name) of class 
    '''
    def __init__(self,myage=0,fname=""): 
        self.age = myage
        self.name = fname

    def __str__(self):
        return f"age is :- {self.age}   name is :- {self.name}";

abcd = Student(12,"priya")
sai = Student(13,"sai")
print(abcd) #here we are printing hex code 
print(sai)