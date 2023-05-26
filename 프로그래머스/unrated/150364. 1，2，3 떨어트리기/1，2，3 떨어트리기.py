from collections import defaultdict

def solution(edges, target):
    answer = []    
    nodes = create_node2tree(edges)
    node2min, node2max = create_node2minmax(target)
    node2visit, visit = create_node2visit(nodes, node2min, node2max)
    if node2visit == [-1]:
        return node2visit
    node2nums = create_node2nums(node2visit, target)
    
    for v in visit:
        answer.append(node2nums[v].pop())
    
    return answer
    
def create_node2tree(edges):
    node_tree = defaultdict(list)
    
    for parent, children in edges:
        node_tree[parent].append(children)
    
    for _, children in node_tree.items():
        children.sort()
    
    return node_tree

def create_node2minmax(target):
    node2min = defaultdict(int)
    node2max = defaultdict(int)
    
    for node, t in enumerate(target, 1):
        node2max[node] = t
        three, other = divmod(t, 3)
        if other:
            node2min[node] += 1
        node2min[node] += three
    
    return node2min, node2max
    
def create_node2visit(nodes, node2min, node2max):
    node2visit = defaultdict(int)
    node2idx = defaultdict(int)
    required = sum(node2min.values())
    visit = []
    
    while required:
        parent = 1
        while nodes[parent]:
            idx = node2idx[parent]
            child = nodes[parent][idx]
            idx += 1
            if idx == len(nodes[parent]):
                idx = 0
            node2idx[parent] = idx
            parent = child
        node2visit[parent] += 1
        visit.append(parent)
        if node2visit[parent] <= node2min[parent]:
            required -= 1
        elif node2visit[parent] > node2max[parent]:
            return [-1], visit
    return node2visit, visit

def create_node2nums(node2visit, target):
    node2nums = defaultdict(list)

    for node, t in enumerate(target, 1):
        three, two = divmod(t - node2visit[node], 2)
        for _ in range(three):
            node2nums[node].append(3)
        if two:
            node2nums[node].append(2)
        while len(node2nums[node]) < node2visit[node]:
            node2nums[node].append(1)
    return node2nums