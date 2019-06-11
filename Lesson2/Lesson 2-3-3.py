import random
if __name__=='__main__':
    def bild_list(a,b,m=8):
        t=[]
        if a>b:
            for j in range(m):
                t.append(random.randint(b,a))
        else:
            for j in range(m):
                t.append(random.randint(a,b))
        return t
    print(bild_list(2,8))
# Как вывести значения массива при условии, что  функция ничего не возвращает ??
