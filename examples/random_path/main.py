import os
import numpy as np
import sys
sys.path.insert(1, '/Users/piet/Git/pytikz')
from pytikz.latex_figure import LatexFigure
from pytikz.path import *
from pprint import pprint


def real_coords(v):
    rx = (1, 0)
    angle = 2 * np.pi / 3
    ry = (np.cos(angle), np.sin(angle))

    x = rx[0] * v[0] + ry[0] * v[1]
    y = rx[1] * v[0] + ry[1] * v[1]
    return x, y

class DimerHeights:
    def __init__(self, n):
        self.n = n
        self.heights = np.zeros((n, n), dtype=int)
        for i in range(n):
            for j in range(n):
                self.heights[i, j] = i+j
        self.rx = (1, 0)
        self.angle = 2 * np.pi / 3
        self.ry = (np.sin(self.angle), np.cos(self.angle))
        self.string = ''
        # print(self.heights)

    def neighbours_plus(self, x, y):
        vertex_list = []
        if x+1 < self.n:
            vertex_list.append((x+1, y))
        if y+1 < self.n:
            vertex_list.append((x, y+1))
        if x-1 >= 0 and y-1 >= 0:
            vertex_list.append((x-1, y-1))
        return vertex_list

    def neighbours_minus(self, x, y):
        vertex_list = []
        if x-1 >= 0:
            vertex_list.append((x-1, y))
        if y-1 >= 0:
            vertex_list.append((x, y-1))
        if x+1 < self.n and y+1 < self.n:
            vertex_list.append((x+1, y+1))
        return vertex_list

    def maximum(self, vertex_list):
        return max([self.heights[vertex] for vertex in vertex_list])

    def minimum(self, vertex_list):
        return min([self.heights[vertex] for vertex in vertex_list])

    def possible_values(self, x, y):
        plus_max = self.maximum(self.neighbours_plus(x, y))
        minus_min = self.minimum(self.neighbours_minus(x, y))
        if plus_max < minus_min:
            return [plus_max - 1, minus_min + 1]
        else:
            return [self.heights[x, y]]

    def resample_vertex(self, x, y):
        possible_values = self.possible_values(x, y)
        options = len(possible_values)
        if options > 1:
            new_value = possible_values[np.random.randint(options)]
            self.heights[x, y] = new_value

    def resample(self, n):
        for k in range(n):
            x = np.random.randint(self.n)
            y = np.random.randint(self.n)
            self.resample_vertex(x, y)
        assert self.is_Lipschitz()

    def is_Lipschitz(self):
        for i in range(self.n):
            for j in range(self.n):
                vertex_a = (i, j)
                for vertex_b in self.neighbours_plus(i, j):
                    diff = self.heights[vertex_b]-self.heights[vertex_a]
                    if diff not in [-2, 1]:
                        return False
        return True

    def real_pos(self, x, y):
        return x * self.rx[0] + y * self.ry[0], x * self.rx[1] + y * self.ry[1]

    def tiling(self, target=-2):
        edge_list = []
        for i in range(self.n):
            for j in range(self.n):
                vertex_a = (i, j)
                for vertex_b in self.neighbours_plus(i, j):
                    diff = self.heights[vertex_b]-self.heights[vertex_a]
                    if diff == target:
                        edge_list.append([vertex_a, vertex_b])
        return edge_list

    def tiling_real(self, target=-2):
        edge_list = self.tiling(target=target)
        list_new = []
        for edge in edge_list:
            newedge = []
            for vertex in edge:
                newedge.append(real_coords(vertex))
            list_new.append(newedge)
        return list_new



# a = DimerHeights(8)
# b = DimerHeights(8)
# a.resample(10000)
# b.resample(10000)
# c = DimerHeights(8)
# c.heights = a.heights - b.heights
#
fig = LatexFigure('test', os.path.join(os.getcwd(), 'figures'))
#
# for edge in c.tiling_real(3):
#     path = DrawablePath(edge)
#     fig.draw(path)
# for edge in c.tiling_real(-3):
#     path = DrawablePath(edge)
#     fig.draw(path)

vertices = 10 * np.random.rand(10, 2)

path = DrawablePath(vertices)
path.line_join = 'round'
fig.draw(path)

fig.update(hard=True)
pprint(vertices)
