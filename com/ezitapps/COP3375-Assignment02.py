'''
Created on Jan 24, 2017

We were asked to add two functionalities to the fractions program (Multiply and Divide Fractions).

The first would be to multiply two fractions. There we would just multiply the two numerator and two denominators. 
Once that is done, we should print the results. 

The second would be to divide two fractions. An easy way to do this is by flipping over the second fraction, and 
then multiplying it be the first. 

Test all the methods and make sure they are working. 

@author: juanramirez
'''
from lib2to3.fixer_util import String
from builtins import str
from fractions import gcd

class Fraction:
    '''
    classdocs
    
    The Fraction Class where we will define all the functions/methods of the fractions.
    This will include addition, multiplication, and division of fractions. This will 
    also include outputting the results. 
    '''


    def __init__(self, top,bottom):
        '''
        Constructor
        
        When an object is created, the constructor will assign the passed values to
        numerator num and denominator den.
        '''
        self.num = top
        self.den = bottom
        
    
    # Print function. This outputs the fraction in a readable format.
    def __str__(self):
        return str(self.num) + "/" + str(self.den)
    
    # Addition function. It will assign the result to a new value. 
    # The formula for adding a fraction is
    # a/b + c/d = ((a*d)+(c*b))/b*d
    # Call gcd funtion to return the result as a simplified fraction. 
    def __add__(self,otherfraction):
        newnum = (self.num * otherfraction.den) + (self.den * otherfraction.num) 
        newden = (self.den * otherfraction.den)
        common = gcd(newnum, newden)
        
        return Fraction(newnum//common,newden//common)
    
    # From the documentation, I was able to determine that
    # to overwrite the * you can redefine the __mul__ method.
    # The formula to multiply a fraction is to simply multiply the 
    # numerators and then the denominators. 
    # Call gcd function to return the result as a simplified fraction. 
    # https://docs.python.org/3/reference/datamodel.html (emulating numeric types)
    def __mul__(self, otherfraction):
        newnum = (self.num * otherfraction.num) 
        newden = (self.den * otherfraction.den)
        common = gcd(newnum, newden)
        
        return Fraction(newnum//common,newden//common)
    
    
    # From the documentation, I was able to determine that
    # to overwrite the / you can redefine the __truediv__ method.
    # The formula to divide a fraction is to simply invert the other fraction and multiply the 
    # new numerators and then the new denominators. 
    # Call gcd function to return the result as a simplified fraction. 
    # https://docs.python.org/3/reference/datamodel.html (emulating numeric types)
    def __truediv__ (self, otherfraction):
        newnum = (self.num * otherfraction.den) 
        newden = (self.den * otherfraction.num)
        common = gcd(newnum, newden)
        
        return Fraction(newnum//common,newden//common)
    
    # Define the comparison methods. 
    # Return true or false depending on the results. 
    def __eq__(self, other):        
        firstnum = self.num * other.den 
        secondnum = other.num * self.den 
        
        return firstnum == secondnum

    
    # Get the greatest common denominator. 
    # Return the value. 
    def gcd(m,n):
        while m%n != 0:
            oldm = m        
            oldn = n       
            m = oldn        
            n = oldm%oldn    
        return n
    
    

def main(): 
    # Print introduction to the program
    print("Welcome to the fractions program")
    
    # Create an object  for the first fraction
    # Print it to screen.
    myFraction = Fraction(1,4)
    print("First Fraction is: " + myFraction.__str__())
    
    # Create an object  for the second fraction
    # Print it to screen.
    myFraction2 = Fraction(2,8)
    print("Second Fraction is: " + myFraction2.__str__())
    print()
    
    # Add the Fractions using the add method.
    # Print the results.
    addFraction = myFraction + myFraction2
    print("The result of adding these two fractions is:")
    print(addFraction)
    print()
    
    # Multiply the fractions using the mul method
    # Print the results.
    multiplyFraction = myFraction * myFraction2
    print("The result of multiplying these two fractions is:")
    print(multiplyFraction)
    print()
    
    # Divide the fractions using the truediv method
    # Print the results.
    divideFraction = myFraction / myFraction2
    print("The result of dividing these two fractions is:")
    print(divideFraction)
    print()
    
    # Check if the two fractions have the same value. 
    # Use the == methods to compare. 
    equalFractions = myFraction == myFraction2
    print("Are the fractions the same?")
    print(equalFractions)
    print()
    
    


# Start Main.
if __name__ == '__main__':
    main()