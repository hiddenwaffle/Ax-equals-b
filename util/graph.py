import matplotlib.pyplot as plt


class Graph:
    def __init__(self):
        ax = plt.gca()
        ax.grid()
        self.xmin = 0
        self.xmax = 0
        self.ymin = 0
        self.ymax = 0

    def append(self, v):
        ax = plt.gca()
        self.xmin = v[0] < self.xmin and v[0] or self.xmin
        self.xmax = v[0] > self.xmax and v[0] or self.xmax
        self.ymin = v[1] < self.ymin and v[1] or self.ymin
        self.ymax = v[1] > self.ymax and v[1] or self.ymax
        ax.set_xlim([self.xmin - 1, self.xmax + 1])
        ax.set_ylim([self.ymin - 1, self.ymax + 1])
        return ax.quiver(0, 0, *v, angles='xy', scale_units='xy', scale=1)

    @staticmethod
    def show():
        plt.show()
