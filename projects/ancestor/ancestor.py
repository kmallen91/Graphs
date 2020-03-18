from stack import Stack


def earliest_ancestor(ancestors, starting_node):
    verticies = {}
    for i in ancestors:
        if i[1] in verticies:
            verticies[i[1]].add(i[0])
        else:
            verticies[i[1]] = set([i[0]])
    print(verticies)
    s = Stack()
    visited = set()
    s.push(starting_node)
    while s.size() > 0:
        v = s.pop()
        if v not in visited:
            visited.add(v)
            if v in verticies:
                if len(verticies[v]) > 1:
                    parents = []
                    for neighbor in verticies[v]:
                        parents.append(neighbor)
                    if parents[1] < parents[0]:
                        s.push(parents[1])
                        s.push(parents[0])
                    else:
                        s.push(parents[0])
                        s.push(parents[1])
                else:
                    for neighbor in verticies[v]:
                        s.push(neighbor)

            elif v not in verticies and v == starting_node:
                return -1
            elif v not in verticies and s.size == 0:
                parents.append(v)
    return v


test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7),
                  (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]

earliest_ancestor(test_ancestors, 3)
