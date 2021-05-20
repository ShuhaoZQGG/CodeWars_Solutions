def likes(names):
    # your code here
    text = ""
    if len(names) == 0:
        text = "no one likes this"
    elif len(names) == 1:
        text = f"{names[0]} likes this"
    elif len(names) == 2:
        text = f"{names[0]} and {names[1]} like this"
    elif len(names) == 3:
        text = f"{names[0]}, {names[1]} and {names[2]} like this"
    elif len(names) > 2:
        text = f"{names[0]}, {names[1]} and {len(names)-2} others like this"
        
    
    return text
