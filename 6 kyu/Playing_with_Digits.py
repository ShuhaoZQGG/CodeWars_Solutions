def dig_pow(n, p):
    # your code
    # n = x*p
    # n (a,b,c,d) for example 9476 (9,6,7,4)
    # Is there an integer k such as : (a ^ p + b ^ (p+1) + c ^(p+2) + d ^ (p+3) + ...) = n * k
    # first find every digit (a,b,c,d) of n
    x = 0
    n = str(n)
    digits = [int(digit) for digit in n]
    for count, ele in enumerate(digits):
        x += pow(ele,count+p)
    output = x/(int(n))
    if output.is_integer():
        return output
    else:
        return -1

#Best Practice
#def dig_pow(n, p):
#  s = 0
#  for i,c in enumerate(str(n)):
#     s += pow(int(c),p+i)
#  return s/n if s%n==0 else -1