import math
import time
import sys
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def orbital_values():
    print("Enter the orbital period in seconds: ")
    orbital_period = float(input())
    print("Enter the orbital radius in meters: ")
    orbital_radius = float(input())
    print("Enter the gravitational acceleration in meters per second squared: ")
    gravitational_acceleration = float(input())
    print("Enter the time step in seconds: ")
    time_step = float(input())

    #calculate the orbital velocity
    orbital_velocity = (gravitational_acceleration * orbital_period)/(2 * math.pi)

    #calculate the orbital acceleration
    orbital_acceleration = (gravitational_acceleration * orbital_radius)/(orbital_period ** 2)

    #calculate the orbital force
    orbital_force = (gravitational_acceleration * orbital_radius ** 3)/(orbital_period ** 2)

    #calculate the orbital energy
    orbital_energy = (gravitational_acceleration * orbital_radius ** 2)/(orbital_period ** 2)

    #print the orbital values
    print("Orbital Velocity: ", orbital_velocity)
    print("Orbital Acceleration: ", orbital_acceleration)
    print("Orbital Force: ", orbital_force)
    print("Orbital Energy: ", orbital_energy)

    #calculate the orbital position
    #set the x, y and z axis
    x = []
    y = []
    z = []

    #calculate the orbital position
    for i in range(0, 100):
        x.append(orbital_radius * math.cos(i))
        y.append(orbital_radius * math.sin(i))
        z.append(0)

    #3d graph
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot(x, y, z, label='orbital position')
    ax.set_xlabel('X axis')
    ax.set_ylabel('Y axis')
    ax.set_zlabel('Z axis')
    plt.show()

orbital_values()




