from collections import Counter


def containsDuplicate(nums):
    print(Counter(nums).most_common(nums))

    return 0


containsDuplicate([1, 2, 3, 1])
