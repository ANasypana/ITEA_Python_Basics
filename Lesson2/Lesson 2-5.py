if __name__=='__main__':
    print('Enter list of numbers (through ", "):')
    a=str(input())
    l=a.split(",")
    S=0
    for i in l:
        S=S+int(i)
    print('Sum: ',S)



