import matplotlib.pyplot as plt


class Graph:
    def __init__(self):
        ax = plt.gca()
        ax.grid()
        self.xmin = 0
        self.xmax = 0
        self.ymin = 0
        self.ymax = 0

    def append(self, v, start=None, color='black'):
        """color is from:
        https://matplotlib.org/3.1.0/gallery/color/named_colors.html
        """
        ax = plt.gca()
        self.xmin = v[0] < self.xmin and v[0] or self.xmin
        self.xmax = v[0] > self.xmax and v[0] or self.xmax
        self.ymin = v[1] < self.ymin and v[1] or self.ymin
        self.ymax = v[1] > self.ymax and v[1] or self.ymax
        ax.set_xlim([self.xmin - 1, self.xmax + 1])
        ax.set_ylim([self.ymin - 1, self.ymax + 1])
        if start is None:
            start = [0, 0]
        return ax.quiver(*start, *v, angles='xy', scale_units='xy', scale=1, color=color)

    @staticmethod
    def show():
        plt.show()
