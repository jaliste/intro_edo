from numpy import *
import pylab as p
def normalize (DX,DY):
    M = (hypot(DX, DY))                           # Norm of the growth rate 
    M[ M == 0] = 1.                                 # Avoid zero division errors 
    return DX / M , DY / M                                      # Normalize each arrows

def autonomous_slope_field(equation, x, y, X0 = None):
    X1 , Y1  = meshgrid(x, y)                 # create a grid
    DX1 = ones (X1.shape)
    DY1 = equation(Y1)
    DX1, DY1 = normalize(DX1, DY1)
    from scipy import integrate
    X, infodict = integrate.odeint(equation, X0, x, full_output=True)
    p.plot(t,X)
    Q = p.quiver(X1,Y1, DX1, DY1, pivot='mid')
