class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRU:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}

        self.head = Node("", "")
        self.tail = Node("", "")
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node: Node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def _add_front(self, node: Node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def _get(self, key):
        if key not in self.cache:
            return -1

        node = self.cache[key]
        self._remove(node)
        self._add_front(node)
        return node.value

    def _put(self, key: int, value: str):
        if key in self.cache:
            self.remove(self.chche[key])

        new_node = Node(key, value)
        self.cache[key] = new_node
        self._add_front(new_node)

        if len(self.cache) > self.capacity:
            del_node = self.tail.prev
            self._remove(del_node)
            del self.cache[del_node.key]


def solution(cacheSize, cities):
    lru = LRU(cacheSize)
    result = 0

    for i in cities:
        city = i.lower()

        if city in lru.cache:
            result += 1
            lru._get(city)
            continue

        lru._put(city, i)
        result += 5

    return result


# print(solution(
#     2,
#     ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]))
print(solution(
    2, ["Jeju", "Pangyo", "NewYork", "newyork"]))
