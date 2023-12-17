import matplotlib.pyplot as plt
import numpy as np

def log_spiral():
    f = np.arange(0, 8 * np.pi, 0.01)
    e = 2.7182818284590452353602874713527
    b = 1
    r = e ** (b * f)

    x = r * np.cos(f)
    y = r * np.sin(f)

    plt.plot(x, y, label='log_spiral')
    plt.legend()
    plt.xlabel('coord: x') # подпись координат
    plt.ylabel('coord: y')
    plt.grid()
    plt.axis('equal')

    plt.savefig('fig_lab_4.1.png')



def arh_spiral():
    f = np.arange(0, 8 * np.pi, 0.01)
    k = 10
    r = k * f

    x = r * np.cos(f)
    y = r * np.sin(f)

    plt.plot(x, y, label='arhimedova spipal')
    plt.grid()
    plt.legend()
    plt.xlabel('coord: x') # подпись координат
    plt.ylabel('coord: y')
    plt.axis('equal')
    plt.savefig('fig_lab_4.2.png')


    
def wand_spiral():
    f = np.arange(0.01, 8 * np.pi, 0.01)
    k = 100

    r = k / f ** 0.5

    x = r * np.cos(f)
    y =  r * np.sin(f)


    plt.plot(x, y, label='wand')
    plt.grid()
    plt.legend()
    plt.xlabel('coord: x') # подпись координат
    plt.ylabel('coord: y')
    plt.axis('equal')
    plt.savefig('fig_lab_4.3.png')

    
def rose():
    f = 8 * np.pi
    k = np.arange(0, 10, 0.01)
    
    r = np.sin(k * f)

    x = r * np.cos(k)
    y = r * np.sin(k)

    plt.plot(x, y, label='rose')
    plt.xlabel('coord: x') # подпись координат
    plt.ylabel('coord: y')
    plt.legend()
    plt.axis('equal')
    plt.savefig('fig_lab_4.4.png')

#rose()
#log_spiral()
#arh_spiral()
#wand_spiral()

