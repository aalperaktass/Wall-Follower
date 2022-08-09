"""wallfollower_controller controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot

def run_robot(robot):

    timestep = int(robot.getBasicTimeStep())
    max_speed = 6.28
 
    left_motor = robot.getMotor('left wheel robot')
    right_motor = robot.getMotor('right wheel robot')
    
    left_motor.setPosition(float('inf'))
    left_motor.setVelocity(0.0)
    
    right_motor.setPosition(float('inf'))
    right_motor.setVelocity(0.0)
    
    prox_sensors = []
    for ind in range(8):
        sensor_name = 'ps' + str(ind)
        prox_sensors.append(robots.getDistanceSensor(sensor_name))
        prox_sensors(ind).enable(timestep)
         
    while robot.step(timestep) != -1:
             
         left_wall = prox_sensors{5}.geValue() > 80
         left_corner = prox_sensors{6}.geValue() > 80
         front_wall = prox_sensors{7}.geValue() > 80
         
         left_speed = max_speed
         right_speed = max_speed
                   
         if front_wall:
             print("Turn right in place")
             left_speed = max_speed
             right_speed = -max_speed
         
         else:
             
             if left_wall:
                 print("Drive forward")            
                 left_speed = max_speed  
                 right_speed = max_speed
             
             else:
                 print("Turn left")
                 left_speed = max_speed / 8 
                 right_speed = max_speed
             
             if left_corner:
                 print("Came to close, drive right")
                 left_speed = max_speed 
                 right_speed = max_speed /8
        
         left_motor.setVelocity(left_speed)
         right_motor.setVelocity(right_speed)                     
              
       
  
if __name__ == "__main__":
    
    my_robot = Robot()
    run_robot(my_robot)