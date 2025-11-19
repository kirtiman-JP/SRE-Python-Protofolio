print("Hello this is a Calculator capable of doing \"Addition\" \"Substraction\" \"Multiplication\" and \"Division\"")
print("please choose a function to do")
print("The following functions are:")
print("1. Addition (+)")
print("2. Substraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")
print("-" * 20)            
operation = (input("please enter the number (1, 2, 3, 4 or the symbols): "))
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
result = None
if operation == "1" or operation == "+":
     result = num1 + num2
elif operation == "2": or operation == "-": result = num1 - num2
elif operation == "3": or operation == "*":   result = num1 * num2
elif operation == "4": or operation == "/": if num2 == 0: print("\nError: Cannot devide by zero.") result = "Undefined"  else: result = num1 / num2
else: print("Invalid choice. please reastart and start again. \n Thank You.....")
if result is not None: print("-" * 20)
print("The final result is: {result}")
print("-" * 20)
print("Thank you for using the calci.")
