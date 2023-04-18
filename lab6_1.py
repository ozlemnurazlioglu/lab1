
#question1
from math import factorial

n = int(input ("Enter a value for n:"));
x=int (input("Enter the value for x:"));
def Equation(n,x):
    sit =lambda n, k: n**k/ factorial(k)
    situ=[sit(n,k) for k in range (x+1)]
    total= sum(situ)+1
    print("Result:", total )
Equation(n,x)
