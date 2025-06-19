import bpy
import os

# 指定解包目录，相对于 .blend 文件路径
TARGET_DIR_NAME = "textures"

# 获取当前 .blend 文件所在目录
blend_dir = os.path.dirname(bpy.data.filepath)
target_dir = os.path.join(blend_dir, TARGET_DIR_NAME)

# 确保目标文件夹存在
os.makedirs(target_dir, exist_ok=True)

# 遍历并解包图像
for img in bpy.data.images:
    if img.packed_file is None:
        print(f"{img.name} is unpacked on {img.filepath_raw}:")
        continue
    
    try:
        # 设置新路径（以图像名为文件名）
        filename = bpy.path.basename(img.filepath_raw)
        new_path = os.path.join(target_dir, filename)
        
        # 写入文件
        img.filepath_raw = new_path  # 设置导出路径
        img.unpack(method='WRITE_LOCAL')  # 解包到 filepath_raw 指定位置
        
        print(f"✅ Unpacked: {img.name} -> {new_path}")
    except Exception as e:
        print(f"❌ Failed to unpack {img.name}: {e}")

bpy.ops.wm.save_mainfile()    
        

