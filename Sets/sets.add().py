# Enter your code here. Read input from STDIN. Print output to STDOUT
total_number_of_INPUTS = int(input())
Sets = set()
for i in range(total_number_of_INPUTS):
    new = input()
    Sets.add(new)
print(len(Sets))
