def main():
    print("Welcome to the Calculator App V1.0.0")
    
    while True:
        print("\nSelect operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Quit")
        
        choice = input("Enter choice (1/2/3/4/5): ")
        
        if choice == '5':
            print("Goodbye!")
            break
        
        if choice not in ['1', '2', '3', '4']:
            print("Invalid choice. Please try again.")
            continue
        
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter numbers.")
            continue
        
        if choice == '1':
            result = num1 + num2
            print(f"{num1} + {num2} = {result}")
        elif choice == '2':
            result = num1 - num2
            print(f"{num1} - {num2} = {result}")
        elif choice == '3':
            result = num1 * num2
            print(f"{num1} * {num2} = {result}")
        elif choice == '4':
            if num2 == 0:
                print("Cannot divide by zero.")
                continue
            result = num1 / num2
            print(f"{num1} / {num2} = {result}")

if __name__ == "__main__":
    main()