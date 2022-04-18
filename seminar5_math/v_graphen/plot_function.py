import matplotlib.pyplot as plt
import numpy as np

# 100 linearly spaced numbers
x = np.linspace(-10,10,100)
#print(x)
# the function, which is y = x^2 here
y = (x ** 2) -10
y2 = (1 / x ** 2) + 10
y3 = (3 * x ** 2 - 7) / (2 * x)
y4 = x**3

# setting the axes at the centre
fig = plt.figure()
ax = fig.add_subplot(2, 3, 1)
#ax = plt.gca()
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

#plt.xlim(-50, 50)
#plt.ylim(-100, 150)

# plot the function
plt.title("y und y2")
plt.plot(x, y, 'red',linestyle="solid")
plt.plot(x, y2, 'black',linestyle="solid")

ax = fig.add_subplot(234)
plt.title("y3")
plt.plot(x, y3, 'green',linestyle="solid")


ax = fig.add_subplot(2, 3, 6)
plt.title("y4")
plt.plot(x, y4, 'blue',linestyle="dotted")

# show the plot
plt.show()
