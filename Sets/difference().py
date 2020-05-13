n = int(input())
english = set(map(int, input().split()))

m = int(input())
french = set(map(int, input().split()))

diff_set = english.difference(french)
print(len(diff_set))
