"""my_controller2 controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot
import time
# create the Robot instance.
robot = Robot()

# get the time step of the current world.
timestep = int(robot.getBasicTimeStep())


# Initialize motors
left_motor = robot.getDevice("left wheel motor")
right_motor = robot.getDevice("right wheel motor")

# Set the motors to rotate indefinitely
left_motor.setPosition(float('inf'))
right_motor.setPosition(float('inf'))

# Set initial speed for the motors
left_motor.setVelocity(0.0)
right_motor.setVelocity(0.0)

# Set max speed
MAX_SPEED = 6.28


# Initialize proximity sensors
proximity_sensors = []
sensor_names = [
    "ps0", "ps1", "ps2", "ps3", 
    "ps4", "ps5", "ps6", "ps7"
]

for name in sensor_names:
    sensor = robot.getDevice(name)
    sensor.enable(timestep)
    proximity_sensors.append(sensor)
    
    
# Main loop:
# - perform simulation steps until Webots is stopping the controller
while robot.step(timestep) != -1:

    left_speed = MAX_SPEED
    right_speed = MAX_SPEED
    
    for ps in proximity_sensors:
        ps_val = ps.getValue()
        print(ps_val)
        if ps_val > 80:
            left_speed = -MAX_SPEED
            
    left_motor.setVelocity(left_speed)
    right_motor.setVelocity(right_speed) 
    


    

# Enter here exit cleanup code.
