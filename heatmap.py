import matplotlib.pyplot as plt
import numpy as np

# 100 records (1 = Match, 0 = Mismatch)
data = np.ones((10, 10))

# Demo ke liye 2 mismatches
data[2][3] = 0
data[7][8] = 0

plt.imshow(data, cmap="RdYlGn", interpolation="nearest")
plt.title("Redis-MySQL Consistency Heatmap")
plt.colorbar(label="1 = Match, 0 = Mismatch")

plt.savefig("consistency_heatmap.png")
plt.show()