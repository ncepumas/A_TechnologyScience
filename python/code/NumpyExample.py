# -*- coding: utf-8 -*-

# numpy 
import numpy as np

# 创建一个numpy数组
array_items = np.array([1,4,5])
print(array_items)

# 生成有规律的数据
# 注意生成数组的同一形式，函数第一个参数为数组的维度，后续参数为数组的内容
print("生成均为0的数组:",'\n',np.zeros(10,dtype = int))

print("生成均为1的数组:",'\n',np.ones((3,5),dtype = float))

print("生成为指定数字的数组:",'\n',np.full((3,5),3.14))

print("生成0~20之间，间隔为2的数组:",'\n',np.arange(0,20,2))

print("生成10个0~20之间，均匀间隔的数组:",'\n',np.linspace(0,20,10))

print("生成均匀分布的数组:",'\n',np.random.random((3,3)))

print("生成正态分布的数组:",'\n',np.random.normal(0,1,(3,3)))

print("生成随机整数的数组:",'\n',np.random.randint(0,10,(3,3)))

print("生成单位阵:",'\n',np.eye(3))

# 操作数组
## 生成三个测试数组
np.random.seed(1234) # 随机种子，可复现结果
ExampleArray1 = np.random.random((2,2))
ExampleArray2 = np.random.normal(0,1,(2,2))
ExampleArray3 = np.random.randint(0,10,5)

# 索引指定位置数据
print("ExampleArray1:",'\n',ExampleArray1)
print("行逆序显示:",'\n',ExampleArray1[::-1,:])
print("列逆序显示:",'\n',ExampleArray1[:,::-1])
print("完全逆序显示:",'\n',ExampleArray1[::-1,::-1])
print("索引[0,0]位置数据:",'\n',ExampleArray1[0,0])
print("索引第一列数据:",'\n',ExampleArray1[:,0])
print("索引第一行数据:",'\n',ExampleArray1[0,:])

print("ExampleArray2:",'\n',ExampleArray2)
print("行拼接:",'\n',np.concatenate([ExampleArray1,ExampleArray2],
                                 axis = 0))
print("列拼接:",'\n',np.concatenate([ExampleArray1,ExampleArray2],
                                 axis = 1))

print("ExampleArray3:",'\n',ExampleArray3)
print("顺序排序:",'\n',np.sort(ExampleArray3))
print("逆序排序:",'\n',np.sort(ExampleArray3)[::-1])

# 数组计算
np.random.seed(1111) # 随机种子，可复现结果
ExampleArray4 = np.random.randint(0,10,5)
print("ExampleArray4:",'\n',ExampleArray4)

print("指数运算:",'\n',np.exp(ExampleArray4))
print("对数运算:",'\n',np.log(ExampleArray4))
print("求和运算:",'\n',np.sum(ExampleArray4))
print("求积运算:",'\n',np.multiply.reduce(ExampleArray4))
print("累加运算:",'\n',np.add.accumulate(ExampleArray4))
print("累积百分比:",'\n',np.add.accumulate(ExampleArray4)/np.sum(ExampleArray4))
print("取最大运算:",'\n',np.max(ExampleArray4))
