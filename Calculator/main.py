while True:
    try:
        a = int(input("Enter the first number: "))
        b = int(input("Enter the second number: "))
        # print("Operation (+,-,*,/): ")
        operation = input("Enter Opartion (+,-,*,/): ")
        match operation:
            case "+":
                print(f"The result is: {a+b}")
            case "-":
                print(f"The result is: {a-b}")
            case "*":
                print(f"The result is: {a*b}")
            case "/":
                print(f"The result is: {a/b}")
            case default:
                print("Error!!")

    except ValueError:
        choice =input("Do you want to quit ? (y/n): ").lower()
        if choice == "y":
            break
        else:
            print("Please enter valid number!!\n")
            continue
