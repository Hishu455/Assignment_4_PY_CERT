from math import acos

a = map(float,input().split(' '))
b = map(float,input().split(' '))
c = map(float,input().split(' '))
d = map(float,input().split(' '))



def dot_product(a,b):
    return a[0]*b[0] + a[1]*b[1] + a[2]*b[2]

def length(a):
    return (a[0]**2 + a[1]**2 + a[2]**2)**0.5

def cross_product(a,b):
    return [ a[1]*b[2] - a[2]*b[1], a[0]*b[2] - a[2]*b[0], a[0]*b[1] - a[1]*b[0]] 

def diff(a,b):
    return [ a[0]-b[0], a[1]-b[1], a[2]-b[2]]

#a = [0, 4, 5]
#b = [1, 7, 6]
#c = [0, 5, 9]
#d = [1, 7, 2]

ab = diff(a,b)
bc = diff(b,c)
cd = diff(c,d)
x = cross_product(ab,bc)
y = cross_product(bc,cd)

cos_phi = dot_product(x,y) / length(x)/length(y)
phi_rad = acos(cos_phi)
pi = 3.141592653589793
phi = phi_rad*360/2/ pi

print("%.2f" % phi)