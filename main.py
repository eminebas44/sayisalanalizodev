import math

a=3.14
x=a/5
taylor1=(math.pow((-1),0))*(x**(2*0))/(math.factorial((2*0)))
print(taylor1)
taylor2=(-1**1)*(x**(2*1))/(math.factorial((2*1)))
print(taylor2+taylor1)
cosDegeri=math.cos(x)
kesmehata1=cosDegeri-taylor1
print(kesmehata1)
kesmehata2=cosDegeri-(taylor1+taylor2)
print(kesmehata2)