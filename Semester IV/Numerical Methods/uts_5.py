from math import pi, exp, sqrt


low = -2
hi = 2
dx = 0.1

sumeven = 0
sumodd = 0

def fun(x):
    a = 1/sqrt(2*pi)
    b = exp((-x**2)/2)
    return a*b

for i in range(1,40):
    sumeven += 4*fun(-2+i*dx)
    sumodd  += 2*fun(-2+(i+1)*dx)

print(sumeven, sumodd)

print(fun(-2))
print(fun(2))

print('result =', ((dx/3)*fun(-2)+fun(2)+sumeven+sumodd))


