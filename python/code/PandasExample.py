# -*- coding: utf-8 -*-

import pandas as pd
import os

print("当前工作目录:",os.getcwd())
## 注意，如果默认路径非code文件夹，需要运行下面语句改为code文件夹路径，
## 具体路径参考个人下载的路径，例如将文件下载在D盘，那么将"path/to/code"
## 换为"D:/A_TechnologyScience/python/code"
## os.chdir("path/to/code")
ExampleDataPath = "../data/Example.csv"
## 从csv文件读取数据
ExampleData = pd.read_csv(ExampleDataPath,encoding = 'gbk')
print("数据类型:",'\n',type(ExampleData))
print("数据维度:",'\n',ExampleData.shape)
print("显示前5行数据:",'\n',ExampleData.head())

## DataFrame保持为csv文件
ExampleSavePath = "../data/ExampleSave.csv"
ExampleData.to_csv(ExampleSavePath,index = False)

## 操作数据
## 索引：loc iloc
## loc:显式索引，使用行列名来索引数据
## iloc:隐式索引，使用行列的序号索引数据
print("显式索引:",'\n',ExampleData.loc[0:2,["学历","男生"]])
print("隐式索引:",'\n',ExampleData.iloc[0:2,0:2])

## 注意到它们之间的区别，显式索引的0:2指行名为0，1，2，所以输出三行
## 隐式索引的0：2指行的序号0：2，python内置的机制一般是取前舍后，
## 即0：2，取0，1，舍掉2，最后显示前两行。

## DataFrame扩展
ExampleData['睡眠时间'] = [8,7,6,5,4]
print("添加一列:",'\n',ExampleData.head())
ExampleData = ExampleData.append({"学历":"幼儿园","男生":5 ,"女生":7,"睡眠时间":10},ignore_index=True)
print("添加一行:",'\n',ExampleData.head(6))

## 数据统计数据分析
print("统计指标:",'\n',ExampleData.describe())
