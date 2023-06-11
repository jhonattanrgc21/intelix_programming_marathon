def main():
    cases = int(input())
    
    for case in range(cases):
        line = input().split()
        years = int(line[0])
        balance = float(line[1])
        percentage = int(line[2])
        
        acum = balance
        for year in range(1, years + 1):
            acum += (acum * percentage) / 100
        
        print('Savings account balance after {} years is : AMD {:.2f}.'.format(years, acum))

if(__name__ == '__main__'):
    main()