def minPartitions(n) -> int:
    m = 0
    for i in n:
        num = int(i)
        m = max(m, num)
    return m


print(minPartitions("27346209830709182346"))
