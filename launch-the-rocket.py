import math
import time
import sys

#function to calculate the rocket launch
def rocket_launch():
    #get input from user
    print("Enter the launch time in seconds: ")
    launch_time = float(input())
    print("Enter the launch angle in degrees: ")
    launch_angle = float(input())
    print("Enter the launch velocity in meters per second: ")
    launch_velocity = float(input())
    print("Enter the mass of the rocket in kilograms: ")
    rocket_mass = float(input())
    print("Enter the mass of the fuel in kilograms: ")
    fuel_mass = float(input())
    print("Enter the fuel burn rate in kilograms per second: ")
    fuel_burn_rate = float(input())
    print("Enter the gravitational acceleration in meters per second squared: ")
    gravitational_acceleration = float(input())
    print("Enter the drag coefficient: ")
    drag_coefficient = float(input())
    print("Enter the cross-sectional area of the rocket in square meters: ")
    cross_sectional_area = float(input())
    print("Enter the density of the air in kilograms per cubic meter: ")
    air_density = float(input())
    print("Enter the time step in seconds: ")
    time_step = float(input())

    #convert launch angle to radians
    launch_angle = math.radians(launch_angle)

    #calculate the initial x and y components of the velocity
    x_velocity = math.cos(launch_angle) * launch_velocity
    y_velocity = math.sin(launch_angle) * launch_velocity

    #calculate the initial x and y components of the position
    x_position = 0
    y_position = 0

    #calculate the initial mass of the rocket
    rocket_mass = rocket_mass + fuel_mass

    #initialize the time
    time = 0

    #calculate the initial drag force
    drag_force = 0.5 * drag_coefficient * cross_sectional_area * air_density * (x_velocity ** 2)

    #calculate the initial thrust force
    thrust_force = fuel_burn_rate * gravitational_acceleration

    #calculate the initial acceleration
    x_acceleration = (thrust_force - drag_force) / rocket_mass
    y_acceleration = -gravitational_acceleration

    #print the initial position and velocity
    print("Time: ", time, "Position: ", x_position, y_position, "Velocity: ", x_velocity, y_velocity)

    #loop until the rocket hits the ground
    while y_position >= 0:
        #calculate the new position
        x_position = x_position + x_velocity * time_step
        y_position = y_position + y_velocity * time_step

        #calculate the new velocity
        x_velocity = x_velocity + x_acceleration * time_step
        y_velocity = y_velocity + y_acceleration * time_step


        #calculate the new drag force
        drag_force = 0.5 * drag_coefficient * cross_sectional_area * air_density * (x_velocity ** 2)

        #calculate the new thrust force
        thrust_force = fuel_burn_rate * gravitational_acceleration

        #calculate the new acceleration
        x_acceleration = (thrust_force - drag_force) / rocket_mass
        y_acceleration = -gravitational_acceleration

        #calculate the new time
        time = time + time_step

        #print the new position and velocity
        print("Time: ", time, "Position: ", x_position, y_position, "Velocity: ", x_velocity, y_velocity)

        #check if the rocket has run out of fuel
        if rocket_mass <= rocket_mass - fuel_burn_rate * time_step:
            #calculate the new mass
            rocket_mass = rocket_mass - fuel_burn_rate * time_step

            #calculate the new thrust force
            thrust_force = 0

            #calculate the new acceleration
            x_acceleration = (thrust_force - drag_force) / rocket_mass
            y_acceleration = -gravitational_acceleration

            #print the new position and velocity
            print("Time: ", time, "Position: ", x_position, y_position, "Velocity: ", x_velocity, y_velocity)

    #print the final position and velocity
    print("Time: ", time, "Position: ", x_position, y_position, "Velocity: ", x_velocity, y_velocity)

    #print the final time
    print("The rocket hit the ground at time: ", time)

#call the rocket launch function
rocket_launch()

#end of program

