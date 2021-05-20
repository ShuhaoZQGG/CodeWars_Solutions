def namelist(names):
    #your code here
    #names is a type of list(dict)
    #want to return str(dict.values())
    
    #for each dictionary in the list
    if len(names) == 0:
        return ''
    elif len(names) == 1:
        return ''.join(list(d.values())[0] for d in names)
    elif len(names) == 2:
        return ' & '.join(list(d.values())[0] for d in names)
    else:  
        str = ', '.join(list(d.values())[0] for d in names)
        last_char_index = str.rfind(",")
        str = str[:last_char_index] + " &" + str[last_char_index+1:]
        
        
        return str

''' Other People's method
def namelist(names):
    if len(names) > 1:
        return '{} & {}'.format(', '.join(name['name'] for name in names[:-1]), 
                                names[-1]['name'])
    elif names:
        return names[0]['name']
    else:
        return ''
'''