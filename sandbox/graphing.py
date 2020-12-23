import numpy as np
import matplotlib.pyplot as plt

# https://stackoverflow.com/a/30252932
points = np.array([
    [1, 1, 1.5, 1.5, 2, 2],
    [2, 4, 4, 2.5, 2.5, 2]
]).T.tolist()
plt.plot(*zip(*(points + points[:1])), marker='o', color='tab:green')
plt.show()

# rectangle = np.array([
#     [0, 0],
#     [0, 1],
#     [1, 1],
#     [1, 0]
# ]).T.tolist()
#
# for points in [rectangle]:
#     plt.plot(*zip(*(points+points[:1])), marker='o', color='tab:green')
#
#     automin, automax = plt.xlim()
#     plt.xlim(automin-0.5, automax+0.5)
#     automin, automax = plt.ylim()
#     plt.ylim(automin-0.5, automax+0.5)
#
#     plt.show()
