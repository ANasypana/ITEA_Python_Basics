import random
if __name__=='__main__':
    a=random.randint(0,10)
    print(a)
    x=-1
    while x!=a:
        print('Enter number:')
        x=int(input())
        if x==a:
            print('Success!')
        elif x<a:
            print('The number is larger')

        else:
            print('The number is less')




