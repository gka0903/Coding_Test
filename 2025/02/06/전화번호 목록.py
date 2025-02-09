def solution(phone_book):
    hash_table = set()

    for phone in phone_book:
        for prefix in range(1, len(phone)):
            hash_table.add(phone[:prefix])

    for phone in phone_book:
        if phone in hash_table:
            return False
    return True


print(solution(["119", "97674223", "1195524421"]))
# print(solution(["123", "456", "789"]))
