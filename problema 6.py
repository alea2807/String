n1=str(input("introduceti primul cuv:"))
n2=str(input("introduceti al 2lea cuv:"))
n3=str(input("introduceti al 3lea cuv:"))
n4=str(input("introduceti al 4lea cuv:"))
w=str(n1)
x=str(n2)
y=str(n3)
z=str(n4)
c=0
if(((len(w))>=3)and((len(x))>=3)and((len(y))>=3)and((len(z))>=3)):
    c=(len(d))/2
    i=int(c)
    a=w[:2]
    b=x[0]
    c=y[:3]
    d=z[:1]
    print( n1," ", n2 , " " , n3 , " " , n4)
    print(str(a)+str(b)+str(c)+str(d))
else:
    print("nu face parte din conditie")