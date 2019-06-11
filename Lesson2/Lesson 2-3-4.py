if __name__=='__main__':
    def fact(n):
        s=1
        for i in range(1,n+1):
            s=s*i
        return s
    print('n!=',fact(7))

        