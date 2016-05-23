"""main program for Random Walks."""
import matplotlib.pyplot as plt

from random_walk import RandomWalk

# Keep making new walks, as long as the program is active.
run = True
while run:
    rw = RandomWalk(50000)
    rw.fill_walk()

    # Set the size of the plotting window
    plt.figure(dpi=128, figsize=(10, 6))

    point_numbers = list(range(rw.num_points))
    plt.scatter(
        rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, s=1,
        edgecolor='none',
     )
    # plt.plot(rw.x_values, rw.y_values, linewidth=5)

    # Emphasize the first and last points.
    plt.scatter(0, 0, c='green', edgecolors='none', s=100)
    plt.scatter(
        rw.x_values[-1], rw.y_values[-1], c='red', edgecolor='none', s=100
    )

    # Remove the axes.
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)

    plt.show()

    while True:
        keep_running = input("Make another walk? (y/n): ")
        if keep_running == 'n':
            run = False
            break
        elif keep_running == 'y':
            break
        else:
            print("Please input yes or no")
