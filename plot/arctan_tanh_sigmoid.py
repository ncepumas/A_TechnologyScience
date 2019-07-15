# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 14:17:56 2019

@author: ZYH
"""
import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.axisartist as axisartist
import seaborn as sns;sns.set();sns.set_style("dark")
## sns.set_style() darkgrid、whitegrid、dark、white、ticks
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

def plot_fig(function_,fig_name):
    plot_style()
    x = (np.random.rand(1000)-0.5) * 20 
    x = np.sort(x)
    y = function_(x)
    
    plt.plot(x,y)
    plt.savefig(fig_name)
    plt.show()

def sigmoid(x):
    return (1/(1+np.exp(-x)))

plot_fig(np.tanh,"tanh.png")
plot_fig(np.arctan,"arctan.png")
plot_fig(sigmoid,"sigmoid.png")
