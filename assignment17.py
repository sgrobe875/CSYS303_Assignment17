# Sarah Grobe
# POCS HW 17
# Due 2/10/23

# imports
import matplotlib.pyplot as plt
import math




# Basic methodology: function which takes in n
# Use n to determine the bounds of the hexagon (n on each side)
# --> maybe find the center and work back from there?
# --> find radius and the vertices of the hexagon
# working up from the bottom, determine algorithm for number of points in each row
# assign coordinates to each node/point 
# build the adjacency list
# --> neighbor = any node within distance close to 1 of the given node (went with dist < 1.2)
# --> for now/to get the required output, assume connection b/w all neighbors


# converts coordinates from string format 'x,y' to float(x) and float(y) 
# as separate variables
def get_float_coords(coord_string):
    coord = coord_string.split(',')
    x = float(coord[0])
    y = float(coord[1])
    return x, y


# calculates Euclidean distance between two coordinates in string format
def calc_distance(coord1_string, coord2_string):
    x1, y1 = get_float_coords(coord1_string)
    x2, y2 = get_float_coords(coord2_string)
    return math.sqrt((x1-x2)**2 + (y1-y2)**2)


# takes in edge width n, draws lattice of the corresponding size and returns the
# adjacency list of all of the nodes within the lattice
def draw_lattice(n): 
    # calculate some parameters based on n
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
    
    
    
    start_x = v1['x']
    start_y = v1['y']
    end_x = v2['x']
    
    # build dictionary to hold non-vertex points
    # key = tuple of (x,y) coordinates of the point
    # value = adjacency list (empty list for now)
    
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
    
    
    
    
    # set neighbors of each point
    for point1 in points:
        # loop through all points
        for point2 in points:
            if point1 != point2:
                # calculate the distance between the two points
                dist = calc_distance(point1, point2)
                # if the two points are close enough, they are neighbors, so add to 
                # the neighbor list for point1
                if dist < 1.2:
                    points[point1].append(point2)
    
    
    
    
    # finally, plot

        
    # plot lines between all neighbors
    for point in list(points.keys()):
        # start by adding points of the current node
        point_x, point_y = get_float_coords(point)
        x = [point_x]
        y = [point_y]
        
        # loop through all neighbors of that node
        neighbors = points[point]
        for neighbor in neighbors:
            x_n, y_n = get_float_coords(neighbor)
            
            # add coordinates of the neighbor, then re-add the points of the
            # original node
            x.append(x_n)
            x.append(point_x)
            y.append(y_n)
            y.append(point_y)
        
        # plot and move on to the next point
        plt.plot(x, y, color = 'black', zorder = 1)
        
    
    # now plot point locations themselves
    for point in list(points.keys()):
        x, y = get_float_coords(point)
        plt.scatter(x, y, color = 'red', zorder = 2)
        
    plt.show()
    
    # return the adjacency list
    return points


# draw the lattice and get the adjacency list
adj_list = draw_lattice(n = 8)

# print the origin as an example
print('Neighbors of (0,0):')
print(adj_list['0,0'])




