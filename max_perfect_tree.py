def solution(node):
    max, _ = step(node)
    return max

def step(node):
    if node is None:
        return 0, 0
    if node.l is None and node.r is None:
        return 1, 1
    max_l, dep_l = step(node.l)
    max_r, dep_r = step(node.r)
    if dep_l == dep_r:
        return max_l + max_r + 1, dep_l + 1

    return max(max_l, max_r), 1