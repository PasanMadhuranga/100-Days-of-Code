# Watermark Adder

## Overview
Watermark Adder is a simple GUI application built with Python that allows users to add custom watermarks to their images. It supports various fonts and colours for the watermark text and can process images from both local storage and the web.

## Features
- Add text watermarks to images.
- Customize the font style, size, and colour of the watermark.
- Position the watermark at a specific location on the image.
- Support for images loaded from a URL or local path.
- Save the watermarked image with a custom name and directory.

## Technologies Used
- Python
- Tkinter for the GUI
- PIL (Python Imaging Library) for image processing
- URLlib for handling images from the web

## Requirements
To run Watermark Adder, ensure you have Python installed on your system. Additionally, you will need the following Python packages:
- `PIL` (or `Pillow`)
- `tkinter`

These can be installed via pip if they're not already present:
```sh
pip install Pillow
```

## Usage
1. Start the application by running `main.py`.
2. Input the image URL or path in the provided text field.
3. Enter the watermark text and customize the appearance as desired.
4. Choose the location for the watermark on the image.
5. Enter the name and destination of the saved watermarked image.
6. Click 'Add' to apply the watermark and save the image.

## How to Contribute
Contributions to the Watermark Adder are welcome! Please read the `CONTRIBUTING.md` for more details on submitting pull requests to us.

## Screenshots
Here's a preview of the Watermark Adder application in action:

![Watermark Adder Application Screenshot](screenshots/app.png)
