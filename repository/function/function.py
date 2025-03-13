""" #Print statement
print("Welcome to the class")

for i in range(1,25):
    print(f"print this line{i}")
 """

def add(x,y):
    '''
    Inputs: Take 2 input x and y
    Outputs: Return 1 output that contains sum of x and y
    '''
    add = x+y
    return add


op_xy = add(23,45)
print(op_xy)


def simple_interest(p,n,r):
    if isinstance(p,int|float) and isinstance(n,int|float) and isinstance(r,int|float):
      si = (p*n*r)/100
      return si
    
simp_intr = simple_interest(34000,6,6.7)
print(f"Output of simp_intr function:{simp_intr}")
    

