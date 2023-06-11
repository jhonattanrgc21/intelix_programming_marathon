def es_primo(n):
    flag = True
    count = 1
    i = 2
    while(i < n and flag):
        if(n % i == 0):
            flag = False
        else:
            i += 1
            
    return flag
    
def main():
    line = input().split(',')
    count_primos = 0
    for value in line:
        value = int(value)
        if(es_primo(value)):
            print('Cache refreshed: Yes')
            count_primos += 1
        else:
            print('Cache refreshed: No')
            
    print('Cache was refreshed {} times.'.format(count_primos))
    
if(__name__ == '__main__'):
    main()