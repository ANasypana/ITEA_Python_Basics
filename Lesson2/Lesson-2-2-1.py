import random
if __name__=='__main__':
    print('Set the range (through ','):')
    a=str(input())
    l = a.split(",")
    a=int(l[0])
    b=int(l[1])
    if a>b:
        print(random.randint(b,a))
    elif a<b:
        print(random.randint(a,b))
    else:
        print('Incorrect range')
