n = int(input())
s = set(map(int, input().split()))

m = int(input())
k = set(map(int, input().split()))

inter_set = s.intersection(k)
print(len(inter_set))
