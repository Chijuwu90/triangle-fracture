import numpy as np
import random
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib.animation as animation


class Triangle:
    """ Triangle is defined as 3 points in 2D space where A is at origin (0,0),
    B is on the X-axis (10, 0)
    and C is a  random location on the horizontal line between (0, 10) and (10, 10)
    """

    def __init__(self, n_iter=100, size=10):

        # random starting point between (0,0) and (10,10)
        self.start_location = (random.random()*size, random.random()*size)
        self.current_location = self.start_location
        self.A = (0, 0)
        self.B = (size, 0)
        self.C = (random.random()*size, size)
        self.n_iter = n_iter
        self.size = size

        self.x, self.y = [], []
        self.sc = None

    def run(self):

        plt.style.use('dark_background')

        fig = plt.figure()
        ax = plt.axes(xlim=(0, self.size), ylim=(0, self.size))
        # lists to store x and y axis points
        self.sc = ax.scatter(self.x, self.y)

        # setting a title for the plot
        plt.title('Creating a triangle fracture plot.')
        # hiding the axis details
        plt.axis('off')

        # call the animator
        anim = animation.FuncAnimation(fig, self.animate, frames=self.n_iter, interval=100, repeat=True)

        # save the animation as mp4 video file
        anim.save('triangle.gif', writer='imagemagick')

    def animate(self, i):
        dice_number = self.roll_dice()

        if (dice_number == 1) | (dice_number == 2):
            target = self.A
        elif (dice_number == 3) | (dice_number == 4):
            target = self.B
        else:
            target = self.C

        # calculate the middle point and replace as new current location
        middle_point = ((self.current_location[0] + target[0])/2, (self.current_location[1] + target[1])/2)
        self.current_location = middle_point

        # x, y values to be plotted
        self.x.append(self.current_location[0])
        self.y.append(self.current_location[1])
        self.sc.set_offsets(np.c_[self.x, self.y])

    @staticmethod
    def roll_dice():
        return random.randint(1, 6)


if __name__ == "__main__":
    Triangle(n_iter=400, size=20).run()


