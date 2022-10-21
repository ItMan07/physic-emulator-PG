# import random
# from itertools import count
# import matplotlib.pyplot as plt
# from matplotlib.animation import FuncAnimation
#
# x_vals = []
# y_vals = []
#
# index = count()
#
#
# def animate(i):
#     x_vals.append(next(index))
#     y_vals.append(random.randint(0, 5))
#
#     plt.plot(x_vals, y_vals)
#
#
# ani = FuncAnimation(plt.gcf(), animate, interval=1000)
#
# plt.tight_layout()
# plt.show()


import numpy as np
import matplotlib.pyplot as plt

plt.axis([0, 10, 0, 1])

for i in range(10):
    y = np.random.random()
    plt.scatter(i, y)
    plt.pause(0.05)

plt.show()



def calculate_plotter():
    pass
    # plt.title("Линейный график зависимости скорости от времени")
    # plt.xlabel("Время")
    # plt.ylabel("Скорость по {х}")
    #
    # for tick in range(0, pygame.time.get_ticks()):
    #     plt.plot(tick, velocity[0])

    # fig = plt.figure()

i = 0
x = list()
y = list()
plt.axis([0, 1000, 0, 1])
while i < 1000:
    temp_y = np.random.random()
    x.append(i)
    y.append(temp_y)
    plt.scatter(i, temp_y)
    i += 1
plt.show()



# calculate_plotter()

            # for tick in range(0, pygame.time.get_ticks()):
            #     plt.plot([tick], [1, 2, 3])
            # plt.title("Линейный график зависимости скорости от времени")
            # plt.xlabel("Время")
            # plt.ylabel("Скорость по {х}")
            # plt.show()