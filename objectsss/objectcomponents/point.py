from math import ceil

class Point:
    def __init__(self, x, y, z):
        self.x = round(x, 12)
        self.y = round(y, 12)
        self.z = round(z, 12)
    
    def __str__(self) -> str:
        return f"{self.x, self.y, self.z}"