# import random
# ar = []
#
# i=1
# h=int(input('введите число : '))
# for i in range(1000):
#     ar.append(random.randint(1,1000))
#     i+=1
# ar.sort()
# print(ar)
#
# g=len(ar)//2
# o=len(ar)//2
# c=0
# p=True
# while True:
#
#     if h==ar[g]:
#         print(g)
#         break
#     if h<ar[g]:
#         o=round(o/2)
#         g-=o
#     else:
#         o=round(o/2)
#         g+=o
#     if o==0:
#         print('врвавыаывы')
#         break
#     c += 1
# print(c)


def increment_string(s):
    if s and s[-1].isdigit():
        num = s
        while num and num[-1].isdigit():
            num = num[:-1]
        return num + str(int(s[len(num):]) + 1).zfill(len(s) - len(num))
    else:
        return s + '1'


def move_zeros(lst):
    p = 0
    lst=list(lst)
    for i in range(len(lst)-1,-1,-1):
        if lst[i] == '0':
            p += 1
            lst.pop(i)

    lst.extend(['0']*p)
    return lst

print(move_zeros('20502925252464'))

















def next_bigger(n):
    n = str(n)
    for i in range(len(n)-2,-1,-1):
        if n[i] < n[i+1]:
            break
    else:
        return -1
    n = list(n)
    for j in range(len(n)-1,i,-1):
        if n[j] > n[i]:
            n[i],n[j] = n[j],n[i]
            break
    n[i+1:] = reversed(n[i+1:])
    return int(''.join(n))
print(next_bigger(7354))




