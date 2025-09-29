# एक tuple (1,2,3,4,5,6) से केवल even numbers निकालकर list बनाओ।

tple = (1,2,3,4,5,6)
even_number = [num for num in tple if num % 2 == 0]

print("even number:",even_number)