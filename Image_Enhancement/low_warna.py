import imageio.v2
import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import convolve

def apply_filter(image, kernel):

    return convolve(image, kernel)

def low_pass_filter():
    
    return np.array([[1, 2, 1],
                     [2, 4, 2],
                     [1, 2, 1]]) / 16  

def main_low_pass_color():
    
    color_image = imageio.v2.imread('C://SMT_5//Pengolahan_Citra//images.jpg')

    low_passed = np.zeros_like(color_image)
    for i in range(3): 
        low_passed[..., i] = apply_filter(color_image[..., i], low_pass_filter())

    
    plt.figure(figsize=(6, 6))
    plt.imshow(low_passed)
    plt.title('Low-Pass Filter Berwarna')
    plt.axis('off')
    plt.show()

main_low_pass_color()