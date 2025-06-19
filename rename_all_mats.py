'''
rename all materials to project's name + models's name + iterator
e.g. Material01 -> [Project] (Cube01) 0
i.e. to avoid duplicated materials if materials unpacked from fbxs which exported from multiple blender projects
'''
import bpy
from pathlib import Path

fpath = bpy.data.filepath
fname = Path(fpath).stem

def rename_materials_unique(fname=fname):
    count_renamed = 0
    for obj in bpy.data.objects:
        i = 0
        if obj.type == 'MESH':
            for slot in obj.material_slots:
                if slot.material:
                    mat = slot.material
                    project_name = f"[{fname}]"
                    model_name = f"({obj.name})"
                    expect_name = " ".join([project_name,model_name,str(i)])
                    
                    i += 1
                    if not mat.name == expect_name:
                        mat.name = expect_name
                        
        count_renamed += i
        
    print(f"Project: {fname} got {count_renamed} mats renamed")


rename_materials_unique()
bpy.ops.wm.save_mainfile()    