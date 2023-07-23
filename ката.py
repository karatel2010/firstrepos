def next_bigg(n):
    n = list(str(n))
    f = 0
    for i in range(len(n) - 1, 0, -1):
        if int(n[i]) > int(n[i - 1]):
            n[i], n[i - 1] = n[i - 1], n[i]
            print(n)
            m= n[i:]

            p= n[:i]
            print(m)
            print(p)
            m.sort()
            print(m)
            n=p+m
            f = 1
            return int("".join(n))
    if f == 0:
        return -1


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

print(next_bigger(1344567))




