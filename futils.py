import numpy as np
import matplotlib.pyplot as plt
import math


def derivative(x):
    '''This function computes the numerical value of the derivative of the cost function.

    Args:
        X (float) : Derivative function input value

    Returns:
            yhat (float) : The value of the derivative function
    '''
    yhat = 2 * x #Change this to use other functions
    return yhat

def cost_function(x):
    '''
    This function computes the value of the cost function y=x^2

    Args:
        x (float): the input of the function

    Returns:
            y (float): the output of the function
    '''
    y= x**2   # Change this to use other functions
    return y

def plot_function(weight,window,step):
    '''This function plots the function along with the steps from the Gradient Descend Algoritmh

    Args:
        weight (numpy array): The different weights for plotting
        windows (int): The window's size
        step(float): The graph's step

    Returns:
            NaN
    '''

    x = np.arange(-window,window,step)
    y = np.square(x) # change this to use other function
    fig, ax = plt.subplots()

    for i in range(len(weight)):
        ax.cla()
        plt.plot(weight[i],cost_function(weight[i]),'ro')
        plt.plot(x,y)
        ax.set_title("frame {}".format(i))
        plt.pause(0.001)


def do_GD(epochs,lr,window):
    '''This function used a basic Gradient Descend algoritmh to find a minimum

    Args:
        epochs (int): The number of steps the algorithm performs
        lr (float): The learning rate for the GD
        windows (int): The window's size

    Returns:
            weight (numpy array): An array containg the consecutive weights the algorithm came up to
    '''

    weight=[]
    weight.append(np.random.randint(-window-100,window+100))
    for i in range(0,epochs):
        weight.append(weight[i] - lr *derivative(weight[i]))

    return weight

def do_GD_momentum(epochs,lr,gamma,window):
    '''This function used a basic Gradient Descend with momentum algoritmh to find a minimum

    Args:
        epochs (int): The number of steps the algorithm performs
        lr (float): The learning rate for the GD
        gamma (float): The gamma parameter
        windows (int): The window's size

    Returns:
            weight (numpy array): An array containg the consecutive weights the algorithm came up to
    '''

    weight=[]
    v=[1]
    weight.append(np.random.randint(-window+50,window-50))
    for i in range(0,epochs):
        v.append(gamma*v[i] + lr *derivative(int(weight[i])))
        weight.append(weight[i] - v[i])
    return weight
