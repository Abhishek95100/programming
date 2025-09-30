def check_prime_num():
    num = int(input("Enter the number:"))
    if num < 2:
        print(" not prime number")
        return

    for i in range(2, int(num**0.5) + 1):
        if num %i ==0:
            print("not prime number")
            return
    print("prime number")

check_prime_num()