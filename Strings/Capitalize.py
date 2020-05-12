def solve(s):
    list_s= list(s)
    list_s[0]= list_s[0].upper()
    for i in range(len(list_s)):
        if list_s[i].isspace()==True:
            list_s[i+1]=list_s[i+1].upper()
    join = "".join(list_s)
    return(join)
