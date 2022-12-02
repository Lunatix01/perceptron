import numpy as np
import matplotlib.pyplot as plt

# add function that adds two (1*2) matrixes


def add(w0, t, x):
    print("add")
    w1 = w0[0] + x[0]
    w2 = w0[1] + x[1]
    t = t+1
    return list([w1, w2])

# add subtract that subtract two (1*2) matrixes


def subtract(w0, t, x):
    print("subtract")
    w1 = w0[0] - x[0]
    w2 = w0[1] - x[1]
    t = t+1
    return list([w1, w2])


# count used for plotting either red point or blue (odd count = blue)
count = 0
# initial weight from -.5 , .5
w0 = np.random.uniform(-.5, .5, 2)
# initializing data which has Class A and B, X's and Labels
data = np.zeros(shape=(1, 3), dtype=object)
# find slope
perpendecular = [w0[1], w0[0]*-1]
slope = perpendecular[1]/perpendecular[0]
# create 100 random points to plot with slope
x = np.linspace(-20.1, 20.1, 100)
b = 0
# y = mx + b
y = slope*x+b
# plot the line
ln, = plt.plot(x, y, 'k-')

# plot the points and seperate them by with a line
for t in range(0, 30):
    # generate a random value in either class A or B
    if (count % 2 == 0):
        x1 = np.random.randint(0.1, 20)
        y1 = np.random.randint(-40.1, 0.1)
        red = np.array([x1, y1, 'red'], dtype=object)
        data = np.vstack((data, red))
        plt.plot([x1], [y1], 'ro')
        plt.pause(0.5)
        count = count+1
    else:
        x2 = np.random.randint(-20, 0.1)
        y2 = np.random.randint(0.1, 40.1)
        blue = np.array([int(x2), int(y2), 'blue'], dtype=object)
        data = np.vstack((data, blue))
        plt.plot([x2], [y2], 'bo')
        plt.pause(0.5)
        count = count+1
    # the algorithm conditions
    x = data[len(data)-1]
    if (x[2] == "red" and np.dot(w0, [x[0], x[1]]) > 0):
        print("skip1")
        continue
    if (x[2] == "red" and np.dot(w0, [x[0], x[1]]) <= 0):
        # get new weight and find slope with [0,0] and new weight to plot
        w0 = add(w0, t, [x[0], x[1]])
        ln.remove()
        # find slope
        perpendecular = [w0[1], w0[0]*-1]
        slope = perpendecular[1]/perpendecular[0]
        x = np.linspace(-20.1, 20.1, 100)
        b = 0
        y = slope*x+b
        # plot the line
        ln, = plt.plot(x, y, 'k-')
        # pause to see the line
        plt.pause(0.5)
    if (x[2] == "blue" and np.dot(w0, [x[0], x[1]]) < 0):
        print("skip2")
        continue
    if (x[2] == "blue" and np.dot(w0, [x[0], x[1]]) >= 0):
        # get new weight and find slope with [0,0] and new weight to plot
        w0 = subtract(w0, t, [x[0], x[1]])
        # remove older line
        ln.remove()
        # find slope
        perpendecular = [w0[1], w0[0]*-1]
        slope = perpendecular[1]/perpendecular[0]
        x = np.linspace(-20.1, 20.1, 100)
        b = 0
        y = slope*x+b
        # plot the line
        ln, = plt.plot(x, y, 'k-')
        # pause to see the line
        plt.pause(0.5)
# title and show the plot
plt.title('Perceptron')
plt.show()
