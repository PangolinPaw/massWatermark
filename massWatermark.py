from PIL import Image, ImageDraw, ImageFont
import os

def addWatermark(image_name, text):
    try:
        image = Image.open(image_name)
        width, height = image.size
         
        draw = ImageDraw.Draw(image)
         
        font = ImageFont.truetype('arial.ttf', 12)
        textwidth, textheight = draw.textsize(text, font)
         
        # calculate the x,y coordinates of the text
        margin = 5
        x = width - textwidth - margin
        y = height - textheight - margin
         
        # draw watermark in the bottom right corner
        draw.text((x, y), text, font=font)
        
        # save watermarked copy
        if not os.path.exists('watermarked'):
            os.makedirs('watermarked')
        try:
            # Windows
            new_image_name = 'watermarked\\{}'.format(image_name.split("\\")[-1])
            image.save(new_image_name)
        except:
            # Mac
            new_image_name = 'watermarked/{}'.format(image_name.split("/")[-1])
            image.save(new_image_name)
        return True
    except:
        return False

def listFiles(suffix):
    file_list = []
    this_dir = os.getcwd()
    for f in os.listdir(this_dir):
        if f.endswith(suffix):
            file_list.append(os.path.join(this_dir, f))
    return file_list

def main():
    print """
 ==================================================
 Batch Watermark                               v1.0
 ==================================================
 This script will apply a watermark to all images 
 in the current directory.
 --------------------------------------------------"""
    print """ 
 What extention do the image files have (e.g. png)?"""
    suffix = raw_input(" > ")
    file_list = listFiles(suffix)
    print " {} file(s) found".format(len(file_list))
    print """
 What should the watermark say (ASCII characters only)?"""
    watermark = raw_input(" > ")

    print """
 Apply the watermark above to the {} file(s)? [Y/N]""".format(len(file_list))
    confirm = raw_input(" > ")
    if confirm.upper() == "Y":
        print """
 Processing, please wait..."""
        success_count = 0
        for f in file_list:
            success = addWatermark(f, watermark)
            if success:
                success_count = success_count + 1
        print """ Process complete. {} of {} files changed.""".format(success_count, len(file_list))
    else:
        print """
 Process cancelled. 0 files changed."""


if __name__ == '__main__':
    main()
    x = raw_input("\n Press Enter to close.")
