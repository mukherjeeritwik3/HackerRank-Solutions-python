def mutate_string(string, position, character):

    string= list(string)
    s_size = len(string)
    for j in range(s_size):
        if j==position:
            string[j]=character
    strings = ""
    strs = strings.join(string)
    return(strs)

