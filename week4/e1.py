import random as rand

# Con pesos en las aristas
def rand_adj_matrix(n):
    return [[rand.randint(0, n-1) for _ in range(0, n)] for _ in range(0, n)]


# Matriz binaria - solo vertices
def rand_adj_binary_matrix(n):
    return [[rand.randint(0, 1) for _ in range(0, n)] for _ in range(0, n)]

# Graficado como conexiones de punto a nodo
def rand_adj_list(n):
    return [list(set([rand.randint(0,n - 1) for _ in range(rand.randint(0,n))])) for _ in range(0, n)]


if __name__ == "__main__":
    print(rand_adj_matrix(5))
    print(rand_adj_binary_matrix(5))
    print(rand_adj_list(5))