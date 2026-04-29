
class Point3:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f"({self.x},{self.y},{self.z})"


def incr_x(pt):
    """Adds 1 to the x attribute of pt."""
    pt.x = pt.x + 1


# Test
p = Point3(1, 2, 3)
print(p)

# Call it four times
incr_x(p)
incr_x(p)
incr_x(p)
incr_x(p)

print(p)