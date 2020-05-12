# Enter your code here. Read input from STDIN. Print output to STDOUT
M = int(input())
a = input().split()
lists_a = list(map(int,a))
mylist_a = list()
mylist_a = lists_a[:M]
mySet_a = set(mylist_a)
N = int(input())
b = input().split()
lists_b = list(map(int,b))
mylist_b = lists_b[:N]
mySet_b = set(mylist_b)
diff_a = mySet_a.difference(mylist_b)
diff_b = mySet_b.difference(mylist_a)
total = diff_a
total.update(diff_b)
total_list = list(total)
total_list.sort()
for i in range(len(total_list)):
    print(total_list[i])
