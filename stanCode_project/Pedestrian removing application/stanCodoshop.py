"""
File: stanCodoshop.py
Name: 
----------------------------------------------
This program is SC101 Assignment 3 and is adapted
from Nick Parlante's Ghost assignment.

The assignment has been redesigned and extended
by Jerry Liao to fit the learning objectives of
the stanCode SC101 course.
"""

import os
import sys
from simpleimage import SimpleImage


def get_pixel_dist(pixel, red, green, blue):
    
    """
    Computes the Euclidean color distance between a pixel's RGB values and a target mean RGB color.

    This function measures how similar a pixel is to a reference color by treating the
    red, green, and blue channels as coordinates in a 3D color space. A smaller distance
    indicates a closer color match.

    Parameters:
        pixel (Pixel): The pixel whose RGB components (pixel.red, pixel.green, pixel.blue)
            will be compared.
        red (int): The reference mean red value.
        green (int): The reference mean green value.
        blue (int): The reference mean blue value.

    Returns:
        float: The Euclidean distance between the pixel's RGB values and the reference color.
    """
    Eu_dis = ((pixel.red-red)**2+(pixel.green-green)**2+(pixel.blue-blue)**2)**0.5    
    return Eu_dis


def get_average(pixels):
    """
    Given a list of pixels, finds their average red, blue, and green values.

    Input:
        pixels (List[Pixel]): a list of pixels to be averaged

    Returns:
        rgb (List[int]): a list of average red, green, and blue values of the pixels
                        (returns in order: [red, green, blue])
    """
    sum_red = 0
    sum_green = 0
    sum_blue = 0
    for pixel in pixels:
        sum_red += pixel.red
        sum_green += pixel.green
        sum_blue += pixel.blue
    rgb = [sum_red/len(pixels),sum_green/len(pixels),sum_blue/len(pixels)]

    return rgb


def get_best_pixel(pixels):
    """
    Selects the pixel that is closest in color to the average color of a group of pixels.

    This function examines a list of pixels and determines which one has the smallest
    color distance to the average RGB values of all pixels in the list. It is useful
    for finding the most "representative" pixel in a set.

    Parameters:
        pixels (List[Pixel]): A list of Pixel objects to evaluate.

    Returns:
        Pixel: The pixel whose color is closest to the average color of the input list.
    """
    #先把pixels丟進去get_average製造出avg = [avg_red,avg_green,avg_blue]
    #對每個pixel跑get_pixel_dist(pixel,avg_red,avg_green,avg_blue)取出距離最小pixel並回傳他的rgb
    #隨時紀錄最好的pixel
    #一個一個比較距離
    final_pixel = None
    final_pixel_dist = 1000000000000000 
    avg = get_average(pixels)
    for pixel in pixels:
        pixel_dist = get_pixel_dist(pixel,avg[0],avg[1],avg[2])
        if pixel_dist < final_pixel_dist:#如果距離小於final_pixel_dist，更新final_pixel_dist，並更新final_pixel
            final_pixel = pixel
            final_pixel_dist = pixel_dist

    return final_pixel


def solve(images):
    """
    Given a list of image objects, compute and display the solution image
    based on images. There will be at least 3 images and they will all
    be the same size.

    Input:
        images (List[SimpleImage]): list of images to be processed
    """
    width = images[0].width
    height = images[0].height
    result = SimpleImage.blank(width, height)
    
    #input一個裝有圖片的list
    #先製造一個空白的圖片
    #把images 
    #pixels只代表一個點，所以總共需要mxn個pixels，可以存成一個(m,n)的矩陣，裡面裝滿最佳的[r,g,b]
    #用最佳rgb矩陣去更新那個空白的圖片
    ##########太沒效率##########
    #直接遍歷圖片的所有pixel直接更新在圖片上

    
    # ----- YOUR CODE STARTS HERE ----- #
    # Write code to populate image and create the 'ghost' effect
    for y in range(height):
        for x in range(width):
             
            pixels = list(map(lambda i:i.get_pixel(x,y),images))
            pix = get_best_pixel(pixels) #取出每個image(x,y)的[r,g,b]
            result.set_pixel(x,y,pix) #把pixels丟進去get_best_pixel，就會生成pix

    # ----- YOUR CODE ENDS HERE ----- #

    print("Displaying image!")
    result.show()


def jpgs_in_dir(dir):
    """
    (provided, DO NOT MODIFY)
    Given the name of a directory, returns a list of the .jpg filenames
    within it.

    Input:
        dir (string): name of directory
    Returns:
        filenames(List[string]): names of jpg files in directory
    """
    filenames = []
    for filename in os.listdir(dir):
        if filename.endswith('.jpg'):
            filenames.append(os.path.join(dir, filename))
    return filenames


def load_images(dir):
    """
    (provided, DO NOT MODIFY)
    Given a directory name, reads all the .jpg files within it into memory and
    returns them in a list. Prints the filenames out as it goes.

    Input:
        dir (string): name of directory
    Returns:
        images (List[SimpleImages]): list of images in directory
    """
    images = []
    jpgs = jpgs_in_dir(dir)
    for filename in jpgs:
        print("Loading", filename)
        image = SimpleImage(filename)
        images.append(image)
    return images


def main():
    # (provided, DO NOT MODIFY)
    args = sys.argv[1:]
    # We just take 1 argument, the folder containing all the images.
    # The load_images() capability is provided above.
    images = load_images(args[0])
    solve(images)


if __name__ == '__main__':
    main()
