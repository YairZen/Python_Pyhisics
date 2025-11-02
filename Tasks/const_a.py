import numpy as np
#import matplotlib.pyplot as plt

qn=int(input('enter question number: '))
a=float(input('enter acceleration: '))
print()

if qn==2:
    t=float(input('enter t: '))
    ## your answer
    v= a*t

    ## output
    print(f'v={v:.5g} m/s')

if qn==3:
    t=float(input('enter t: '))
    ## your answer

    x= 0.5*a*(t*t)

    ## output
    print(f'x={x:.5g} m')

if qn==4:
    v=float(input('enter v: '))
    ## your answer

    x= ((v*v)/a)*0.5

    ## output3
    print(f'x={x:.5g} m')

if qn==7:
    ANS=False
    print(ANS)