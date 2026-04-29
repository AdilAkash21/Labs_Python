
class Point3:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


p = Point3(0, 0, 0)

q = p

p.x = 5.6
q.x = 7.4

print(p.x)
print(q.x)