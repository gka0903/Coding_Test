def prime_factors(self, x: int):
    result = x
    arr = []
    while x != 1:
        for i in range(2, x + 1):
            if x % i == 0:
                x //= i
                arr.append(i)
                break
    if sum(arr) == 4:
        return 4
    elif len(arr) >= 2:
        return self.prime_factors(sum(arr))
    else:
        return result


def smallestValue(self, n: int) -> int:
    answer = self.prime_factors(n)
    return answer




print(smallestValue(15))
