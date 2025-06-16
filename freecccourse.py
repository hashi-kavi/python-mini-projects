
print("Basic Calculator!")
print("Here you can +,-,*,/")
while True:
    operation = input("Enter Your Operation or 'q' to Quit: ")
    if operation.lower()=='q':
        print("GoodBye!")
        break
    try:
        a = float(input("Enter 1st number: "))
        b = float(input("Enter 2nd number: "))

        if operation == "+":
            print(a+b)
        elif operation == "-":
            print(a-b)
        elif operation == "*":
            print(a * b)
        elif operation == "/":
            if b!= 0:
                print(a/b)
            else:
                print("Error:Division by zero")
        else:

            print("invalid operation .You can only choose from +, -, *, /")

    except ValueError:
        print("Invalid number input.Please enter numeric values only.")

