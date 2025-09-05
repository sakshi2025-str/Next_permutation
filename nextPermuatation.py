def nextPermutation( arr):
    n = len(arr)
    idx = -1
    for i in range(n-2,-1,-1):
        if arr[i] < arr[i+1]:
            idx = arr[i]
            break
    if idx == -1:
        arr.reverse()
        return arr
    for i in range(n-1,idx,-1):
        if arr[i] > arr[idx]:
            arr[i],arr[idx] = arr[idx],arr[i]
            break
    arr[idx+1:] = reversed(arr[idx+1:])
    return arr


arr = list(map(int,input("enter the array:").split()))
print("after permuatation array is:" , nextPermutation(arr))