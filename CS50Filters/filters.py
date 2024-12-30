import numpy as np
from PIL import Image, ImageFilter


def normalise_arr(arr: np.ndarray, scale=255) -> np.ndarray:
    max = arr.max()
    normalised = arr * (255/max)
    return normalised.astype(np.uint8)


def capify(arr: np.ndarray, max=255):
    """Performs on the provided array"""
    return arr.clip(max=255)


def grayscale(image: Image.Image) -> Image.Image:
    arr = np.array(image)
    grey_arr = arr.mean(axis=-1)
    return Image.fromarray(grey_arr).convert("L")


def edge(image): return image.filter(ImageFilter.FIND_EDGES)
def reflect(image): return image.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
def blur(image): return image.filter(ImageFilter.BLUR)


class sobel:
    x = ImageFilter.Kernel(
        size=(3, 3), kernel=[-1, 0, 1, -2, 0, 2, -1, 0, 1], scale=8)
    y = ImageFilter.Kernel(
        size=(3, 3), kernel=[-1, -2, -1, 0, 0, 0, 1, 2, 1], scale=8)


def edge_sobel(image: Image.Image):
    Gx_arr = np.array(image.filter(sobel.x))
    Gy_arr = np.array(image.filter(sobel.y))
    arr = np.sqrt(Gx_arr**2 + Gy_arr**2)
    # print(arr, arr.max())
    arr = normalise_arr(arr).astype(np.uint8)
    output = Image.fromarray(arr)
    return output


class sepia_filter:
    R = np.array([0.393, 0.769, 0.189])
    G = np.array([0.349, 0.686, 0.168])
    B = np.array([0.272, 0.534, 0.131])


def sepia(img: Image.Image):
    arr = np.array(img)
    R = capify((arr*sepia_filter.R).sum(axis=-1)).astype(np.uint8)
    G = capify((arr*sepia_filter.G).sum(axis=-1)).astype(np.uint8)
    B = capify((arr*sepia_filter.B).sum(axis=-1)).astype(np.uint8)
    return Image.merge("RGB", [Image.fromarray(channel) for channel in [R, G, B]])


available_filters = dict(
    none=lambda img: img,
    edge_sobel=edge_sobel,
    edge=edge,
    blur=blur,
    grayscale=grayscale,
    reflect=reflect,
    sepia=sepia,
)
