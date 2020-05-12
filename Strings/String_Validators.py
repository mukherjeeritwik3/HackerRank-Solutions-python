
if __name__ == '__main__':

    s = input()
    s = str(s)
    isalnum = any(char.isalnum() for char in s)
    isalpha = any(char.isalpha() for char in s)
    isdigit = any(char.isdigit() for char in s)
    islower = any(char.islower() for char in s)
    isupper = any(char.isupper() for char in s)
    count = 0
    val = [isalnum, isalpha, isdigit, islower, isupper]
    for i in range(len(val)):
        print(val[i])
