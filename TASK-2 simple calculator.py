while True:
    print("\nSimple Calculator:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")
    choice = input("Enter your choice (1-5): ")
    
    if choice > "5":
      print("Invalid choice. Please enter a number between 1 and 5.")
      continue
    elif choice == "5":
      print("Exiting the calculator. Goodbye!") 
      break
    n1 = float(input("Enter the first number: "))
    n2 = float(input("Enter the second number: "))
    if choice == "1":
       result = n1 + n2
       operation = "Addition"
    elif choice == "2":
       result = n1 - n2
       operation = "Subtraction"
    elif choice == "3":
       result = n1 * n2
       operation = "Multiplication"
    elif choice == "4":
       if n2 != 0:
        result = n1 / n2
        operation = "Division"
       else:
        print("Error: Cannot divide by zero.")
        continue
print(f"{operation} result: {result}")
