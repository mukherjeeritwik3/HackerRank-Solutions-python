# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
s = set(map(int, input().split()))

m = int(input())
k = set(map(int, input().split()))

union_set = s.union(k)
print(len(union_set))
