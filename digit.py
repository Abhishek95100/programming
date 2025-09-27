# एक number लो और उसके सारे digits का sum निकालो (जैसे 123 → 1+2+3 = 6)।

num = int (input ("Enter th number:"))

total = 0
while num >0 :
    digit = num %10
    total = total + digit
    num = num//10
print ("sum of digit ",total)