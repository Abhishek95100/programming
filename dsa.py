def is_palindrone(n):
    num = n 
    result = 0
    while num>0:
        id = num%10
        result = (result * 10)+id
        num = num // 10
    return n == result

print(is_palindrone(1234))