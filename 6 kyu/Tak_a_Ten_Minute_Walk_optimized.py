# compared to the first attempt, this version of solution is more compact since list.count() built in function
def isValidWalk(walk):
    return len(walk) == 10 and walk.count('n') == walk.count('s') and walk.count('e') == walk.count('w')