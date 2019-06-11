if __name__=='__main__':
    print('Enter number:')
    a=int(input())
    S=0
    i=0
    if a!=0:
        while a!=0:
            i=i+1
            S=a+S
            print('Enter number:')
            a = int(input())
        print('Sum: ',S)
        print('Quantity ', i)
        print('Mean: ', S/i)
    else:
        print('Your number is null')
