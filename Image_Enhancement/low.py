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

def main_low_pass():
    
    color_image = imageio.v2.imread('C://SMT_5//Pengolahan_Citra//Image_Enhancement//images.jpg')

    if color_image is None:
        print("Gambar tidak dapat dibaca. Pastikan path benar.")
        return

    gray_image = np.mean(color_image, axis=2).astype(np.uint8)

    low_passed = apply_filter(gray_image, low_pass_filter())

    plt.figure(figsize=(6, 6))
    plt.imshow(low_passed, cmap='gray')
    plt.title('Low-Pass Filter')
    plt.axis('off')
    plt.show()

main_low_pass()