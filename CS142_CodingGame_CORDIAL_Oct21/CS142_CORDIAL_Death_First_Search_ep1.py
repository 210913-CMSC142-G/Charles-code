def getBestBloker(si, gate):
    global link
    for g in gate:
        if g in link[si]:
            return [si, g]
    for g in gate:
        if len(link[g]) > 0:
            return [g, link[g][0]]
    return [0, 0]


def unsetter(c1, c2):
    global link
    link[c1].remove(c2)
    link[c2].remove(c1)


n, l, e = [int(i) for i in input().split()]
gate = []
link = {}
for i in range(l):
    n1, n2 = [int(j) for j in input().split()]
    link.setdefault(n1, []).append(n2)
    link.setdefault(n2, []).append(n1)
for i in range(e):
    ei = int(input())
    gate.append(ei)
# game loop
while True:
    si = int(input())
    c1, c2 = getBestBloker(si, gate)
    unsetter(c1, c2)
    print("{0} {1}".format(c1, c2))