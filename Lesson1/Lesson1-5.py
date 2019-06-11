if __name__=='__main__':
    print('Enter number 1:')
    a=str(input())
    print('Enter number 2:')
    b=str(input())
    a=a[-1]
    b=b[-1]
    c=int(a)+int(b)
    print('Sum of the last digits: ', c)