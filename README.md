# massWatermark
Apply a text-based watermark to all images in the current directory.

## Installation (Mac)
1. Download this repo
2. Navigate to the download destination via the Terminal (`cd path/to/directory`)
3. Install pip by entering `sudo easy_install pip` into the Terminal
4. Install all the requirements by entering `pip install -r requirements.txt` into the Terminal

## Usage
1. Place the script in the same directory as the images that need to be watermarked
2. Navigate to that directroy via the Terminal (`cd path/to/directory`)
3. Run the script by entering `python massWatermark.py` into the Terminal
4. Follow the on-screen instructions
5. A watermarked copy of every will be made in a subdirectory named 'watermark'

## Notes
This script is intended only for image files (e.g. .png, .jpg) and the watermark is limited to ASCII characters only.
