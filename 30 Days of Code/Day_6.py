# Enter your code here. Read input from STDIN. Print output to STDOUT
total = int(input())
arr = []
for i in range(total):
    a = input()
    arr.append(a)
for j in range(len(arr)):
    odd = ""
    even = ""
    for k in range(len(arr[j])):
        if k%2==0:
            odd = odd+arr[j][k]
        else:
            even = even +arr[j][k]
    print(odd,even)
