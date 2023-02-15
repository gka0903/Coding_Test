def findArray(pref):
    arr = [pref[0]]
    for i in range(len(pref) - 1):
        arr.append(pref[i] ^ pref[i + 1])
    return arr


print(findArray([5, 2, 0, 3, 1]))
