'''
Append a prefix to all Image Assets
for example 'Image01.png' -> 'New_Image01.png'
'''
import bpy
import os

# set your prefix to append on images name
PREFIX = ""

# optional: change paths for images to unpack
def update_unpack_paths(img, new_name):
    filename = new_name + ".png"  # 默认扩展名
    if img.file_format == 'JPEG':
        filename = new_name + ".jpg"
    elif img.file_format == 'TARGA':
        filename = new_name + ".tga"
    elif img.file_format == 'TIFF':
        filename = new_name + ".tif"
    elif img.file_format == 'WEBP':
        filename = new_name + ".webp"
    # ... TODO extend if needed

    img.filepath_raw = "//textures/" + filename  # path for images unpacked to

for img in bpy.data.images:
    if img.packed_file is not None:
        old_name = img.name
        idx = old_name.find("_")
        suffix = old_name[idx:] if idx != -1 else old_name
        new_name = PREFIX + old_name[old_name.find("_"):]
        
        # avoid dupilicated rename
        if img.name.startswith(PREFIX):
            print(f"🔁 Skipped rename for {img.name}, as it already has your prefix")
            continue

        # rename
        img.name = new_name
        print(f"✅ Renamed: {old_name} -> {new_name}")
        
        # TODO optional functions
        update_unpack_paths(img=img, new_name=new_name)

bpy.ops.wm.save_mainfile()