import heapq

# python에서 heapq 라이브러리는 max heap을 따로 제공하지 않기 때문에 들어가는
# 값의 부호를 바꾸고 이를 출력할 때 부호를 반대로 넣으면 임의적으로 max heap을 구현할 수 있다
def heapsort(list):
    h = []
    result = []
    for value in list:
        heapq.heappush(h, -value)
    for i in range(len(h)):
        result.append(-(heapq.heappop(h)))
    return result


print(heapsort((2, 5, 3, 1, 35, 25, 100, 2, 11, 23)))
