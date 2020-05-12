def minion_game(string):
    staurt = 0
    kevin = 0
    n = len(s)
        
    for i in range(n):
        if s[i] in ('A','E','I','O','U'):
            kevin += n-i
        else:
            staurt += n-i
    if kevin>staurt:
        print('Kevin', kevin)
    elif staurt>kevin:
        print('Stuart', staurt)
    else:
        print('Draw')    

