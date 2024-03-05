# import re
import os
import glob
# # pip install pillow
# from PIL import Image, ImageDraw, ImageFont
# #  pip install  pyperclip
# import pyperclip


# def chen_van_ban_vao_anh(duong_dan_anh):
#     anh = Image.open(duong_dan_anh)
#     draw = ImageDraw.Draw(anh)
#     font = ImageFont.truetype("arial.ttf", 100)
#     draw.text((0, 0), "Vũ Văn Nghĩa 20206205", fill=(255, 255, 5), font=font)
#     anh.save(duong_dan_anh)


root = r"C:\Users\vvn20206205\Desktop\20232\Datawarehouse"
tex_files = glob.glob(os.path.join(root, "**/*.tex"), recursive=True)
for i in tex_files:
    print("🚀 Giá trị của i:", i)
    # chen_van_ban_vao_anh(i)



# đổi tên bỏ đi image