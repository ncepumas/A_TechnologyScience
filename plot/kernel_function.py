# -*- coding: utf-8 -*-
"""
Created on Sun Jun  9 14:30:53 2019

@author: ZYH
"""
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import seaborn as sns;sns.set();sns.set_style("dark")

## circle_1
def BulidCircle(Centre,Radius):
    theta = np.arange(0,2*np.pi,0.1)
    x = Centre[0] + Radius * np.cos(theta)
    y = Centre[1] + Radius * np.sin(theta)
    return x,y
"""
def plot_style():
    fig = plt.figure(figsize=(8, 8))
    ax = axisartist.Subplot(fig,111)
    fig.add_axes(ax)
    ax.axis[:].set_visible(False) ## 隐藏四周边框
    ## x y坐标轴设置
    ax.axis["x"] = ax.new_floating_axis(0,0) ## (0,0) 0:水平，0:通过0点
    ax.axis["x"].set_axisline_style("->", size = 1.0) #添加箭头
    ax.axis["y"] = ax.new_floating_axis(1,0)
    ax.axis["y"].set_axisline_style("-|>", size = 1.0)
    ## 刻度数值显示方向设置
    ax.axis["x"].set_axis_direction("top")
    ax.axis["y"].set_axis_direction("right")
"""
def PlotCircle2(Centre,Radius,figname):
    plt.figure(figsize=(8, 8))
    x1,y1 = BulidCircle(Centre[0],Radius[0])
    x2,y2 = BulidCircle(Centre[1],Radius[1])
    plt.plot(x1,y1,'bo')
    plt.plot(x2,y2,'go')
    plt.savefig(figname)
    plt.show()
def PlotCircle3(Centre,Radius,figname):
    plt.figure(figsize=(8, 8))
    fig = plt.subplot(111,projection='3d') 
    x1,y1 = BulidCircle(Centre[0],Radius[0])
    z1 = np.array(np.zeros(len(x1)) + Radius[0])
    #X1,Y1 = np.meshgrid(x1,y1)
    #Z1 = np.array(np.zeros(X1.shape) + Radius[0])
    x2,y2 = BulidCircle(Centre[1],Radius[1])
    z2 = np.array(np.zeros(len(x2)) + Radius[1])
    #X2,Y2 = np.meshgrid(x2,y2)
    #Z2 = np.array(np.zeros(X2.shape) + Radius[1])
    fig.scatter(x1,y1,z1,c = 'b',marker='o')
    fig.scatter(x2,y2,z2,c = 'g',marker='o')
    plt.savefig(figname)
    plt.show()

Centre = [[3.0,3.0],[3.0,3.0]]
Radius = [1.5,2]
PlotCircle2(Centre,Radius,'circle2')
PlotCircle3(Centre,Radius,'circle3')
"""
CircleCentre1 = [3.0,3.0]
CircleRadius1
theta = np.arange(0,2*np.pi,0.01)
x = CircleCentre1[0] + np.cos(theta)
y = CircleCentre1[1] + np.sin(theta)
"""