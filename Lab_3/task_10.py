
class Point3:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z        
    
p = Point3(4, 5, 6)

# Print attributes
print(p.x)
print(p.y)
print(p.z)

# Compute and store sum
a = p.x + p.y

# Print result
print(a)
