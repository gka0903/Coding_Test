class Node:
    """이중 연결 리스트의 노드 정의"""

    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:
    """LRU 캐시 구현 (Doubly Linked List + HashMap)"""

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # { key: Node }

        # 가상의 head(더미 노드)와 tail(더미 노드) 생성 (이중 연결 리스트의 경계)
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node: Node):
        """이중 연결 리스트에서 노드를 제거"""
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def _add_to_front(self, node: Node):
        """노드를 가장 최근 사용된 위치(헤드 바로 뒤)로 이동"""
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def get(self, key: int) -> int:
        """캐시에서 데이터를 가져옴 (O(1))"""
        if key not in self.cache:
            return -1  # 캐시에 없는 경우

        node = self.cache[key]
        self._remove(node)  # 기존 위치에서 삭제
        self._add_to_front(node)  # 가장 최근 사용된 위치로 이동
        return node.value

    def put(self, key: int, value: int) -> None:
        """캐시에 데이터를 추가 (O(1))"""
        if key in self.cache:
            # 기존 값 업데이트 후, 최근 사용된 위치로 이동
            self._remove(self.cache[key])

        new_node = Node(key, value)
        self.cache[key] = new_node
        self._add_to_front(new_node)

        if len(self.cache) > self.capacity:
            # 가장 오래된 항목 제거 (tail의 이전 노드)
            lru_node = self.tail.prev
            self._remove(lru_node)
            del self.cache[lru_node.key]  # 해시맵에서도 삭제


# 🔹 실행 예제
lru = LRUCache(2)
lru.put(1, 10)  # {1=10}
lru.put(2, 20)  # {1=10, 2=20}
print(lru.get(1))  # 10 (1이 최근 사용됨 → {2=20, 1=10})
lru.put(3, 30)  # {1=10, 3=30} (2가 제거됨)
print(lru.get(2))  # -1 (2는 캐시에서 제거됨)
lru.put(4, 40)  # {3=30, 4=40} (1이 제거됨)
print(lru.get(1))  # -1 (1은 제거됨)
print(lru.get(3))  # 30
print(lru.get(4))  # 40

# ㄹㅏ이브러리 사용
from collections import OrderedDict


class LRUCache:
    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1  # 캐시에 데이터가 없으면 -1 반환
        self.cache.move_to_end(key)  # 최근에 사용된 것으로 업데이트
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.move_to_end(key)  # 기존 데이터는 최근 사용된 것으로 이동
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)  # 가장 오래된 항목 제거 (FIFO 방식)


# 🔹 실행 예제
lru = LRUCache(2)
lru.put(1, 10)  # {1=10}
lru.put(2, 20)  # {1=10, 2=20}
print(lru.get(1))  # 10 (1이 최근 사용됨 → {2=20, 1=10})
lru.put(3, 30)  # {1=10, 3=30} (2가 제거됨)
print(lru.get(2))  # -1 (2는 캐시에서 제거됨)
lru.put(4, 40)  # {3=30, 4=40} (1이 제거됨)
print(lru.get(1))  # -1 (1은 제거됨)
print(lru.get(3))  # 30
print(lru.get(4))  # 40

# 라이브러리 사용2
from functools import lru_cache


@lru_cache(maxsize=3)
def slow_function(n):
    print(f"Calculating {n}...")
    return n * n


# 🔹 실행 예제
print(slow_function(2))  # Calculating 2... → 4
print(slow_function(3))  # Calculating 3... → 9
print(slow_function(4))  # Calculating 4... → 16
print(slow_function(2))  # 캐시에서 가져옴 (Calculating 생략) → 4
print(slow_function(5))  # Calcul
