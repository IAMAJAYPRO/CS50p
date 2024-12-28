# CS50Filter: A Command-Line Image Filter App
    ### Video Demo:  <URL HERE>
    ### Description:
    This project is a python CLI (command line interface) app to apply various filters to images.
    It used Pillow library to essentially support any image format supported by Pillow library.

    Usage: ```project.py [-h] input_img filter [output_img]```
    If the output_file_name is not provided then it temporarily opens the image.
    Use [-h] flag for available filters


    ####Files: 
        project.py:
            This file contains main function
            It also uses argparse python library to support command line interface.
        
        filters.py
            This file contains function definitions to apply filters
            Implemented filters:
                Grayscale
                Blur
                Sepia
                Reflect: flips the image left to right.
                Edge: detect edges using `ImageFilter.FIND_EDGES`.
                Edge_Sobel: detect edges using sobel operators.

            It also contains a dictionary which is used in main to call the correct filter function

        test_project.py
            This file contains tests to test the filter functions