class Disjointset:
    def __init__(self, n):
        self.data = list(range(n))
        self.size = n

    def find(self, index):
        return self.data[index]

    def union(self, x, y):
        x, y = self.find(x), self.find(y)
        if x == y:
            return

        for i in range(self.size):
            if self.find(i) == y:
                self.data[i] = x

        def length(self):
            return len(set(self.data))

disjoint = Disjointset(10)
print(disjoint.data)
print(disjoint.size)

disjoint.union(0, 1)
disjoint.union(1, 2)
disjoint.union(2, 3)
disjoint.union(4, 5)
disjoint.union(5, 6)
disjoint.union(6, 7)
disjoint.union(8, 9)

print(disjoint.data)

# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# 10
# [0, 0, 0, 0, 4, 4, 4, 4, 8, 8]