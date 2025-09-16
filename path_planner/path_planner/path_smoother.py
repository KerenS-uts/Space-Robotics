#!/usr/bin/env python3

import copy

from geometry_msgs.msg import Point

from .graph import is_occluded

class PathSmoother():
    def __init__(self, parent_node, graph, alpha, beta):
        self.parent_node_ = parent_node
        self.graph_ = graph
        
        self.alpha_ = alpha
        self.beta_ = beta

        self.path_smooth_ = []

    def smooth_path(self, path_nodes):
        """Smooth the path to remove sharp corners resulting from the grid-based planning"""

        self.parent_node_.get_logger().info('Smoothing path...')

        # Convert into into a geometry_msgs.Point[]
        path = []

        for node in path_nodes:
            p = Point()
            p.x = float(node.x)
            p.y = float(node.y)
            path.append(p)

        # Initialise the smooth path
        path_smooth = copy.deepcopy(path)

        # Loop until the smoothing converges
        # In each iteration, update every waypoint except the first and last waypoint

        ####################
        ## YOUR CODE HERE ##
        ## Task 5         ##
        ####################
        
        alpha = self.alpha_
        beta = self.beta_

        epsilon = 0.001  # Convergence threshold
        change = epsilon + 1  # Initialise to a value greater than epsilon to enter the loop

        while change > epsilon:
            change = 0.0
            # Update all waypoints except the first and last
            for i in range(1, len(path) - 1):
                prev_x = path_smooth[i].x
                prev_y = path_smooth[i].y

                # Apply smoothing formula
                new_x = path_smooth[i].x - (alpha + 2 * beta) * path_smooth[i].x + alpha * path[i].x + beta * path_smooth[i - 1].x + beta * path_smooth[i + 1].x
                new_y = path_smooth[i].y - (alpha + 2 * beta) * path_smooth[i].y + alpha * path[i].y + beta * path_smooth[i - 1].y + beta * path_smooth[i + 1].y
                #Check if new point is occluded
                blocked_prev = is_occluded(self.graph_.map_.obstacle_map_, [path_smooth[i-1].x, path_smooth[i-1].y], [new_x, new_y])
                blocked_next = is_occluded(self.graph_.map_.obstacle_map_, [new_x, new_y], [path_smooth[i+1].x, path_smooth[i+1].y])
            
                # Update smooth path if not occluded
                path_smooth[i].x = new_x
                path_smooth[i].y = new_y

                # Calculate change
                change += (new_x - prev_x) ** 2 + (new_y - prev_y) ** 2


        ####################

        self.path_smooth_ = path_smooth