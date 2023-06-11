def calcular(a, b, operador):
    a = int(a)
    b = int(b)
    
    if(operador == '+'):
        result = a + b
    
    if(operador == '-'):
        result = a - b
        
    if(operador == '*'):
        result = a * b
        
    if(operador == '/'):
        result = a / b

    return result


def main():
    cases = int(input())
    for case in range(cases):
        line = input().split()
        izquierda = calcular(line[0], line[1], line[2])
        derecha =  calcular(izquierda, line[3], line[4])
        print(derecha)

if(__name__ == '__main__'):
    main()