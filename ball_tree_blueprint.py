import numpy as np

from matplotlib import pyplot as plt
from matplotlib.patches import Circle


class BallTree:
    """Simple Ball tree class"""

    # class initialization function
    def __init__(self, data):
        self.data = np.asarray(data)

        # data should be two-dimensional
        assert self.data.shape[1] == 2

        self.loc = data.mean(0)
        self.radius = np.sqrt(np.max(np.sum((self.data - self.loc)**2, 1)))

        self.child1 = None
        self.child2 = None

        if len(self.data) > 1:
            # sort on the dimension with the largest spread
            largest_dim = np.argmax(self.data.max(0) - self.data.min(0))
            i_sort = np.argsort(self.data[:, largest_dim])
            self.data[:] = self.data[i_sort, :]

            # find split point
            N = self.data.shape[0]
            half_N = int(N / 2)
            split_point = 0.5 * (self.data[half_N, largest_dim] + self.data[half_N - 1, largest_dim])

            # recursively create subnodes
            self.child1 = BallTree(self.data[half_N:])
            self.child2 = BallTree(self.data[:half_N])

    def draw_circle(self, ax, depth=None):
        """Recursively plot a visualization of the Ball tree region"""
        if not depth:
            circ = Circle(self.loc, self.radius, ec='k', fc='none')
            ax.add_patch(circ)

        if self.child1:
            if depth is None:
                self.child1.draw_circle(ax)
                self.child2.draw_circle(ax)
            elif depth > 0:
                self.child1.draw_circle(ax, depth - 1)
                self.child2.draw_circle(ax, depth - 1)


# --------------------------------------------
# Create a set of structured random points in two dimensions
np.random.seed(0)
X = np.random.random((100, 2)) * 0.2 - 1
X[:, 1] *= 1.5
# X[:, 1] += X[:, 0] ** 2

# --------------------------------------------
# Use our Ball Tree class to recursively divide the space
BT = BallTree(X)

# --------------------------------------------
# Plot four different levels of the Ball tree
fig = plt.figure(figsize=(12, 12))
fig.subplots_adjust(wspace=0.1, hspace=0.15, left=0.1, right=0.9, bottom=0.05, top=0.9)

for level in range(1, 5):
    ax = fig.add_subplot(2, 2, level, xticks=[], yticks=[])
    ax.scatter(X[:, 0], X[:, 1], s=9)
    BT.draw_circle(ax, depth=level - 1)

    # ax.set_xlim(-1.35, 1.35)
    # ax.set_ylim(-1.0, 1.7)
    # ax.set_title('level %i' % level)

# suptitle() adds a title to the entire figure
fig.suptitle('Ball-tree Example')
plt.show()
