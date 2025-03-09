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

def segintersect(seg1:list, seg2:list):

    if not (isinstance(seg1, list) and isinstance(seg2, list)):
        raise TypeError("Os pontos devem ser listas de dois números")

    if seg1[0] == seg1[1] or seg2[0] == seg2[1]:
        raise ValueError("Os segmentos de reta não podem ser pontos únicos.")
    
    def orientation(p, q, r):
        det = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
        return 0 if det == 0 else (1 if det > 0 else -1)

    p1, p2 = seg1
    p3, p4 = seg2

    o1 = orientation(p1, p2, p3)
    o2 = orientation(p1, p2, p4)
    o3 = orientation(p3, p4, p1)
    o4 = orientation(p3, p4, p2)

    if o1 != o2 and o3 != o4:
        A1, B1, C1 = p2[1] - p1[1], p1[0] - p2[0], (p2[1] - p1[1]) * p1[0] + (p1[0] - p2[0]) * p1[1]
        A2, B2, C2 = p4[1] - p3[1], p3[0] - p4[0], (p4[1] - p3[1]) * p3[0] + (p3[0] - p4[0]) * p3[1]
        det = A1 * B2 - A2 * B1
        if det == 0: return False
        x, y = (B2 * C1 - B1 * C2) / det, (A1 * C2 - A2 * C1) / det
        return (x, y)

    return False