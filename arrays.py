import numpy as np
arr_1d = np.array([1,2,3,4,5])
arr_2d = np.array([[1,2,3], [4,5,6]])
arr_zeros = np.zeros((3,3))
arr_ones = np.ones((3,4))
arr_random = np.random.rand(3,3)
arr_range = np.arange(0,20,2)
print("original arr_2d:", arr_2d)
print ("access element at row 0, column 1:", arr_2d[0,1])
arr_2d[1,2] = 10
print("modified arr_2d:", arr_2d)
arr_slice = arr_2d[:, 1]
arr_1d_slice = arr_1d[1:4]
arr_bool = arr_1d[arr_1d > 3]
print("Elements greater than 3:", arr_bool)
arr_squared = arr_1d ** 2
arr_sum = np.sum(arr_2d)
arr_mean = np.mean(arr_2d)
reshape_arr = np.reshape(arr_1d, (1,5))
flatten_arr = arr_2d.flatten()
arr_broadcast = arr_2d + np.array([1,0,1])
arr_masked = np.where(arr_1d % 2 == 0, "Even", "Odd")
print("1d", arr_1d)
print("2d",arr_2d)
print("0s",arr_zeros)
print("1s",arr_ones)
print("i-i", arr_range)
print("x", arr_slice)
print("2-2d", arr_1d_slice)
print("+",arr_sum)
print("flatten", flatten_arr)
print("broadcast", arr_broadcast)
print("masked", arr_squared)

arr_1d = [1,2,3,4,5]
arr_2d = [[1,2,3],[4,5,6],[7,8,9],[4,3,2]]
arr_zeros = [0] * 5
arr_ones = [1] * 5
arr_range = list(range(0,20,2))
print("original arr 2d, arr_2d")
print("access elemen at r 0, col 1", arr_2d[0][1])
arr_2d[1][2] = 10
print("modified arr", arr_2d)
arr_slice = arr_1d[1:4]
second_column = [row[1] for row in arr_2d]
arr_squared = [x**2 for x in arr_1d]
arr_filtered = [x for x in arr_1d if x < 3]
arr_sum = sum (arr_1d)
arr_mean = arr_sum / len(arr_1d) if arr_1d else 0
reshaped_arr = [arr_1d[i:i+2] for i in range(0, len(arr_1d), 2)]
 Example
# If arr_1d = [1, 2, 3, 4, 5, 6], then:
# reshaped_arr = [arr_1d[i:i+2] for i in range(0, len(arr_1d), 2)]
# reshaped_arr = [[1, 2], [3, 4], [5, 6]]
arr_masked = ["Even" if x % 2 == 0 else "Odd" for x in arr_1d]
print("1D Array:", arr_1d)
print("2D Array:", arr_2d)
print("Array of Zeros:", arr_zeros)
print("Array of Ones:", arr_ones)
print("Range Array:", arr_range)
print("Sliced Array (1D):", arr_slice)
print("Second Column from 2D Array:", second_column)
print("Filtered Array (Elements > 3):", arr_filtered)
print("Squared 1D Array:", arr_squared)
print("Sum of 1D Array:", arr_sum)
print("Mean of 1D Array:", arr_mean)
print("Reshaped Array (Pairs):", reshaped_arr)
print("Masked Array with Even/Odd:", arr_masked)
# Example
# If arr_1d = [1, 2, 3, 4, 5, 6], then:
# reshaped_arr = [arr_1d[i:i+2] for i in range(0, len(arr_1d), 2)]
# reshaped_arr = [[1, 2], [3, 4], [5, 6]]




