if __name__=='__main__':

    def prime_num(a):
        p=1
        for i in range(2,int((a**0.5)+1)):
            p=p*(a%i)

        if p==0:
            return 'Composite number'
        return 'Prime number'
    print(prime_num(11))

