import numpy as np

img = np.array([[10, 20, 30],
                [40, 50, 60],
                [70, 80, 90]])

print("Original Image:\n", img)

print("Reshaped Image:\n", img.reshape(1, 9))

print("Sliced Region:\n", img[0:2, 0:2])

print("Brightness Adjusted:\n", img + 20)

transform = np.array([[1, 0, 0],
                      [0, 1, 0],
                      [0, 0, 1]])

print("Transformed Image:\n", np.dot(img, transform))