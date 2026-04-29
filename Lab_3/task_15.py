
class Point3:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f"({self.x},{self.y},{self.z})"


def reset_to_origin(pt):
    """Changes pt so that it becomes the origin (0,0,0)."""
    pt.x = 0
    pt.y = 0
    pt.z = 0


# Test
p = Point3(8, 9, 10)
print(p)

reset_to_origin(p)

print(p)