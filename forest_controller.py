from controller import Robot
from controller import Keyboard
from controller import DistanceSensor

robot = Robot()
keyboard = Keyboard()

timestep=64

ds1= robot.getDevice("ds1")
ds2=robot.getDevioce("ds2")
ds1.enable(timestep)
ds2.enable(timestep)

wheel1=robot.getDevice("wheel1")
wheel1.setPosition(float('inf'))
wheel1.setVelocity(0.0)

wheel2=robot.getDevice("wheel2")
wheel2.setPosition(float('inf'))
wheel2.setVelocity(0.0)

wheel3=robot.getDevice("wheel3")
wheel3.setPosition(float('inf'))
wheel3.setVelocity(0.0)

wheel4=robot.getDevice("wheel4")
wheel4.setPosition(float('inf'))
wheel4.setVelocity(0.0)

auto_mode= False
prev_key=0
key_pressed=-1
n_turns=0
speed=4
 
keyboard.enable(timestep)

while (robot.step(timestep) !=-1):
    prev_key=key_pressed
   
    key_pressed= keyboard.getKey()
    print(key_pressed)
    
    if(prev_key==-1 and key_pressed== 65):
        auto_mode = not auto_mode
    if(automode):
        ds1_value=ds1.getValue()
        ds2_value=ds2.getValue()
        if(ds1_value<1000 or ds2_value<1000):
            n_turns=8
        if(n_turns>0):
            n_turns-=1
            wheel1_left.setVelocity(-speed)
            wheel1_right.setVelocity(speed)
            wheel2_left.setVelocity(-speed)
            wheel2_right.setVelocity(speed)
        else:                              
            wheel1_left.setVelocity(speed)
            wheel1_right.setVelocity(speed)
            wheel2_left.setVelocity(speed)
            wheel2_right.setVelocity(speed)
    if(not auto_mode):
        # front movement - press up arrow key
        if(key_pressed== 315):
            wheel1.setVelocity(speed)
            wheel2.setVelocity(speed)
            wheel3.setVelocity(speed)
            wheel4.setVelocity(speed)
            
        # back movement - press down arrow key   
        if(key_pressed== 317):
            wheel1.setVelocity(-speed)
            wheel2.setVelocity(-speed)
            wheel3.setVelocity(-speed)
            wheel4.setVelocity(-speed)
        
        # left movement - press left arrow key      
        if(key_pressed== 314):
            wheel1.setVelocity(-speed)
            wheel2.setVelocity(speed)
            wheel3.setVelocity(-speed)
            wheel4.setVelocity(speed)
        
        # right movement - press right arrow key     
        if(key_pressed== 316):
            wheel1.setVelocity(speed)
            wheel2.setVelocity(-speed)
            wheel3.setVelocity(speed)
            wheel4.setVelocity(-speed)
        
        # if no key is pressed   
        if(key_pressed== -1):
            wheel1.setVelocity(0)
            wheel2.setVelocity(0)
            wheel3.setVelocity(0)
            wheel4.setVelocity(0)