n = int(input())
s = set(map(int, input().split()))

m = int(input())

for i in range(m):
    inputs = list(input().split())

    if inputs[0]=="pop":
        s.pop()
    elif inputs[0]=="remove":
        s.remove(int(inputs[1]))
    elif inputs[0]=="discard":
        s.discard(int(inputs[1]))

sum_s = sum(s)
print(sum_s)
