






def next_smaller(n):
    n = str(n)
    for i in range(len(n)-2, -1, -1):
        if n[i] > n[i+1]:
            break
    else:
        return -1
    n = list(n)
    for j in range(len(n)-1, i, -1):
        if n[j] < n[i]:
            n[i], n[j] = n[j], n[i]
            break
    n[i+1:] = reversed(n[i+1:])
    if n[0] == '0':
        return -1
    return int(''.join(n))
print(next_smaller(7645))
