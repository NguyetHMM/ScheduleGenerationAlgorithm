import numpy as np

array1 = [0.5, 2]
array2 = [300, 480]
array3 = [4, 6]
array4 = [6, 8]

# 16 giờ

step = 30

array2.append(step)

print(array2)

newArray2 = np.arange(array2[0], array2[1], array2[2]) # np.arrange khong bao gom phan tu cuoi cung

newArray2 = np.append(newArray2, array2[1])

# newArray2.length

print(newArray2)


