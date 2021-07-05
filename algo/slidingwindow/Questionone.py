def find_average(a,n):

    result = []
    arr =[]
    Sum = 0.0
    count =0
    for i in range(len(a)):
        count+=1
        print("Initial", arr)
        arr.append(a[i])
        if count>=n:
            print(arr)
            Sum = sum(arr)/n
            result.append(Sum)
            arr.pop(0)
            print(Sum)
    return result

print(find_average([1, 3, 2, 6, -1, 4, 1, 8, 2],5))
