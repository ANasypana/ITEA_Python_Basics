import string
if __name__=='__main__':
    ts=''
    l=[]
    # print('Enter the list of words (through ','):')
    # a = str(input())
    a='ooojuoi, tyiu, ll, , k'
    for i in a:
        if i!=',':
            ts=ts+i
        else:
            l.append(ts.strip(' '))
            ts=''
    l.append(ts.strip(' '))
    print(l)





