from PIL import Image, ImageDraw, ImageFont
from tkinter import filedialog as fd
import tkinter as tk
import os


SOURCE_DIRECTORY = "Users/nurayahmadova/Desktop"
TARGET_DIRECTORY = "Users/nurayahmadova/Desktop"


def add_watermark():
    filename = fd.askopenfilename(initialdir=SOURCE_DIRECTORY, title="Select A File")
    filetypes = [
            ("All Files", "*.*"),
            ("Python File", "*.py"),
            ("Image File", "*.bmp"),
            ]

    # Creates an image object
    opened_image = Image.open(filename)

    # Get image size
    image_width, image_height = opened_image.size

    # Draw on image
    draw = ImageDraw.Draw(opened_image)

    # Specify a font size and name
    font_size = int(image_width / 8)  # good ratio for around 10 characters
    font = ImageFont.truetype('Arial.ttf', font_size)

    # Coordinates for where we want the text on the image
    x, y = int(image_width/2), int(image_height/2)

    # Add the watermark
    wm_text = "Nuray"
    draw.text((x, y), wm_text, font=font, fill='#FFF', stroke_width=5, stroke_fill='#222', anchor='ms')

    # Show the new image
    opened_image.show()

    # Save watermarked image
    # finished_img_name = filename[:-4] + " WM.jpg"
    opened_image.save("filename[:-4] + 'WM', png")


root = tk.Tk()
root.title("Image_Watermarking_App")
root.geometry("400x400")

instruction_label = tk.Label(root, text="Select photo to watermark.", font="Ariel")
instruction_label.place(x=100, y=120)


browse_text = tk.StringVar()
browse_btn = tk.Button(root, command=add_watermark, textvariable=browse_text, font="Ariel", bg="black",
                       fg="black", height=2, width=15)
browse_text.set("Browse")
browse_btn.place(x=100, y=160)

root.mainloop()
