import math
if __name__=='__main__':
    def fun1(x):
        return math.sin(x)+math.cos(x)
    print('Enter a function argument:')
    x=float(input())
    print('Function values:', fun1(x))