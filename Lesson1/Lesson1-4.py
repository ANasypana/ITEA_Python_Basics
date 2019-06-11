import string
if __name__=='__main__':
    ts=''
    l=[]
    # print('Enter the list of numbers (through ','):')
    # a = str(input())
    a='3453, 6,89,999,7'
    for i in a:
        if i!=',':
            ts=ts+i
        else:
            l.append(int(ts.strip(' ')))
            ts=''
    l.append(int(ts.strip(' ')))
    print(l)
    for i in range(len(l)):
       indMin=i
       for j in range(i+1,len(l)):
          if l[j] < l[indMin]:
              indMin = j
       tmp = l[indMin]
       l[indMin] = l[i]
       l[i] = tmp
    print(l)












