import bpy
import os
import re

filepath = bpy.data.filepath  # 完整路径
filename = os.path.basename(filepath)  # 只提取文件名
project_name = os.path.splitext(filename)[0]  # 去掉扩展名
print("Project name:", filepath)

def remove_dupl_prefixes(orig_name, pref="New_"):
    new_name = re.sub(rf'({pref})+', pref, orig_name)
    if new_name != orig_name:
        print(f'Material: {orig_name} renamed to {new_name}')
    return new_name

def new_name(original_name):
    idx = original_name.find("_")
    if idx == -1:
        return original_name
    else:
        return f"{project_name}{original_name[idx:]}"

for obj in bpy.data.objects:
    if obj.type == 'MESH':
        for slot in obj.material_slots:
            if slot.material:
                original_name = slot.material.name
                material = slot.material
                material.name = new_name(original_name)
                
                # TODO optional: whether to remove duplicated prefix e.g. New_New_Material01 -> Material01
                # material.name = remove_dupl_prefixes(original_name)
                
                
                print(f"RENAME DONE! {obj.name}: {original_name} -> {material.name}")
                
                
bpy.ops.wm.save_mainfile()
