import math
def find_next_square(sq):
    # Return the next square if sq is a square, -1 otherwise
    sqrt = math.isqrt(sq)
    if pow(sqrt,2) ==  sq:
        next_number = math.sqrt(sq)+1
        return math.pow(next_number,2)
    else:
        return -1