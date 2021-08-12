#!/usr/bin/env python3
"""
Module Docstring
"""
import random
import math
import matplotlib.pyplot as plt

G = 1.0

class Point:
    def __init__(self, initial_pos, initial_vel, mass):
        self.pos = initial_pos
        self.vel = initial_vel
        self.acc = [0, 0, 0]
        self.mass = mass

    def _getAcceleration(self, other_points):
        acc = [0, 0, 0]

        for point in other_points:
            r = [other_pos - cur_pos for cur_pos, other_pos in zip(self.pos, point.pos)]
            r_mag = math.sqrt(r[0]**2 + r[1]**2 + r[2]**2)
            r3 = r_mag**3

            acc[0] += (point.mass * r[0]) / r3
            acc[1] += (point.mass * r[1]) / r3
            acc[2] += (point.mass * r[2]) / r3
        
        acc = [G * ai for ai in acc]

        return acc

    def integrateVelocty(self, other_points, dt):
        acc = self._getAcceleration(other_points)
        self.vel[0] += acc[0] * dt / 2.0
        self.vel[1] += acc[1] * dt / 2.0
        self.vel[2] += acc[2] * dt / 2.0

    def integratePosition(self, dt):
        self.pos[0] += self.vel[0] * dt
        self.pos[1] += self.vel[1] * dt
        self.pos[2] += self.vel[2] * dt


def getSpawnPoints(sample_size):
    x = []
    y = []

    for i in range(0, sample_size):
        rand_x = random.uniform(-1.0,1.0)
        rand_y = random.uniform(-1.0,1.0)

        if ((rand_x**2 + rand_y**2) <= 1.0):
            x.append(rand_x)
            y.append(rand_y)
    
    return x, y

def update_graph(num):
    graph._offsets3d = (data.x, data.y, data.z)
    title.set_text('3D Test, time={}'.format(num))

def main():
    sample_size = 100
    t = 0
    tMax = 100
    dt  = 0.1

    points = getSpawnPoints()

    # Setup matplotlib
    
    for i in range(int(tMax / dt)):

        for point in points:
            points_filtered = points[:]
            points_filtered.remove(point)

            point.integrateVelocity(points_filtered, dt)
            point.integtatePosition(dt)
        
        #  Update plot?

        t += dt


if __name__ == "__main__":
    main()