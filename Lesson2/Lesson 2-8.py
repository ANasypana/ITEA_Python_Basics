if __name__=='__main__':
    print('Enter number:')
    a=str(input())
    S1=0
    S2=0
    for i in a:
        S1=S1+int(i)
    n=len(a)
    for i in range(0,n):
        S2=S2+(int(a)%(10**(i+1)))//(10**i)
    print(S1)
    print(S2)