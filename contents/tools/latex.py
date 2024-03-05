# # import re
import os
import glob
# # # pip install pillow
# # from PIL import Image, ImageDraw, ImageFont
# # #  pip install  pyperclip
# # import pyperclip
 
def format(file):
    print("🚀 Giá trị của file:", file)


root = r"../../"
tex_files = glob.glob(os.path.join(root, "**/*.tex"), recursive=True)
for i in tex_files:

    format(i)

 

        # with open(path, 'r', encoding="utf-8") as file:
        #     contents = file.read()