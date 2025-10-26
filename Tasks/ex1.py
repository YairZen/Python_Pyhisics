import numpy as np
# import matplotlib.pyplot as plt

#input
A=float(input("A:"))
B=float(input("B:"))
qn=int(input("qn:"))

# you code
##########
C = np.abs(A-B)
D = A + B

# # create array b with specified number of elements.
# x = np.linspace(start=0, stop=10, num=100)
# y = np.sin(x+2)*np.cos((2*x) - 3)
#
# # create
# plt.plot(x,y)
# plt.show()

max_no = 5

##########
#output
if qn==1:
    print(f'{C:.5g}')
elif qn==2:
    print(f'{D:.5g}')
elif qn==3:
    print(max_no)