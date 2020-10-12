
def main():

    greet = "Benvenuto nella calcolatrice autistica; scegli un opzione."
    print(greet)
    
    print("1. Addizione")
    print("2. Sottrazione")
    print("3. Moltiplicazione")
    print("4. Divisione")
    print("5. Esponenziale")
    print("6. Modulare")
    
    def addizione(n1, n2):
        return n1 + n2
    
    def sottrazione(n1, n2):
        return n1 - n2
    
    def moltiplicazione(n1, n2):
        return n1 * n2
    
    def divisione(n1, n2):
        return n1 / n2
    
    def esponenziale(n1, n2):
        return n1 ** n2
    
    def modulare(n1, n2):
        return n1 % n2
    
    while True:
        choice = input("Inserisci la tua opzione(1/2/3/4/5/6): ")
        
        if choice in ('1', '2', '3', '4', '5', '6'):
            num1 = float(input("Inserisci il primo numero: "))
            num2 = float(input("Inserisci il secondo numero: "))
            
            if choice == '1':
                print(num1, "+", num2, "=", addizione(num1, num2))
            
            elif choice == '2':
                print(num1, "-", num2, "=", sottrazione(num1, num2))
                
            elif choice == '3':
                print(num1, "*", num2, "=", moltiplicazione(num1, num2))
                
            elif choice == '4':
                print(num1, "/", num2, "=", divisione(num1, num2))
                
            elif choice == '5':
                print(num1, "**", num2, "=", esponenziale(num1, num2))
            
            elif choice == '6':
                print(num1, "%", num2, "=", modulare(num1, num2))
            
            break
    else:
        print("Input non valido")
        
        
if __name__ == "__main__":
    main()        