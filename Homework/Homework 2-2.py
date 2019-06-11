if __name__=='__main__':
    def fuct(n):
        if n==0:
            return 1
        else:
            return n*fuct(n-1)
    print('8! ',fuct(8))