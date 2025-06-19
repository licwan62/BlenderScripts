'''
Report all image assets' stats and link states.

For each image, report:
    1. Physical path
    2. Unpacking path (if different from physical path)
    3. Packed or not
    4. Memory size
    5. Missing or not
    6. Used materials
'''

import bpy
import os

# Skip assets with resolution (smaller dimension) lower than this
SKIP_RESO = 0

def get_img_filesize(img: bpy.types.Image): 
    """Get image file size from disk or packed data."""
    if img.packed_file is not None:
        return img.packed_file.size
    
    img_path = os.path.abspath(bpy.path.abspath(img.filepath))
    
    if not os.path.exists(img_path):
        print(f"⚠️ File not found: {img_path}")
        return 0
    
    try:
        return os.path.getsize(img_path)
    except Exception as e:
        print(f"❌ Failed to get file size: {img.name}, error: {e}")
        return 0

def find_used_materials(img: bpy.types.Image):
    """Find which materials are using this image."""
    used_in_materials = []
    for mat in bpy.data.materials:
        if not mat.use_nodes:
            continue
        for node in mat.node_tree.nodes:
            if node.type == 'TEX_IMAGE' and node.image == img:
                used_in_materials.append(mat.name)
    return used_in_materials

# Start reporting
print("\n=== Image Assets Report ===\n")

total_mem, count, packed, packed_mem = 0, 0, 0, 0
small_img_count = 0

for img in bpy.data.images:
    w, h = img.size

    if max(w, h) <= SKIP_RESO:
        small_img_count += 1
        continue

    mem = get_img_filesize(img)
    is_packed = img.packed_file is not None
    filepath = bpy.path.abspath(img.filepath)
    file_exists = os.path.exists(filepath)
    used_materials = find_used_materials(img)

    # Per-image report
    print(f"\n📄 Image: {img.name} ({img.file_format})")
    print(f"    Resolution: {w}x{h}")
    print(f"    Memory Size: {mem / 1024:.2f} KB")
    print(f"    Packed: {'✅ Yes' if is_packed else '❌ No'}")
    print(f"    File Path: {filepath}")
    if filepath != img.filepath_raw:
        print(f"    Unpacking Path: {img.filepath_raw}")
    print(f"    File Exists: {'✅ Yes' if file_exists else '❌ No'}")
    print(f"    Used in Materials: {used_materials if used_materials else '🚫 None'}")

    count += 1
    if is_packed:
        packed += 1
        packed_mem += mem
    total_mem += mem

# Summary
print("\n=== Overall Summary ===")
print(f"Total Images: {count}")
print(f"Packed Images: {packed}")
print(f"Skipped Low-res Images (<{SKIP_RESO}): {small_img_count}")
print(f"Total Memory: {total_mem / (1024 ** 2):.2f} MB")
print(f"Packed Memory: {packed_mem / (1024 ** 2):.2f} MB")
