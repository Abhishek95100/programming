balance = 6000
withdrawa = int(input("Enter the amount to withdrawal:"))

if withdrawa>balance:
    print_directory("insufficient balance")
else:
    balance = balance -withdrawa
    print("please collect your cash")