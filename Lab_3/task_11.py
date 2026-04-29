
class Point3:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z    

    def __str__(self):
        return f"({self.x},{self.y},{self.z})"


p = Point3(1, 2, 3)

# Print original point
print(p)

# Change attributes
p.x = 10
p.y = p.x + p.z

# Print updated point
print(p)
