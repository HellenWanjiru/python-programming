#import functions 

#x = functions.add(12,34)
#print(x) 

#from mathematics import subtract
#x=add(23,45)
#print(x)
#y= subtract(20,5)
#print(y) 

#import mathematics 
#x = mathematics.divide(10,2)
#print(x)

#import others 
#x = others.cube(3)
#print(x)
import operators
import trig
import others 
operator=input("Enter operator:")

if operator=="cube":
    num=eval(input("Enter number:"))
    x=others.cube(num)
    print(x)



elif operator =="sin":
    angle=eval(input("Enter sin of angle in degrees:"))
    sin_of_angle=trig.get_sine(angle)
    print(sin_of_angle) 



else:
    num1=eval(input("enter number 1:"))
    num2=eval(input("Enter number 2:"))

    if operator == "+":
      x=operators.add(num1,num2)
      print(x)


    elif operator == "-":
       x=operators.subtract(num1,num2)
       print(x)


    



