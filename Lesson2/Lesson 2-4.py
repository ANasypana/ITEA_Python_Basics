if __name__=='__main__':
    print('Enter word:')
    a=str(input())
    for i in a:
        if i.isupper():
            print(i, end=' ')
        continue