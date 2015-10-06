'''
Created on 28.12.2013

@author: uhs374h
'''
from bruch.Bruch import *
from random import randint
if __name__ == '__main__':
    b1=Bruch(3,4)
    b2=Bruch(3,4)+b1
    z1,z3=b1
    z2=b1.nenner
    print(z1,z2)
    b3=3+b1+Bruch(1,4)
    b4=3/b3+3
    b3+=Bruch(3,2)
    b0=Bruch(4,3)
    print(str(b1)+" == invert "+str(b0),b1== ~b0 )
    print(b3)
    b3=-b3
    print(b3 is not b2)
    b5=Bruch(b3.zaehler,b3.nenner)
    print(b3 is b5)
    b4=4*b4-Bruch(2,4)-b3**2
    print(b1,'=',float(b1))
    print(hex(int(b1+123)))
    print(oct(int(b1+123)))
    print(int(b1+123))
    print(b2,'=',float(b2))
    print(b3,'=',float(b3))
    print(b4,'=',float(b4))
    print("abs%s ="%(b4),abs(b4))
#----------------------------------------------
# Initialisierung 1000 Elemente
#----------------------------------------------
    b=[]
    for x in range(0, 1000):
        z=randint(0,50)
        n=randint(1,50)
        b.append(Bruch(z,n))
#----------------------------------------------
# Ausgabe und Vergleich mit b1 (3/4)
#----------------------------------------------
    for x in range(len(b)):
        z=b[x]
        print (z,"= "+str(float(z))+
               ("; gt %s" %b1 if z>b1 else '')+
               ("; ge %s" %b1 if z>=b1 else '')+
               ("; lt %s" %b1 if z<b1 else '')+
               ("; le %s" %b1 if z<=b1 else '')+
               ("; eq %s" %b1 if z==b1 else '')+
               ("; ne %s" %b1 if z!=b1 else ''))
        