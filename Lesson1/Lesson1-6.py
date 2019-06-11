if __name__=='__main__':
    print('Enter temperature values in Kelvin:')
    K=float(input())
    if K<0:
        print('It is not correct')
    else:
        C=K-273.15
        print(round(C),' C')
