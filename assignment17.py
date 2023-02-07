# POCS HW 17
# Due 2/10/23

# imports
import matplotlib.pyplot as plt
import numpy as np




# Basic methodology: function which takes in n
# Use n to determine the bounds of the hexagon (n on each side)
# --> maybe find the center and work back from there?
# --> find the vertices of the hexagon
# working up from the bottom, determine algorithm for number of points in each row
# space that number of points evenly (np.linspace?)
# to build the adjacency list, use networkx! 
# assign coordinates to each node/point 
# build the adjacency list
# --> neighbor = any node within distance 1 of the given node (this might be tricky)
# --> for now/to get the required output, assume connection b/w all neighbors








### FUNCTIONIZE AT THE END ####

n = 8



# Function starts here

radius = n-1
half_radius = radius/2

# assume the center is the origin (0,0)

# start with finding vertices (start at lower left and go counter-clockwise)
v1 = {'x': -1 * half_radius, 
      'y': -1 * radius}
v2 = {'x': half_radius, 
      'y': -1 * radius}
v3 = {'x': radius, 
      'y': 0}
v4 = {'x': half_radius, 
      'y': radius}
v5 = {'x': -1 * half_radius, 
      'y': radius}
v6 = {'x': -1 * radius, 
      'y': 0}

# put in a list to help with graphing
vertices = [v1, v2, v3, v4, v5, v6]


start_x = v1['x']
start_y = v1['y']
end_x = v2['x']
end_y = v2['y']

# build dictionary to hold non-vertex points
# key = tuple of (x,y) coordinates of the point
# value = useful info like adjacency list (empty list for now)

points = dict()


# starting with the bottom half of the hexagon
x = start_x
y = start_y


while y != 0:
    x = start_x
    key = str(x) + ',' + str(y)
    points[key] = []
    
    while x != end_x:
        x += 1
        key = str(x) + ',' + str(y)
        points[key] = []
        
    y += 1
    start_x -= 0.5
    end_x += 0.5


# repeat for the top half
start_x = v5['x']
start_y = v5['y']
end_x = v4['x']
end_y = v4['y']

x = start_x
y = start_y

while y != 0:
    x = start_x
    key = str(x) + ',' + str(y)
    points[key] = []
    
    while x != end_x:
        x += 1
        key = str(x) + ',' + str(y)
        points[key] = []
        
    y -= 1
    start_x -= 0.5
    end_x += 0.5



# do the middle row
start_x = v6['x']
start_y = v6['y']
end_x = v3['x']
end_y = v3['y']

x = start_x
y = start_y

key = str(x) + ',' + str(y)
points[key] = []

while x != end_x:
    x += 1
    key = str(x) + ',' + str(y)
    points[key] = []
    
start_x -= 0.5
end_x += 0.5










# finally, plot

# start with vertices
for v in vertices:   
    plt.scatter(v['x'], v['y'], color = 'blue')
    
# now plot the contents of the points dict
x = []
y = []
for point in list(points.keys()):
    values = point.split(',')
    plt.scatter(float(values[0]), float(values[1]), color = 'red')
    
    
    
    
    
    
    
    
plt.show()








