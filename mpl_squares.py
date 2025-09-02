import matplotlib
import matplotlib.pyplot as plt
# plt.style.available
matplotlib.use('TkAgg')
# import tkinter

# ['Solarize_Light2', '_classic_test_patch', '_mpl-gallery']
input_values = [1, 2, 3, 4, 5, 6]
squares = [1, 4, 9, 16, 25, 20]

plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(input_values, squares, linewidth=3)

# Set chart title and label axes.
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# Set size of tick labels.
ax.tick_params(labelsize=14)

plt.show()