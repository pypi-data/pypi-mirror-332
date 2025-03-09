def multmat(size:int, matrizA:list, matrizB:list) -> None:
    if not isinstance(matrizA, list) or not isinstance(matrizB, list):
        raise TypeError("As matrizes devem ser em formato de Listas")

    if not isinstance(size, int):
        raise TypeError("O tamanho deve ser do tipo inteiro")

    if size <= 0:
        raise ValueError("Digite um número maior que zero")
    
    if len(matrizA) != size or len(matrizB) != size:
        raise ValueError(f"As matrizes devem possuir a quantidade de valores respectivos a uma matriz {size} x {size}")
    
    for row in matrizA:
        if len(row) != size:
            raise ValueError(f"Todas as linhas da matriz de entrada devem ter tamanho {size}")
    
    for row in matrizB:
        if len(row) != size:
            raise ValueError(f"Todas as linhas da matriz de entrada devem ter tamanho {size}")

    result_matriz = [[0] * size for _ in range(size)]
    
    for i in range(size):
        for j in range(size):
            for k in range(size):
                result_matriz[i][j] += matrizA[i][k] * matrizB[k][j]
    
    for row in result_matriz:
        print(row)

def seglen(pointA:list, pointB:list):

    if not (isinstance(pointA, list) and isinstance(pointB, list)):
        raise TypeError("Os pontos devem ser listas de dois números")

    if not (len(pointA) == 2 and len(pointB) == 2):
        raise ValueError("Cada ponto deve conter exatamente duas coordenadas (x, y)")

    if not all(isinstance(coord, (int, float)) for coord in pointA + pointB):
        raise TypeError("As coordenadas devem ser números inteiros ou de ponto flutuante")

    return ((pointA[0] - pointB[0]) ** 2 + (pointA[1] - pointB[1]) **2) ** 0.5