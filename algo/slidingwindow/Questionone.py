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

#print(find_average([1, 3, 2, 6, -1, 4, 1, 8, 2],5))

#Maximum Sum Subarray of Size K (easy)
def subarraysum(a,k):
    sum = 0.0
    start =0
    maxsub =0
    for i in range(len(a)):
        sum +=a[i]
        #print(i)
       # print(sum)
        if i >= k -1:
            maxsub = max(maxsub,sum)
           # result.append(sum)
            # if maxsub < sum:
            #     maxsub=sum
           #set sum to be less the first digit
            sum -= a[start]
            start+=1
            #print(j)
    return maxsub
print(subarraysum([2, 1, 5, 1, 3, 2],3 ))

print(subarraysum([2, 3, 4, 1, 5], 2 ))
