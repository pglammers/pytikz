import os
import numpy as np
import pytikz as pt


class HexLip:
    def __init__(self, n, l=2):
        self.n = n
        self.l = l
        self.state = np.zeros((n, n), dtype=np.int8)

    def neighbours(self, x, y):
        assert 0 < x < self.n - 1
        assert 0 < y < self.n - 1
        neighbours_list = [(x - 1, y), (x + 1, y)]
        if (x + y) % 2 == 0:
            neighbours_list.append((x, y + 1))
        else:
            neighbours_list.append((x, y - 1))
        return neighbours_list

    def lower_bound(self, x, y):
        return max([self.state[a, b] for a, b in self.neighbours(x, y)]) - self.l

    def upper_bound(self, x, y):
        return min([self.state[a, b] for a, b in self.neighbours(x, y)]) + self.l

    def update(self, x, y):
        self.state[x, y] = np.random.randint(
            self.lower_bound(x, y), self.upper_bound(x, y) + 1
        )

    def mcmc(self, n):
        for k in range(n):
            if k % 100000 == 0:
                print(f"{k // 100000} * 100k")
            x = np.random.randint(1, self.n - 1)
            y = np.random.randint(1, self.n - 1)
            self.update(x, y)

    def slice(self, n):
        h = HexLip(self.n - 4 * n, self.l)
        h.state = self.state[2 * n : -2 * n, 2 * n : -2 * n]
        return h

    def iterate_vertices(self):
        for x in range(self.n):
            for y in range(self.n):
                yield (x, y)

    def iterate_edges(self):
        for x in range(self.n):
            for y in range(self.n):
                if x < self.n - 1:
                    yield ((x, y), (x + 1, y))
                if (x + y) % 2 == 0 and y < self.n - 1:
                    yield ((x, y), (x, y + 1))

    def draw_node(self, view, x, y):
        s = pt.ShapeStyle()
        s.fill = True
        h = self.state[x, y]
        if h > 0:
            s.fill_color = "blue!40"
        elif h == 0:
            s.fill_color = "white"
        else:
            s.fill_color = "red!40"
        view.append(pt.DrawableShape(pt.shape.Circle(pt.Vector(x, y), 0.3), s))
        view.append(pt.Node(pt.Vector(x, y), self.state[x, y]))

    def draw_edge(self, view, x, y, a, b):
        s = pt.ShapeStyle()
        view.append(
            pt.DrawableShape(pt.shape.Path([pt.Vector(x, y), pt.Vector(a, b)]), s)
        )


np.random.seed(1)


n = 12
sim = HexLip(n)
sim.mcmc(10 ** 6)


view = pt.View(lambda x: 1 * x)

for u, v in sim.iterate_edges():
    x, y = u
    a, b = v
    sim.draw_edge(view, x, y, a, b)

for x, y in sim.iterate_vertices():
    sim.draw_node(view, x, y)


fig = pt.LatexFigure("figure", os.path.dirname(__file__))
for o in view:
    fig.draw(o)


fig.build()
