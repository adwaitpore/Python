Python 3.13.1 (tags/v3.13.1:0671451, Dec  3 2024, 19:06:28) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
... num1 = float(input("Enter the first number: "))
... num2 = float(input("Enter the second number: "))
... 
... print("\nChoose an operation:")
... print("1. Addition")
... print("2. Subtraction")
... print("3. Multiplication")
... print("4. Division")
... 
... choice = input("Enter your choice (1/2/3/4): ")
... 
... if choice == '1':
...     result = num1 + num2
...     print(f"\nThe result of addition is: {result}")
... elif choice == '2':
...     result = num1 - num2
...     print(f"\nThe result of subtraction is: {result}")
... elif choice == '3':
...     result = num1 * num2
...     print(f"\nThe result of multiplication is: {result}")
... elif choice == '4':
...     if num2 != 0:
...         result = num1 / num2
...         print(f"\nThe result of division is: {result}")
...     else:
...         print("\nDivision by zero is not allowed.")
... else:
...     print("\nInvalid choice. Please select a valid operation.")
