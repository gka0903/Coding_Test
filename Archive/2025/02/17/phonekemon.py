def solution(nums):
    pokemon_catch = set()
    can_take = len(nums) // 2
    catches = 0

    for num in nums:
        if num not in pokemon_catch:
            pokemon_catch.add(num)
            catches += 1

        if catches == can_take:
            break

    return catches


print(solution([3, 3, 3, 2, 2, 2]))
