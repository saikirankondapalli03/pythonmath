import matplotlib.pyplot as plt
import matplotlib.cm as cm
import random

x0, x1 = -2.5, 1
y0, y1 = -1, 1


def initialize_image(x_p, y_p):
    image = []
    for i in range(y_p):
        x_colors = []
        for j in range(x_p):
            x_colors.append(0)
        image.append(x_colors)
    return image

def color_points():
    x_p = 400
    y_p = 400
    n= 400
    dx = (x1-x0)/(n-1)
    dy = (y1-y0)/(n-1)
    x_coords = [x0 + i*dx for i in range(n)]
    y_coords = [y0 + i*dy for i in range(n)]
    max_iteration = 1000
    image = initialize_image(x_p, y_p)
    for i in range(0,len(x_coords)):
        for j in range(0,len(y_coords)):
            z1= complex(0,0)
            c= complex(x_coords[i],y_coords[j])
            iteration =0 
            for k in range(max_iteration): 
                if abs(z1) > 2.0: break
                z1 = z1 * z1 + c 
                iteration += 1
            image[j][i] = iteration
    plt.imshow(image, origin='lower', extent=(-2.5,9.0, 1.0, 8.0),
    cmap=cm.Greys_r, interpolation='nearest')
    plt.show()

if __name__ == '__main__':
    color_points()