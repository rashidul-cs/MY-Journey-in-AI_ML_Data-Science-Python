
c = float(input("Enter Celcius Degrees: "))
# c/5 = (f-32)/9 = (k-273)/5
f = (9/5)*c + 32
k = c + 273
print("Fahrenheit Degrees:", round(f, 2))
print("Kelvin Degrees:", round(k, 2))
