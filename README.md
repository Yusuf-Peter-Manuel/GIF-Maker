# GIF-Maker

## An easy-to-use program that turns a set of images into a GIF file.

This program is a short ~50 line script that turns a set of images, from either a folder/compressed folder into a GIF file. The choice of language is Python, and the main module used is ImageIO for the handling of images.

## Requirements

* Python >= 3.10
* ImageIO
* NumPy
* Pillow >= 8.3.2

## Project Installation

Installing this program can be done through either one or two ways. The first option is to clone this repository with the command below by installing [Git](https://git-scm.com/install/) either through their website, or by using a package manager of your choice, e.g., [WinGet](https://learn.microsoft.com/en-us/windows/package-manager/winget/) for Windows, APT for various Linux Distributions (Debian, Ubuntu, and Linux Mint), and [Brew](https://brew.sh/) for MacOS. 

The second option is just to manually download the script from GitHub and place it wherever.

### Option 1
```
git clone htps://github.com/Yusuf-Peter-Manuel/GIF-Maker.git <custom-folder-name>
```

### Option 2
This just involves clicking on the gifmaker.py file and selecting the download icon near the top-right.

## Install External Dependencies

To install dependencies, you can use [PIP](https://packaging.python.org/en/latest/tutorials/installing-packages/) (Python's built-in package manager for external dependencies). If you don't have Python, install it from [here](https://www.python.org/downloads/release/python-31011/).

### Install ImageIO, NumPy, and Pillow using PIP
```
python -m pip install ImageIO numpy pillow
```

## Usage

Using this is simple, the script has three mandatory arguments and one optional one. `<path>` is the location of the folder/compressed folder, `<output>` is the location of the GIF file and the only optional argument, `<duration>` is the time in miliseconds between each frame, and `loop` is the amount of times the GIF should repeat (0 for infinite).  

### Example

```
python gifmaker.py 'Test Images 1' 'GIF Output/MyGif.gif' 60 0
```

## ⚠ Limitations

There are some limitations with regards to the input, that I may or may not address in the future:

* ZIP files are the only type of compressed files allowed,
* Folders with different types of image formats may or may not work,
* Folders must contain only images,
* Depending on the file type, you may need to modify the script by downloading and importing different libraries. ImageIO has a list of supported file types and their respective libraries [here](https://imageio.readthedocs.io/en/stable/formats/index.html).

If there any issues that I missed or a feature you want added, please create an issue and I'll consider fixing/implementing in the future.
