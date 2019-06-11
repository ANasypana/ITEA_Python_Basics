if __name__=='__main__':
    print('Enter n:')
    n=int(input())
    l = [1, 1]
    for i in range(2,n):
        l.append(l[i-2]+l[i-1])
    print('Fibonacci numbers: ',l)


