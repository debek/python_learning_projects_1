def funkcja(x):
    return x * x

def funkcja2(f1, x, y):
    return f1(x) + y

print(funkcja2(funkcja, 2, 3))
