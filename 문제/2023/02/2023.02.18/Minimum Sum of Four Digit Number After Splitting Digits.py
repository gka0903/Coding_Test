def minimumSum(num):
    numbers = [i for i in str(num)]
    answer = 0
    while numbers:
        m_ax = max(numbers)
        m_in = min(numbers)
        numbers.remove(m_ax)
        numbers.remove(m_in)
        n = m_in + m_ax
        answer += int(n)
    return answer


print(minimumSum(2932))
