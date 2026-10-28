
sum = 0
for i in range(1, 101):
    if (i%3 == 0 or i%5 == 0):
        if (i%15 == 0):
            continue
        else:
            sum += i
    if (sum >= 2000):
        break
print("Sum:", sum)
