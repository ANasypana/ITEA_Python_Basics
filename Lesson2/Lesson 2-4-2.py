if __name__=='__main__':
    def power2(n):

        if n%1!=0:
            return 'No'
        elif n==1:
            return 'Yes'
        else:
            return power2(n/2)

    print(power2(16))

