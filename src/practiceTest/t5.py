def f(a,L=None):
    if L is None:
        L=[]
    L.append(a)
    return L

print(f(1))