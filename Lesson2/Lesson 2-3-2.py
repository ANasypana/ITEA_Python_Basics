if __name__=='__main__':
    l=[106,77,8,90]
    def sum_num(l):
        n=len(l)
        a=[]
        for i in range(n):
            s=0
            for j in str(l[i]):
                s=s+int(j)
            a.append(s)
        return a
    def sort_mass(l):
        t=[]
        def sm (a):
            s=0
            for i in a:
                s=s+int(i)
            return s
        for i in range(len(l)):
            Nmin=i
            for j in range(i+1,len(l)):
                if sm(str(l[j]))<sm(str(l[Nmin])):
                    Nmin=j
            tmp = l[Nmin]
            l[Nmin] = l[i]
            l[i] = tmp
        return l
    print('List: ',l)
    print('List of sum of numbers: ',sum_num(l))
    print('Sorted mass: ', sort_mass(l))
