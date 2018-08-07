import futils
import numpy as np
import matplotlib.pyplot as plt
import argparse
import math


ap=argparse.ArgumentParser(description="Arguments for running the visualisation script")

ap.add_argument('momentum',nargs='*',action="store", default="",type=str,help="Use or not GD with momentum")
ap.add_argument("--lr",dest='lr',action='store',default=0.1,type=float,help="Select the learning rate")
ap.add_argument("--epochs",dest='epochs',action='store',default=50,type=int,help="Select the number of steps for the GD")
ap.add_argument('--gamma',dest='gamma',action='store',default=0.5,type=float,help="Select the gamma parameter for the GD with momentum algorithm. Gamma < 1")
ap.add_argument("--window",dest='window',help="Precise the windows dimensions. Values between 50 and 500",type=int,default=200)
ap.add_argument("--step",dest='step',help="Graph's steps",type=float,default=1)

pa = ap.parse_args()
if pa.window and( pa.window < 10 ):
    ap.error("Window size must be bigger than 50")
if pa.gamma and pa.gamma > 1:
    ap.error("Gamma parameter has to be lower that 1")

epochs = pa.epochs
lr = pa.lr
gamma = pa.gamma
type = pa.momentum
window = pa.window
step = pa.step

if type == ["momentum"]:
    weight = futils.do_GD_momentum(epochs,lr,gamma,window)
else:
    weight = futils.do_GD(epochs,lr,window)

futils.plot_function(weight,window,step)
