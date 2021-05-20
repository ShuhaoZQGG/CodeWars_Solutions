def accum(s):
    # your code
    # s is a string
    #for every character in s, repeat itself by the number of its location number. The first appearance
    #be upper case. For example:
    #accum("abcd") -> "A-Bb-Ccc-Dddd"
    #accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
    #accum("cwAt") -> "C-Ww-Aaa-Tttt"
    str = ""
    for i,c in enumerate(s):
        c =c.upper()+c.lower()*i
        c+='-'
        str += c
    
    str = str[:-1]
    return str


''' Other People's optimized solutions:
def accum(s):
    return '-'.join(c.upper() + c.lower() * i for i, c in enumerate(s))
'''