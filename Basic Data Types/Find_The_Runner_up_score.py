if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    list = set(arr)
    list.remove(max(list))
    print(max(list))
