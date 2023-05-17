speed = 20000
rot_speed = 5000

global x_speed, y_speed, z_speed, v_rot_speed, h_rot_speed

x_speed = 0
y_speed = 0
z_speed = 0
h_rot_speed = 0
v_rot_speed = 0

def press(event, camera, delta_time):
    global x_speed, y_speed, z_speed, v_rot_speed, h_rot_speed
    
    if event.keysym == "w":
        z_speed = speed * delta_time
    elif event.keysym == "s":
        z_speed = -speed * delta_time
    elif event.keysym == "a":
        x_speed = -speed * delta_time
    elif event.keysym == "d":
        x_speed = speed * delta_time
    elif event.keysym == "Shift_L":
        y_speed = -speed * delta_time
    elif event.keysym == "space":
        y_speed = speed * delta_time
    elif event.keysym == "Up" and camera.v_rot < 80:
        v_rot_speed = rot_speed * delta_time
    elif event.keysym == "Down" and camera.v_rot > -80:
        v_rot_speed = -rot_speed * delta_time
    elif event.keysym == "Left":
        h_rot_speed = rot_speed * delta_time
    elif event.keysym == "Right":
        h_rot_speed = -rot_speed * delta_time
    
        
def release(event):
    global x_speed, y_speed, z_speed, v_rot_speed, h_rot_speed

    if event.keysym == "w":
        z_speed = 0
    elif event.keysym == "s":
        z_speed = 0
    elif event.keysym == "a":
        x_speed = 0
    elif event.keysym == "d":
        x_speed = 0
    elif event.keysym == "Shift_L":
        y_speed = 0
    elif event.keysym == "space":
        y_speed = 0
    elif event.keysym == "Up":
        v_rot_speed = 0
    elif event.keysym == "Down":
        v_rot_speed = 0
    elif event.keysym == "Left":
        h_rot_speed = 0
    elif event.keysym == "Right":
        h_rot_speed = 0