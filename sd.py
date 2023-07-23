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

def parse_int(string):
    num_dict = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9,
                'ten': 10, 'eleven': 11, 'twelve': 12, 'thirteen': 13, 'fourteen': 14, 'fifteen': 15, 'sixteen': 16,
                'seventeen':17, 'eighteen':18, 'nineteen':19, 'twenty':20, 'thirty':30, 'forty':40, 'fifty':50,
                'sixty':60,'seventy':70,'eighty':80,'ninety':90}
    thou_dict= {'hundred':100,'thousand':1000,'million':1000000}
    string = string.replace(' and','').replace('-',' ')
    num_list = string.split()
    thou_sum = 0
    for num in num_list:
        if num in num_dict:
            thou_sum += num_dict[num]
        else:
            if num in thou_dict:
                thou_sum *= thou_dict[num]


    return thou_sum
print(parse_int("seven hundred eighty-three thousand nine hundred and nineteen"))

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




