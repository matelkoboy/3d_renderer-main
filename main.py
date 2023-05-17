import tkinter as tk
from objectsss.cube import Brick
from objectsss.tetrahedron import Tetrahedron
from objectsss.plane import Plane
from objectsss.objectcomponents.point import Point
from objectsss.triangle import Triangle
from visual.camera import Cam
import controls, time
from visual.renderer import add_to_renderer, render_all

width = 1000
height = 1000

root = tk.Tk()
root.geometry(f"{width}x{height}")
canvas = tk.Canvas(root, width=width, height=height)
camera = Cam(width, height, 45)
light = Point(-1, -1, -1)
cube1 = Brick(Point(-200, 100, 200), 
              Point(-100, 0, -200),
              light)
tetrahedron = Tetrahedron(Point(0, 0, 0), 
                          Point(-100, 50, 50), 
                          Point(-70, -10, -50), 
                          Point(-50, 100, 0), 
                          light)
ground = Plane(Point(-200, -50, -200), 
               Point(200, -50, -200), 
               Point(200, -50, 200))

pseudo_map = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 1, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 1, 1, 1, 0, 0],
    [0, 0, 1, 2, 3, 2, 1, 1, 0, 0],
    [0, 0, 1, 3, 4, 3, 3, 2, 1, 0],
    [0, 1, 2, 3, 4, 3, 4, 3, 1, 0],
    [0, 1, 2, 2, 3, 2, 3, 1, 0, 0],
    [0, 0, 1, 1, 2, 2, 2, 1, 0, 0],
    [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]

m = 20
h = 20

for i in range(9):
    for j in range(9):
        p1 = Point(i * m, pseudo_map[i][j] * h, j * m)
        p2 = Point((i + 1) * m, pseudo_map[i + 1][j] * h, j * m)
        p3 = Point(i * m, pseudo_map[i][j + 1] * h, (j + 1) * m)
        
        #add_to_renderer(Triangle(p1, p2, p3, light))
        
        ap1 = Point((i + 1) * m, pseudo_map[i + 1][j + 1] * h, (j + 1) * m)
        ap2 = Point((i + 1) * m, pseudo_map[i + 1][j] * h, j * m)
        ap3 = Point(i * m, pseudo_map[i][j + 1] * h, (j + 1) * m)
        
        #add_to_renderer(Triangle(ap1, ap2, ap3, light))
        

add_to_renderer(cube1)
#add_to_renderer(tetrahedron)
#add_to_renderer(ground)

def update():
    camera.move(controls.x_speed, controls.y_speed, controls.z_speed)
    
    if (controls.v_rot_speed > 0 and camera.v_rot < 80) or (controls.v_rot_speed < 0 and camera.v_rot > -80):
        camera.v_rot += controls.v_rot_speed
    camera.h_rot += controls.h_rot_speed
    
    camera.update_plane()
    
    
    canvas.delete("all")
    render_all(canvas, camera)
    
    
delta_time = 10
def press(event):
    controls.press(event, camera, delta_time)

def release(event):
    controls.release(event)
    
overall_time = time.time()
end_time = time.time()
c = 1
total_fps = 0

while True:
    start_time = time.time()
    
    
    update()
    
    #FPS
    
    try:
        end_time = time.time() - start_time
        t = 60 / end_time
        total_fps += t
        c += 1
        delta_time = c / total_fps
    except:
        t = "ERROR"
    
    if time.time() - overall_time > 1:
        overall_time = time.time()
        print(total_fps / c)
    #====
    
    
    root.bind("<KeyPress>", press)
    root.bind("<KeyRelease>", release)
    root.update()