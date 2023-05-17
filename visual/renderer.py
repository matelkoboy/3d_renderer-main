from visual.mesh_utils import dist_of_closest_point, dist_of_points
from objectsss.objectcomponents.point import Point
import time

render_list = []

def add_to_renderer(obj):
    render_list.extend(obj.for_render())
    
def render_poly(polyg, canvas, camera):
    points = []
    for point in polyg.points:
        points.extend(camera.project_point_on_plane(point))
    try:
        canvas.create_polygon(points, fill=polyg.color, outline="black", width=3)
    except:
        pass
    canvas.pack()
    
def sort_polygons_painters(camera):
    return sorted(render_list, key=lambda poly: dist_of_points(poly.midpoint, camera), reverse=True)
    
def sort_polygons_new(camera):
    temp = sorted(render_list, key=lambda poly: dist_of_points(poly.midpoint, camera), reverse=True)
    
    for i in range(1, len(temp)):
        poly_points = temp[i - 1].points
        a = Point(poly_points[1].x - poly_points[0].x,
                  poly_points[1].y - poly_points[0].y,
                  poly_points[1].z - poly_points[0].z)
        b = Point(poly_points[2].x - poly_points[0].x,
                  poly_points[2].y - poly_points[0].y,
                  poly_points[2].z - poly_points[0].z)
        
        norm_vector_of_poly_plane = Point(a.y * b.z - a.z * b.y,
                                          a.z * b.x - a.x * b.z,
                                          a.x * b.y - a.y * b.x)
        
        while True:
            flag = False
            lis = list(temp[i].points)
            lis.append(temp[i].midpoint)
            for point in lis:
                
                a1 = norm_vector_of_poly_plane.x * (point.x - poly_points[0].x)
                a2 = norm_vector_of_poly_plane.y * (point.y - poly_points[0].y)
                a3 = norm_vector_of_poly_plane.z * (point.z - poly_points[0].z)
            
                b1 = norm_vector_of_poly_plane.x * (point.x - camera.x)
                b2 = norm_vector_of_poly_plane.y * (point.y - camera.y)
                b3 = norm_vector_of_poly_plane.z * (point.z - camera.z)
            
                t = (a1 + a2 + a3) / (b1 + b2 + b3)
                if t > 0 and t < 1:
                    temp[i - 1], temp[i] = temp[i], temp[i - 1]
                    flag = True
                    break
            if flag == False:
                break
            
    
    return temp

    
def render_all(canvas, camera):
    #pretty shitty
    final_order = sort_polygons_painters(camera)
    
    for poly in final_order:
        render_poly(poly, canvas, camera)