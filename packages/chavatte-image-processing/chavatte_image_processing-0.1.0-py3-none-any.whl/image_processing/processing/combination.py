import numpy as np
from skimage.color import rgb2gray
from skimage.exposure import match_histograms
from skimage.metrics import structural_similarity

def find_difference(image1, image2):
    assert image1.shape == image2.shape, "Specify 2 images with de same shape."

    if image1.shape[-1] == 4:
        image1 = image1[..., :3]
    if image2.shape[-1] == 4:
        image2 = image2[..., :3]

    gray_image1 = rgb2gray(image1)
    gray_image2 = rgb2gray(image2)
    data_range = image1.max() - image1.min()
    (score, difference_image) = structural_similarity(gray_image1, gray_image2, full=True, data_range=data_range)

    print("Similarity of the images:", score)
    normalized_difference_image = (difference_image-np.min(difference_image))/(np.max(difference_image)-np.min(difference_image))
    return normalized_difference_image

def transfer_histogram(image1, image2):
    matched_image = match_histograms(image1, image2)
    return matched_image