class User:

    def __init__(self,first_name,last_name):
        self.fist_name = first_name
        self.last_name = last_name 
        self.last_name_and_first_name = first_name + last_name

    def SayFirstName(self) :
        print ("My first name is" ,self.fist_name)


    def SayLastName(self) :
        print ("My last name is" ,self.last_name)

    def SayFirstAndLastName(self) :
         print ("My first and last name is" , self.last_name_and_first_name)

