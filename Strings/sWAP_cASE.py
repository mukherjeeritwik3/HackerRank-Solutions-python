def swap_case(s):
    ls = list(s)
    for i in range(len(ls)):
        tmp=ls[i]
        if ls[i]==tmp.upper():
            ls[i]=tmp.lower()
        elif ls[i]==tmp.lower():
            ls[i]=tmp.upper()
    str1=""
    return(str1.join(ls))

