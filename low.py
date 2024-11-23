import imageio
import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import convolve

def apply_filter(image, kernel):
    
    return convolve(image, kernel)

def low_pass_filter():
    
    return np.array([[1, 2, 1],
                     [2, 4, 2],
                     [1, 2, 1]]) / 16 
def main_low_pass():
    
    color_image = imageio.imread('C://SMT_5//Pengolahan_Citra//images.jpeg')

    gray_image = np.mean(color_image, axis=2).astype(np.uint8)

    low_passed = apply_filter(gray_image, low_pass_filter())

    
    plt.figure(figsize=(6, 6))
    plt.imshow(low_passed, cmap='gray')
    plt.title('Gambar Low-Pass Filter')
    plt.axis('off')
    plt.show()