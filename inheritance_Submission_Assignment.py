"""This is created to practice making
parent classes and having those attributes
be passed to the children classes and adding
new attributes to the child classes."""


"""This is the parent class"""

class God_Class:
      def __init__(self, Name, Powers, Symbol_of_Power):
       self.Name = 'Name of God'
       self.Powers = 'Please List Powers'
       self.Symbol_of_Power: 'Please type symbol'
       
#Child class 1
class Demi_God(God_Class):
       Godly_Parent = 'Insert Name'
       Weapon = ''

#child class number 2
class Titan(God_Class):
       Godly_Child = ''
       Roman_Name = ''

       
print(God_Class,Demi_God,Titan)
