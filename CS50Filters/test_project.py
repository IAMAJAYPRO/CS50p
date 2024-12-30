from filters import normalise_arr, grayscale, sepia, edge, np, Image, capify
import project


def compare_images(A: Image.Image, B: Image.Image) -> bool:
    "Return ```True``` if images are equal."
    Arr = np.array(A)
    Brr = np.array(B)
    equal = np.array_equal(Arr, Brr)
    if not equal:
        print("Dindn't match")
        print("\nArr:\n")
        print(Arr)
        print("\nBrr:\n")
        print(Brr)
    return equal


def test_normalise_arr():
    arr = np.array([[1, 2, 3], [4, 5, 6]])
    expected = np.array([[42,  85, 127],
                         [170, 212, 255]])
    assert np.array_equal(normalise_arr(
        arr), expected), "normalise_arr output dint match"


def test_capify():
    arr = np.array([[42,  585, 127],
                    [170, 262, 255]])
    expected = np.array([[42,  255, 127],
                        [170, 255, 255]])
    output = capify(arr)
    assert np.array_equal(output, expected), "Capify didnt work properly"


def test_grayscale():
    inp_arr = np.array([
        [[100, 150, 200], [50, 75, 100]],  # Row 1
        [[25, 50, 75], [10, 20, 30]]      # Row 2
    ], dtype=np.uint8)
    inp_img = Image.fromarray(inp_arr)
    expected = Image.fromarray(np.array([[150,  75],
                                         [50,  20]]))
    out_img = grayscale(inp_img)
    assert compare_images(out_img, expected), "Grayscale Output didnt match"


def test_sepia():
    input = Image.fromarray(np.array([
        [[100, 150, 200], [50, 75, 100]],
        [[25, 50, 75], [0, 0, 0]]
    ], dtype=np.uint8))

    expected = Image.fromarray(np.array([
        [[192, 171, 133], [96, 85, 66]],
        [[62, 55, 43], [0, 0, 0]]
    ], dtype=np.uint8))

    output = sepia(input)
    assert compare_images(expected, output), "Sepia Output didnt match"


"""
def test_edge_sobel():
    raise NotImplementedError("Yet to implement tests for edge detection")
    image_arr = np.array([[[10, 20, 30], [10, 20, 30], [10, 20, 30]], [[40, 50, 60], [
                         40, 50, 60], [40, 50, 60]], [[70, 80, 90], [70, 80, 90], [70, 80, 90]]], dtype=np.uint8)
    inp_img = Image.fromarray(image_arr)
"""
