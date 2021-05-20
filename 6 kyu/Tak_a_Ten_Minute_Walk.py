def is_valid_walk(walk):
    #determine if walk is valid
    # if number of 'n' = number of 's'
    # if number of 'e' = number of 'w'
    # if the len = 10
    # input walk is a list type
    my_dict = {i:walk.count(i) for i in walk}
    num_n = my_dict.get('n')
    num_s = my_dict.get('s')
    num_e = my_dict.get('e')
    num_w = my_dict.get('w')
    if len(walk) != 10:
        return False
    if num_n == num_s and num_e == num_w:
        return True
    else:
        return False