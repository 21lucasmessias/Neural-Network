import random

amostrasAnd = [
    (0.0, 0.0, -1.0),
    (0.0, 1.0, -1.0),
    (1.0, 0.0, -1.0),
    (1.0, 1.0, 1.0),
]

amostrasOr = [
    (0.0, 0.0, -1.0),
    (0.0, 1.0, 1.0),
    (1.0, 0.0, 1.0),
    (1.0, 1.0, 1.0),
]

pesosAnd = [random.randint(0, 100) / 100, random.randint(0, 100) / 100, random.randint(0, 100) / 100]
pesosOr = [random.randint(0, 100) / 100, random.randint(0, 100) / 100, random.randint(0, 100) / 100]

n = 0.01

amostrasAVerificar = [
    (0.0, 0.0),
    (0.0, 1.0),
    (1.0, 0.0),
    (1.0, 1.0),
]


def sinal(u):
    return 1.0 if u >= 0 else -1.0


def treinador():
    global pesosAnd
    global pesosOr
    for epoca in range(200):
        for x in amostrasAnd:

            u = (x[0] * pesosAnd[0]) + (x[1] * pesosAnd[1]) + pesosAnd[2]
            y = sinal(u)

            if y != x[2]:
                for j in range(3):
                    if j == 2:
                        pesosAnd[2] += (n * (x[2] - y))
                        break
                    pesosAnd[j] += (n * (x[2] - y) * x[j])

    for epoca in range(200):
        for x in amostrasOr:

            u = (x[0] * pesosOr[0]) + (x[1] * pesosOr[1]) + pesosOr[2]
            y = sinal(u)

            if y != x[2]:
                for j in range(3):
                    if j == 2:
                        pesosOr[2] += (n * (x[2] - y))
                        break
                    pesosOr[j] += (n * (x[2] - y) * x[j])


def operacao():
    print("Amostras And")
    for x in amostrasAVerificar:
        u = (x[0] * pesosAnd[0]) + (x[1] * pesosAnd[1]) + pesosAnd[2]
        y = sinal(u)
        if y == -1:
            print('classe A')
        else:
            print('classe B')


    print("\nAmostras Or")
    for x in amostrasAVerificar:
        u = (x[0] * pesosOr[0]) + (x[1] * pesosOr[1]) + pesosOr[2]
        y = sinal(u)
        if y == -1:
            print('classe A')
        else:
            print('classe B')

if __name__ == '__main__':
    treinador()
    operacao()
