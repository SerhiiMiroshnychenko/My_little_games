def calculator():
    """Simple calculator --- Простий калькулятор."""
    print("\nSIMPLE CALCULATOR --- ПРОСТИЙ КАЛЬКУЛЯТОР")
    print('Quit --- Вихід: "q"\n\n')
    while True:
        calculation = input("Enter your calculation --- Введіть обчислення: ")
        if calculation == "q":
            print("END...")
            break
        try:
            result = eval(calculation)
            print(f"\t\t\t\t\t\t Result --- Результат: {result}\n")
        except:
            print("\t\tSomething is wrong --- Щось не так...\n")


calculator()
