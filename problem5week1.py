N=input('Slices:')
Y=input('Total price of pizza:')
Z=input('Slice eaten by one person:')
z=int(Z)
a=int(N)
b=int(Y)
for_one_person=b/a
amount=for_one_person*z


print('You should pay:BDT',amount)