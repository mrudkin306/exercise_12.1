def most_frequent(n):
    d = dict()
    for key in n:
        if key not in d:
            d[key] = 1
        else:
            d[key] += 1
    return d

print(most_frequent('Python is cool'))
