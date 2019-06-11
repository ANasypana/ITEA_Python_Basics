if __name__=='__main__':
    def print_digit(n):
        if n < 10:
            print(n)
        else:
            s = n - (n // 10) * 10
            print(s)

            a = n // 10
            return print_digit(a)


    print_digit(6749)
