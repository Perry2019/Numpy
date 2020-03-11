# 1. Numpy属性
import numpy as np
array = np.array([[1,2,3],[4,5,6]])

print(array)
print('number of demension:', array.ndim)
print('shape:', array.shape)
print('size:', array.size)

# 2. Numpy 矩阵的生成
a = np.array([1,2,3],dtype='int32')
print(a)
b = np.zeros((3,4))
print(b)
c = np.arange(10,20,2)
print(c)
d = np.arange(10,20,1).reshape(2,5)
print(d)
e = np.arange(12).reshape(3,4)
print(e)
f = np.linspace(1,10,5)
print(f)

# 3. Numpy的基础运算
aa = np.random.random((2,4))  # 生成0~1的随机数
print(aa)
print(np.max(aa, axis=0))     # 每列最大值
print(np.min(aa, axis=1))     # 每行最小值

bb = np.array([[1,2],
                [4,5]])
cc = np.arange(4).reshape(2,2)
print(bb*cc)                 # 矩阵内积
print(np.dot(bb,cc))         # 矩阵乘法
print(bb**2)                 # 矩阵平方

# 4. Numpy的运算2
A = np.arange(2,14).reshape((3,4))
print(A)
print(np.mean(A,axis=0))    # 均值
print(np.cumsum(A))         # 累加
print(np.transpose(A))      # 转置
print(np.clip(A,2,3))       # 设置范围控制矩阵（所有小于2的设为2，大于3的设为3，其余保持）

# 5. Numpy的索引
A = np.arange(3,15).reshape((3,4))
print(A)
print(A[2])                    # 第2行
print(A[2,:])                  # 第2行
print(A[2,1])                  # 第2行,第1列 元素索引
print(A[:,1])                  # 第1列

# 语句行索引
for row in A:
    print(row)

# 语句列索引
for column in A.T:
    print(column)

# 元素迭代列打印
print(A.flatten())
for item in A.flat:
    print(item)

# 6. Numpy的array合并
A = np.array([1,1,1,1])
B = np.array([2,2,2,2])
print(np.vstack((A,B)))                     # 垂直方向合并
print(np.hstack((A,B)))                     # 水平方向合并
print(A[:,np.newaxis])                      # 序列横向变纵向
C = np.concatenate((A,B,B,A), axis=0)       # 多个array在列方向合并
print(C)

# 7. Numpy的array分割
A = np.arange(0,12).reshape((3,4))
print(A)
print(np.split(A,2,axis=1))                # 垂直方向分割
print(np.hsplit(A,2))                      # 垂直方向分割
print(np.split(A,3,axis=0))                # 水平方向分割
print(np.vsplit(A,3))                      # 水平方向分割
print(np.array_split(A,3,axis=1))          # 垂直方向分割

# 8. Numpy的copy
a = np.arange(0,12).reshape((3,4))
print(a)
a[1,2] = 77
print(a)
b = a                                     # copy
a[2,2] = 66
print(b)
b = a.copy()                              # deep copy
a[2,2] = 33
print(b)