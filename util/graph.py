import matplotlib.pyplot as plt


class Graph:
    def __init__(self):
        ax = plt.gca()
        ax.grid()
        # TODO: Use plt.x/ylim() somehow instead?
        self.xmin = None
        self.xmax = None
        self.ymin = None
        self.ymax = None

    def add_vector(self, v, start=None, color='black'):
        """color is from:
        https://matplotlib.org/3.1.0/gallery/color/named_colors.html
        """
        ax = plt.gca()
        self.fix_bounds([v])
        if start is None:
            start = [0, 0]
        return ax.quiver(*start, *v, angles='xy', scale_units='xy', scale=1, color=color)

    def add_shape(self, m, color='black'):
        """Expects a matrix whose columns are consecutive points of a polygon"""
        ax = plt.gca()
        points = m.T.tolist()
        self.fix_bounds(points)
        # https://stackoverflow.com/a/30252932
        ax.plot(*zip(*(points + points[:1])), marker='o', color=color)

    @staticmethod
    def show():
        plt.show()

    def fix_bounds(self, vs):
        """Center and zoom the graph around the points"""
        ax = plt.gca()
        for v in vs:
            if self.xmin is not None:
                self.xmin = v[0] < self.xmin and v[0] or self.xmin
            else:
                self.xmin = v[0]
            if self.xmax is not None:
                self.xmax = v[0] > self.xmax and v[0] or self.xmax
            else:
                self.xmax = v[0]
            if self.ymin is not None:
                self.ymin = v[1] < self.ymin and v[1] or self.ymin
            else:
                self.ymin = v[1]
            if self.ymax is not None:
                self.ymax = v[1] > self.ymax and v[1] or self.ymax
            else:
                self.ymax = v[1]
            ax.set_xlim([self.xmin - 1, self.xmax + 1])
            ax.set_ylim([self.ymin - 1, self.ymax + 1])
