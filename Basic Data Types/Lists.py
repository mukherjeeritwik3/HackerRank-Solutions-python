if __name__ == '__main__':
    N = int(input())
    list=[]
    for i in range(N):
        ins=input().split()


        if ins[0]=='insert':
            one=ins[1]
            two=ins[2]
            int_one=int(one)
            int_two=int(two)
            list.insert(int_one,int_two)
        elif ins[0]=='remove':
            one=ins[1]
            int_one=int(one)

            list.remove(int_one)
        elif ins[0]=='append':
            one=ins[1]
            int_one=int(one)
            list.append(int_one)
        elif ins[0]=='sort':
            list.sort()
        elif ins[0]=='reverse':
            list.reverse()
        elif ins[0]=='pop':
            list.pop()
        elif ins[0]=='print':
            print(list)
