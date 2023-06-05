def main():
    expresion = input()
    
    #Opcion 1
    resultado = ''.join(dict.fromkeys(expresion))
    
    # Opcion 2
    # resultado = str()
    # for letra in expresion:
    #     if(letra not in resultado):
    #         resultado += letra
        
    print(resultado)

if(__name__ == '__main__'):
    main()