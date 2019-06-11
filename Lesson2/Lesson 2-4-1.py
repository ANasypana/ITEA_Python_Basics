if __name__=='__main__':
    def sum_digit(n):
        if n<10:
            return n
        else:
            s=n-(n//10)*10

            a=n//10
            return s+sum_digit(a)


    print(sum_digit(5909))

