from collections import deque
from platform import node
from typing import Any

__all__ = (
    'Node',
    'Graph'
)


class Node:
    def __init__(self, value: Any):
        self.value = value

        self.outbound = []
        self.inbound = []

    def point_to(self, other: 'Node'):
        self.outbound.append(other)
        other.inbound.append(self)

    def __str__(self):
        return f'Node({repr(self.value)})'

    __repr__ = __str__


class Graph:
    def __init__(self, root: Node):
        self._root = root

    def dfs(self) -> list[Node]:
        visited = []
        nodes_queue = deque()
        nodes_queue.append(self._root)
        while nodes_queue:
            cur_node = nodes_queue.pop()
            if cur_node not in visited:
                visited.append(cur_node)
            for node in reversed(cur_node.outbound):
                if node not in visited:
                    nodes_queue.append(node)
        return visited

    def bfs(self) -> list[Node]:
        nodes_queue = deque()
        nodes_queue.append(self._root)
        visited = []
        visited.append(self._root)
        while nodes_queue:
            cur_node = nodes_queue.popleft()
            for node in cur_node.outbound:
                if node not in visited:
                    visited.append(node)
                    nodes_queue.append(node)
        return visited
