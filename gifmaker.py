import argparse as ap
import glob
import shutil
import os
import imageio.v3 as iio

def main():
    # CLI Options
    parser = ap.ArgumentParser(description="Turn a set of images from a folder into a GIF file.")
    parser.add_argument("path", type=str, help="Path to the folder that holds the images.")
    parser.add_argument("--output", type=str, help="Path (including name) to output the GIF to.")
    parser.add_argument("duration", type=int, help="The time in milliseconds between each frame.")
    parser.add_argument("loop", type=int, help="The amount of times the GIF will loop for (0 for infinite).")
    args = parser.parse_args()

    # Path of .zip File and Output File
    target_folder, output_folder = args.path, args.output # default output to current directory

    # Verification/Validation of Command-Line Arguments
    # Verify if Path Exists
    if not os.path.exists(target_folder):
        # If it fails Supplied Path then could lead to a ZIP File then, so Verify
        if os.path.isfile(target_folder + ".zip") == True:
            target_folder = target_folder + ".zip"
        # Path doesn't lead to either a Folder or a ZIP file
        else:
            raise SystemExit(f"'{target_folder}' folder or ZIP file cannot be found.")

    # Set a Default Name for the Output Folder if not Provided
    if output_folder == None:
        output_folder = os.path.join(os.path.splitext(target_folder)[0] + ".gif")
    # Create Output Folder if it doesn't already Exist
    elif os.path.exists(output_folder) == False:
        os.mkdir(os.path.dirname(output_folder))
    else:
        pass

    # Duration & Loop Values are handled by Parser ^

    # (Unzip Folder)
    if os.path.splitext(target_folder)[1] == ".zip":
        # Attempt to Unpack Archive
        try:
            shutil.unpack_archive(target_folder, os.path.splitext(target_folder)[0]) # uncompress the.zip file and store it in the same location (with the same name)
            print(f"Archive '{target_folder}' unpacked successfully to '{os.path.splitext(target_folder)[0]}'.")
        except shutil.ReadError as sre:
            raise SystemExit(f"Archive '{target_folder}' is not a valid archive. '{sre}'")
        except Exception as e:
            raise SystemExit(f"An unknown error occurred. '{e}'")

    # Add all Image Names into a List
    image_names = sorted(glob.glob(os.path.splitext(target_folder)[0] + "/*")) # remove possible extension in case one was supplied, e.g., (.zip)

    # Load Images into List
    images = []
    # Folder or Uncompressed Folder must ONLY contain images
    try:
        for name in image_names:
            images.append(iio.imread(name)) # e.g., JPEG/JPG, PNG, WEBG. Refer to ImageIO's documentation for supported file types, some may require additional libraries
    except Exception as e:
        raise SystemExit(f"Folder or Uncompressed Folder can only have images in it. \nFull Message:\n'{e}'")

    # Create GIF
    print("Creating GIF...")
    iio.imwrite(output_folder, images, duration = args.duration, loop = args.loop)
    print("DONE.")

if __name__ == "__main__":
    main()