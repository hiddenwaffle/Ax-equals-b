import numpy as np

# strawberry $2
# vanilla $1
# chocolate $3
prices = np.array([2, 1, 3])

sales = np.array([
    # M   T   W  Th   F
    [12, 15, 10, 16, 12],   # S
    [5, 9, 14, 7, 10],      # V
    [8, 12, 10, 9, 15]      # C
])

totals_by_day = prices @ sales
print(totals_by_day)
