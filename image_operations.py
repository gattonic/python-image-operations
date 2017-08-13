from  PIL import Image
import numpy as np


def load_greyscale(image, return_as_array=True, show_image=False, save_image=False):
    img = Image.open(image)
    img = img.convert('L')

    return __option_routine(img, return_as_array, show_image, save_image)


def load_binary(image, threshold, return_as_array=True, show_image=False, save_image=False):
    img = load_greyscale(image, return_as_array=False)
    (width, height) = img.size
    img_pixel_map = img.load()

    binary_img = Image.new('1', img.size)
    binary_img_pixel_map = binary_img.load()

    for x in range(0, width):
        for y in range(0, height):
            binary_img_pixel_map[x,y] = 1 if img_pixel_map[x,y] >= threshold else 0

    return __option_routine(binary_img, return_as_array, show_image, save_image)


def gamma_correction(img, gamma, return_as_array=True, show_image=False, save_image=False):
    img_array = np.asarray(img)
    img_corrected_array = 255 * ((img_array/255) ** (1/gamma))
    img_corrected_array = np.uint8(img_corrected_array)
    img_corrected = Image.fromarray(img_corrected_array, img.mode)
    return __option_routine(img_corrected, return_as_array, show_image, save_image)


def __option_routine(img, return_as_array, show_image, save_image):
    if show_image:
        img.show()

    if save_image:
        img.save(img + ".jpg")

    if return_as_array:
        img = np.asarray(img)

    return img

