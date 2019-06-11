if __name__=='__main__':
    def degree_of_number (a,n):
        s=1
        for i in range(n):
            s=s*a
        return s
    print(degree_of_number(2,3))
