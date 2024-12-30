# CS50Filter: A Command-Line Image Filter App
### Video Demo: 
[CS50Filters Video Demo](https://youtu.be/ok3NyBbytcc)
### Description:
This project is a python CLI (command line interface) app to apply various filters to images.
It used Pillow library to essentially support any image format supported by Pillow library.

#### Usage
```bash
project.py [-h] input_img filter [output_img]
```
- If the output_file_name is not provided then it temporarily displays the image.
- Use [-h] flag for available filters


### Files: 
- project.py:
    - This file contains main function
    - It also uses argparse python library to support command line interface.
        
- filters.py
    - This file contains function definitions to apply filters
    - Implemented filters:
        1. None: Use this filter to only change the extension (convert).
        2. Grayscale
        3. Blur
        4. Sepia
        5. Reflect: flips the image left to right.
        6. Edge: detect edges using `ImageFilter.FIND_EDGES`.
        7. Edge_Sobel: detect edges using sobel operators.

    - It also contains a dictionary which is used in main to call the correct filter function

- test_project.py
    - This file contains tests to test the filter functions


### Workflow
    1. Supply img and filter through command prompt.
    2. Open the image and pass it to a filter function.
    3. The filter functions are in a dictionary called filters.available_filters. 
    4. Each filter function takes an Image.Image object and applies filter to it and returns another Image.Image object
    5. This returned img then can be saved into desired format (or directly opened if the output file name is not provided). 