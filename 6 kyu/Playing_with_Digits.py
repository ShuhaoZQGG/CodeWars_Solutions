n = 46288
n = str(n)
digits = [int(digit) for digit in n]
print(digits)
x=0
for count, ele in enumerate(digits):
    x += pow(ele,count+1)
print(x)
output = x/(int(n))
print(output)