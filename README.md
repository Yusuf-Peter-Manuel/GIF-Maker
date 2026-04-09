# GIF-Maker
A simple Python CLI tool that turns a folder of images into an animated GIF using **ImageIO**.

### Features
- Simple command-line interface.
- Input validation with clear error messages.
- Customizable frame duration and looping.

## Requirements
* Python 3.10+
* ImageIO, NumPy, Pillow 8.3.2+

## Project Installation
Use [Git](https://git-scm.com/install/), or a package manager of your choice, e.g., [WinGet](https://learn.microsoft.com/en-us/windows/package-manager/winget/) for Windows, APT for various Linux Distributions (Debian, Ubuntu, and Linux Mint), and [Brew](https://brew.sh/) for MacOS. 

```
git clone htps://github.com/Yusuf-Peter-Manuel/GIF-Maker.git <custom-folder-name>
```

## Install External Dependencies

To install dependencies, you will need [PIP](https://packaging.python.org/en/latest/tutorials/installing-packages/).

```
python -m pip install ImageIO numpy pillow
```

## Usage

There are three mandatory arguments and one optional one:
- `<path>` is the location of the folder/compressed folder, 
- `<output>` is the location of the GIF file and the only optional argument, 
- `<duration>` is the time in miliseconds between each frame, and 
- `loop` is the amount of times the GIF should repeat (0 for infinite).  

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
