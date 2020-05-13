n = int(input())
s = set(map(int, input().split()))

m = int(input())
k = set(map(int, input().split()))

symetric_difference_set = s.symmetric_difference(k)
print(len(symetric_difference_set))
