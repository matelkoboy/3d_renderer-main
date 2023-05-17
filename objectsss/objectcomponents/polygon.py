from objectsss.objectcomponents.point import Point

class Poly:
    def __init__(self, light,  *points):
        self.points = points
        self.color = "#00FF00"
        a = Point(points[0].x - points[1].x, points[0].y - points[1].y, points[0].z - points[1].z)
        b = Point(points[2].x - points[1].x, points[2].y - points[1].y, points[2].z - points[1].z)
        
        norm_vector = Point(a.y * b.z - a.z * b.y,
                            a.z * b.x - a.x * b.z,
                            a.x * b.y - a.y * b.x)
        
        x_avg = sum([p.x for p in self.points]) / len(self.points)
        y_avg = sum([p.y for p in self.points]) / len(self.points)
        z_avg = sum([p.z for p in self.points]) / len(self.points)
        
        self.midpoint = Point(x_avg, y_avg, z_avg)
    
    def __str__(self):
        return str(self.midpoint) + str(self.points[0]) + str(self.points[1]) + str(self.points[2])