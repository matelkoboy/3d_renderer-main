from objectsss.objectcomponents.point import Point
from objectsss.objectcomponents.polygon import Poly
from visual.mesh_utils import dist_of_points

class Plane:
    def __init__(self, point_1, point_2, point_3):
        
        spec_point_x = point_3.x - point_2.x + point_1.x - point_2.x
        spec_point_y = point_3.y - point_2.y + point_1.y - point_2.y
        spec_point_z = point_3.z - point_2.z + point_1.z - point_2.z
        
        spec_point = Point(spec_point_x + point_2.x, spec_point_y + point_2.y, spec_point_z + point_2.z)
        
        
        self.poly = Poly(point_1, point_2, point_3, spec_point)
        
    def for_render(self):
        return [self.poly]