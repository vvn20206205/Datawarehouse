import re
import os
import glob
# pip install pillow
from PIL import Image, ImageDraw, ImageFont
#  pip install  pyperclip
import pyperclip


def chen_van_ban_vao_anh(duong_dan_anh):
    anh = Image.open(duong_dan_anh)
    draw = ImageDraw.Draw(anh)
    font = ImageFont.truetype("arial.ttf", 100)
    draw.text((0, 0), "Vũ Văn Nghĩa 20206205", fill=(255, 255, 5), font=font)
    anh.save(duong_dan_anh)


root = r"C:\Users\vvn20206205\Desktop\20232\Datawarehouse"
png_files = glob.glob(os.path.join(root, "**/*.png"), recursive=True)
for i in png_files:
    chen_van_ban_vao_anh(i)



# noi_dung = pyperclip.paste()
# pattern = r'\{(.*?)\}'
# noi_dung_trong_ngoac = re.findall(pattern, noi_dung)
# print(noi_dung_trong_ngoac[0])
