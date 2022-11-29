import numpy as np
import matplotlib.pyplot as plt


def add(slope, t, x):
    slope = slope + x
    t = t+1
    print("slope: ", slope)
    print("t: ", t)
    return slope


def subtract(slope, t, x):
    slope = slope - x
    t = t+1
    print("slope: ", slope)
    print("t: ", t)
    return slope


line = np.linspace(-5, 5, 100)
slope = np.random.uniform(-5, 5)
y = slope*line+0
ln, = plt.plot(line, y, 'k-')
count = 0
for t in range(0, 10):
    x = np.random.uniform(-1, 1)
    x1 = np.random.randint(1, 5)
    x2 = np.random.randint(-5, 0)
    y1 = np.random.randint(0, 5)
    y2 = np.random.randint(0, 5)
    if (count % 2 == 0):
        plt.plot([x1], [y1], 'ro')
        plt.pause(0.5)
        count = count+1
    else:
        plt.plot([x2], [y2], 'bo')
        plt.pause(0.5)
        count = count+1

    if (x > 0 and slope*x > 0):
        continue
    if (x < 0 and slope*x <= 0):
        slope = add(slope, t, x)
        y = slope*line+1
        ln.remove()
        ln, = plt.plot(line, y, 'k-')
        plt.pause(0.5)
    if (x < 0 and slope*x < 0):
        continue
    if (x < 0 and slope*x >= 0):
        slope = subtract(slope, t, x)
        y = slope*line+1
        ln.remove()
        ln, = plt.plot(line, y, 'k-')
        plt.pause(0.5)


plt.title('Perceptron')
plt.show()
