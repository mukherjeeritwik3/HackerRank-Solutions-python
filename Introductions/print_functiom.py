if __name__ == '__main__':
    n = int(input())
    next = n+1
    arr= []
    for i in range(1,next):
        arr.append(i)
    
    strings = [str(integer) for integer in arr]   
    string = "".join(strings)
    print(string) 
        
