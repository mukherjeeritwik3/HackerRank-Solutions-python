def average(array):
    array = set(array)
    array = list(array)
    length = len(array)
    sum = 0
    for i in range(length):
        sum += array[i]
    avg = sum/length
    return(avg)
