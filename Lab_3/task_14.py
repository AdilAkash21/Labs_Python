
class Point3:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f"({self.x},{self.y},{self.z})"


def x_plus_y(pt):
    """Returns the sum of x and y for a Point3 object."""
    return pt.x + pt.y


def move_x(pt, amount):
    """Adds amount to the x coordinate of pt."""
    pt.x = pt.x + amount


# Test
p = Point3(2, 3, 4)

print(x_plus_y(p))  # 2 + 3 = 5

move_x(p, 5)
print(p)            # x becomes 2 + 5 = 7 → (7,3,4)