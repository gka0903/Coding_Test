def solution(arr):
    a = ''
    for i in range(len(arr)):
        if a == arr[i]:
            arr[i] = " "
        else:
            a = arr[i]

    print(arr)
    for i in arr:
        if i == " ":
            arr.remove(" ")
    
    return arr

print(solution([1,1,3,3,0,1,1]))
print(solution([4,4,4,3,3,3]))