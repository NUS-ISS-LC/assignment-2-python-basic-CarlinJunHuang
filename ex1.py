def find(s, n):
    length = len(s)
    for i in range(length):
        for j in range(length):
            if (s[i] + s[j]) == n:
                return [i, j]
    return None
