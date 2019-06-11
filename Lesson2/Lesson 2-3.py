import math
if __name__=='__main__':
    print('Enter number:')
    i=int(input())
    if math.sqrt(i)>10:
        while math.sqrt(i)>10:
            print(math.sqrt(i))
            print('Enter number:')
            i = int(input())
        print('Square root of number <10')
    else:
        print('Square root of number <10')