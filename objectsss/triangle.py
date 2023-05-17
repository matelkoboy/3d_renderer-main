from objectsss.objectcomponents.point import Point
from objectsss.objectcomponents.polygon import Poly
from visual.mesh_utils import dist_of_points

class Triangle:
    def __init__(self, point_1, point_2, point_3, light):
        self.poly = Poly(light, point_1, point_2, point_3)
        
    def for_render(self):
        return [self.poly]