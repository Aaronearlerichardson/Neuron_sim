# run in interactive python mode
from random import random

from matplotlib.pyplot import fill, figure, subplot, pause, show, xlim, ylim
from numpy import linspace, cos, sin, pi, dot, loadtxt, outer


def circle(radius, x, y, value):
    """create graphical circle

    """
    t = linspace(0, 2 * pi, 1000)
    a = cos(t)
    b = sin(t)
    if value == 1.0:
        fill(x + radius * a, y + radius * b, 'b')
    elif value == -1.0:
        fill(x + radius * a, y + radius * b, 'w')
    elif value == 2.0:
        fill(x + radius * a, y + radius * b, 'r')
    elif value == 3.0:
        fill(x + radius * a, y + radius * b, 'g')
    else:
        return


def net(dim1, values):
    """create the network circles that become the image (7x7)

    """
    k = 0
    for i in range(dim1):
        for j in range(dim1):
            circle(0.4, i, j, values[k])
            k = k + 1


def recall(activity, weights):
    """storage scheme for final graph at the end

    """
    outt = dot(weights, activity)
    a = outt
    for n in range(len(activity)):
        if outt[n] >= 0.0:
            a[n] = 1.0
        if outt[n] < 0.0:
            a[n] = -1.0
        if outt[n] == 0.0:
            a[n] = outt[n]
    return (a)


def ener(activity, weights):
    """function for detemining the "energy" or difference between the ideal
    picture and the real picture
    """
    e = 0
    volt = dot(activity, weights)
    for k in range(49):
        for n in range(49):
            e = e + weights[n, k] * volt[n] * volt[k]
    e = -0.5 * e
    return (e)


def updateone(n, activity, weights):
    """a recursive function that repeatedly calculates energy and stores it for
     last display

    """
    a = 0.0
    for k in range(len(activity)):
        a = a + weights[n, k] * activity[k]
    if a > 0.0:
        act = 1.0
    elif a < 0.0:
        act = -1.0
    elif a == 0.0:
        act = activity[n]
    else:
        return 
    return act


def main(file: str):
    In1 = loadtxt(file)
    test1 = In1

    w = 1 / 49.0 * outer(In1, In1)
    figure(1)
    subplot(1, 4, 1)
    net(7, In1)
    for n in range(49):
        r = random()
        if 0.2 > r:
            if test1[n] == 1:
                test1[n] = -1
            if test1[n] == -1:
                test1[n] = 1

    subplot(1, 4, 2)
    net(7, test1)
    subplot(1, 4, 3)
    net(7, test1)
    pause(1)
    rec = test1
    figure(1)
    for n in range(49):
        rec[n] = updateone(n, rec, w)
        e = ener(rec, w)
        subplot(1, 4, 3)
        net(7, rec)
        pause(0.001)
        show()
        e = ener(rec, w)
        subplot(1, 4, 4)
        ylim([-50, 0])
        xlim([0, 50])
        circle(0.5, n, e, 1.0)


if __name__ == "__main__":
    main('grim.txt')
