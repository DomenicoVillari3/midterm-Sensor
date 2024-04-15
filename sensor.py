from threading import Thread
import matplotlib.pyplot as plt
import numpy as np



def main():
    plot()


def plot():
    plt.ion()
    for i in range(50):
        y = np.random.random([10,1])
        plt.plot(y)
        plt.draw()
        plt.pause(0.1)
        plt.clf()


if __name__ == '__main__':
    main()
