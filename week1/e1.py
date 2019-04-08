import random as r

def generar(n):
    a = [0]*n
    return list(map(lambda x : r.randint(1,100), a))

def mostar(array):
    print(array)

def reversa(array):
    print(array[::-1])

def minArreglo(array):
    return min(array)

def mediaArreglo(array):
    pos = int(len(array)/2)
    return array[pos]

def ocurrencias(array):
    return list(map(lambda x : array.count(x), array))

def main():
    n = 10
    a = generar(n)
    print(a)
    reversa(a)
    print(minArreglo(a))
    print(mediaArreglo(a))
    print(ocurrencias(a))

if __name__ == "__main__":
    main()
