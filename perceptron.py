import numpy as np
import matplotlib.pyplot as plt


def add(w0, t, x):
    print("add")
    w1 = w0[0] + x[0]
    w2 = w0[1] + x[1]
    t = t+1
    print("w1: ", w1)
    print("w2: ", w2)
    return list([w1, w2])


def subtract(w0, t, x):
    print("subtract")
    w1 = w0[0] - x[0]
    w2 = w0[1] - x[1]
    t = t+1
    print("w1: ", w1)
    print("w2: ", w2)
    return list([w1, w2])


count = 0
w0 = np.random.uniform(-.5, .5, 2)
print("inital w: ", w0)
data = np.zeros(shape=(1, 3), dtype=object)
perpendecular = [w0[1], w0[0]*-1]
slope = perpendecular[1]/perpendecular[0]
x = np.linspace(-20.1, 20.1, 100)
b = 0
y = slope*x+b
ln, = plt.plot(x, y, 'k-')

for t in range(0, 100):
    if (count % 2 == 0):
        x1 = np.random.randint(0.1, 20)
        y1 = np.random.randint(-10.1, 0.1)
        red = np.array([x1, y1, 'red'], dtype=object)
        data = np.vstack((data, red))
        plt.plot([x1], [y1], 'ro')
        plt.pause(0.5)
        count = count+1
    else:
        x2 = np.random.randint(-20, 0.1)
        y2 = np.random.randint(0.1, 10.1)
        blue = np.array([int(x2), int(y2), 'blue'], dtype=object)
        data = np.vstack((data, blue))
        plt.plot([x2], [y2], 'bo')
        plt.pause(0.5)
        count = count+1
    x = data[len(data)-1]
    if (x[2] == "red" and np.dot(w0, [x[0], x[1]]) > 0):
        print("skip1")
        continue
    if (x[2] == "red" and np.dot(w0, [x[0], x[1]]) <= 0):
        print("add")
        w0 = add(w0, t, [x[0], x[1]])
        ln.remove()
        line = np.linspace(w0[1], 0, 100)
        line2 = np.linspace(w0[0]*-1, 0, 100)
        perpendecular = [w0[1], w0[0]*-1]
        slope = perpendecular[1]/perpendecular[0]
        x = np.linspace(-20.1, 20.1, 100)
        b = 0
        y = slope*x+b
        ln, = plt.plot(x, y, 'k-')
        plt.pause(0.5)
    if (x[2] == "blue" and np.dot(w0, [x[0], x[1]]) < 0):
        print("skip2")
        continue
    if (x[2] == "blue" and np.dot(w0, [x[0], x[1]]) >= 0):
        print("subtract")
        w0 = subtract(w0, t, [x[0], x[1]])
        ln.remove()
        perpendecular = [w0[1], w0[0]*-1]
        slope = perpendecular[1]/perpendecular[0]
        x = np.linspace(-20.1, 20.1, 100)
        b = 0
        y = slope*x+b
        ln, = plt.plot(x, y, 'k-')
        plt.pause(0.5)


plt.title('Perceptron')
plt.show()
