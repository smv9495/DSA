class Node():
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

ls = [('a', 'b'), ('b', 'c'), ('x', 'y'), ('z', 'c'), ('p', 'r')]
node_cache = dict()
for pair in ls:
    i, j = pair
    if not node_cache.get(i):
        node_i = Node(i)
        node_cache[i] = node_i
    else:
        node_i = node_cache.get(i)
    if not node_cache.get(j):
        node_j = Node(j)
        node_cache[j] = node_j
    else:
        node_j = node_cache.get(j)
    node_i.next = node_j


class solution():
    def find_intersection(self, node_value_list):
        paths = []
        sum = 0
        for value in node_value_list:
            set_ = set()
            node = node_cache.get(value)
            while node:
                set_.add(node.value)
                node = node.next
            paths.append(set_)
            sum += len(set_)
        union_set = set()
        for i in range(len(paths)):
            union_set = union_set.union(paths[i])
        if len(union_set) == sum:
            print(False)
        else:
            print(True)

l1 = ['a', 'r', 'z']
l2 = ['p', 'c']
l3 = ['b', 'z']
solution().find_intersection(l1)
solution().find_intersection(l2)
solution().find_intersection(l3)