def somar_dois(a, b):
    return f"{a}+{b}={a+b}"


inputA = []
inputB = []
results = []


while True:
    try:
        a = int(input("Numero 1: "))
        b = int(input("Numero 2: "))
    except ValueError as v_error:
        print("Erro Inserção de Valor: ", v_error)
        break
    except TypeError as t_error:
        print("Erro de Tipo de Input: ", t_error)

    result = somar_dois(a, b)
    inputA.append(a)
    inputB.append(b)
    results.append(result)

inputA += [x*2 for x in inputA]
inputA.sort()
inputB += [y*2 for y in inputB]
inputB.sort()


print(inputA)
print(inputB)
