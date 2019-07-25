import matplotlib.pyplot as plt
x = [1, 2, 3]
y = [1, 2, 3]
fig = plt.figure()
ax = plt.axes()
plt.plot(x, y)
plt.show()


'''
Example of using matplotlib's Circle patch
'''
import matplotlib.pyplot as plt
def create_circle():
    circle = plt.Circle((0, 0), radius = 0.5)
    return circle

def show_shape(patch):
    ax = plt.gca()
    ax.add_patch(patch)
    ax.set_aspect('equal')
    plt.axis('scaled')
    plt.show()

if __name__ == '__main__':
    c = create_circle()
    show_shape(c)

