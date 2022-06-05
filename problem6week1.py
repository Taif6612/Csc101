from math import remainder
from platform import java_ver


x=input('x=')
y=input('y=')
z=input('z=')
a=input('a=')
b=input('b=')

q=int(x)
w=int(y)
e=int(z)
r=int(a)
t=int(b)
addition=q+w+e+r+t
quotient=q//t
multiplication_divison=w*r//e


print('Sum of the numbers',addition)
print('Average of the number=',addition/5)
print('Quotient =',quotient)
print('Multiplication and division=',multiplication_divison)
print('value x greater than42',q>5)
print('value y',w>5)
print('value z',e>5)
print('value a',r>5)
print('value b',t>5)
l= q%13==0
k=w%13==0
j=e%13==0
h=r%13==0
g=t%13==0
print('value x qoutient',l)
print('value y',k)
print('value of z',j)
print('value of a',h)
print('value of b',g)
print('if x equal to 42=',q==42)
print('if x equal to 42=',w==42)
print('if x equal to 42=',e==42)
print('if x equal to 42=',r==42)
print('if x equal to 42=',t==42)
