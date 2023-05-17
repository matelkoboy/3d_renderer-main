from math import tan, radians, sin, cos
from objectsss.objectcomponents.point import Point

class Cam:
    def __init__(self, width, height, fov):
        self.x = 50
        self.y = 120
        self.z = -500
        self.h_rot = 0
        self.v_rot = 0
        self.plane_width = width
        self.plane_height = height
        
        self.start_v_rot_axix = Point(1, 0, 0)
        self.v_rot_axix = self.start_v_rot_axix
        
        dist_of_plane_and_point = width / (tan(radians(fov) / 2) * 2)
        print(dist_of_plane_and_point)
        self.start_norm = Point(0, 0, dist_of_plane_and_point)
        self.normal_vect = self.start_norm
        
        self.center_of_plane = Point(self.x + self.normal_vect.x, self.y + self.normal_vect.y, self.z + self.normal_vect.z)
        self.rotated_center_of_plane = self.center_of_plane
    
    #TODO
    def move(self, local_x, local_y, local_z):
        self.x += sin(radians(-self.h_rot)) * local_z + cos(radians(-self.h_rot)) * local_x
        self.z += cos(radians(self.h_rot)) * local_z + sin(radians(self.h_rot)) * local_x
        self.y += local_y
    
    def rotate(self, vect, axis, angle):
        (v1, v2, v3) = (vect.x, vect.y, vect.z)
        (a1, a2, a3) = (axis.x, axis.y, axis.z)
    
        c = cos(radians(angle))
        s = sin(radians(angle))
    
        cv1 = v1 * c
        cv2 = v2 * c
        cv3 = v3 * c
    
        cross1, cross2, cross3 = (v2 * a3) - (v3 * a2), (v3 * a1) - (v1 * a3), (v1 * a2) - (v2 * a1)
        cross1 *= s
        cross2 *= s
        cross3 *= s
    
        scalar = v1 * a1 + v2 * a2 + v3 * a3
    
        a1 *= scalar * (1 - c)
        a2 *= scalar * (1 - c)
        a3 *= scalar * (1 - c)
    
        return Point(cv1 + cross1 + a1, cv2 + cross2 + a2, cv3 + cross3 + a3)
    
    def update_plane(self):
        self.v_rot_axix = self.rotate(self.start_v_rot_axix, Point(0, 1, 0), self.h_rot)
        self.normal_vect = self.rotate(self.rotate(self.start_norm, Point(0, 1, 0), self.h_rot), self.v_rot_axix, self.v_rot)
        self.center_of_plane = Point(self.x + self.normal_vect.x, self.y + self.normal_vect.y, self.z + self.normal_vect.z)
        xd = Point(self.center_of_plane.x - self.x, 
                    self.center_of_plane.y - self.y, 
                    self.center_of_plane.z - self.z)
        temp = self.rotate(xd, self.v_rot_axix, -self.v_rot)
        self.rotated_center_of_plane = self.rotate(temp, Point(0, 1, 0), -self.h_rot)
            
        
    def project_point_on_plane(self, point):
        a1 = self.normal_vect.x * (point.x - self.center_of_plane.x)
        a2 = self.normal_vect.y * (point.y - self.center_of_plane.y)
        a3 = self.normal_vect.z * (point.z - self.center_of_plane.z)
        
        b1 = self.normal_vect.x * (point.x - self.x)
        b2 = self.normal_vect.y * (point.y - self.y)
        b3 = self.normal_vect.z * (point.z - self.z)
        
        try:
            t = (a1 + a2 + a3) / (b1 + b2 + b3)
        except ZeroDivisionError:
            return ()
        if t > 1 or t < -20000:
            return ()
        
        
        point_on_plane = Point(
            point.x + t * (self.x - point.x),
            point.y + t * (self.y - point.y),
            point.z + t * (self.z - point.z)
        )
        
        rotated_point = self.rotate(self.rotate(Point(point_on_plane.x - self.x, 
                                                        point_on_plane.y - self.y, 
                                                        point_on_plane.z - self.z),
                                                        self.v_rot_axix, -self.v_rot),
                                                    Point(0, 1, 0), -self.h_rot)
        
        return self.plane_width / 2 + rotated_point.x - self.rotated_center_of_plane.x, self.plane_height - (self.plane_height / 2 + rotated_point.y - self.rotated_center_of_plane.y)
        