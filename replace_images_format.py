'''
update all image assets to the new extension if they have been converted
i.e. sync the extendion changes on physical image sources with blender assets
e.g. Image01.png -> Image01.webp
'''
import bpy
import os

NEW_EXT = '.png'

count = 0
for image in bpy.data.images:
    if image.filepath:
        original_path = bpy.path.abspath(image.filepath)
        dir_name = os.path.dirname(original_path)
        base_name = os.path.splitext(os.path.basename(original_path))[0]
        new_path = os.path.join(dir_name, base_name + NEW_EXT)

        if os.path.exists(new_path):
            print(f"🔁 Replacing {image.filepath} ➜ {new_path}")
            image.filepath = bpy.path.relpath(new_path)
            count += 1
        else:
            print(f"❌ {NEW_EXT} not found for: {original_path}")

print(f"✅ Done. Replaced {count} image to {NEW_EXT}")

bpy.ops.wm.save_mainfile()
