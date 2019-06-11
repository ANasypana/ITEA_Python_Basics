if __name__=='__main__':
    def avrg_mass(l):
        s=0
        num_of=len(l)
        for i in l:
            s=s+int(i)
        return float(s/num_of)
    print('Enter the list of numbers (through ','):')
    a=str(input())
    l = a.split(",")
    print(l)
    print('Result of avrg_mass:', avrg_mass(l))

