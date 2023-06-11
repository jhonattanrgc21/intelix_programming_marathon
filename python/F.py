def main():
    n = int(input())
    
    lien = input().split()
    array = [float(value) for value in lien]
    
    min_value = min(array)
    max_value = max(array)
    average = sum(array) / n
    
    sd = 0.0
    denominador = n - 1
    for i in range(1, n+1):
        numerador = ((array[i-1] - average) ** 2)
        sd +=  numerador /  denominador
    
    sd = sd ** 1/2
    
    print('{:.2f} {:.2f} {:.2f} {:.2f}'.format(average, sd, min_value, max_value))

if(__name__ == '__main__'):
    main()