import bpy
import os

# 导出当前场景内所有顶层物体
def export_current_top_level_objects():
    view_layer_objects = set(bpy.context.view_layer.objects)

    # 找出所有没有父物体的对象
    top_level_objects = [
        obj for obj in bpy.context.scene.objects 
        if obj.parent is None 
        and obj.type not in {'CAMERA', 'LIGHT'}
        and obj in view_layer_objects  # 只处理能被当前 ViewLayer 访问的物体
    ]

    count = 0
    # 导出每一个父物体 + 它的子物体
    for parent_obj in top_level_objects:
        # 选中这个父物体及其所有子物体
        bpy.ops.object.select_all(action='DESELECT')
        parent_obj.select_set(True)
        
        # 获取所有子对象并选中
        for child in parent_obj.children_recursive:
            if child in view_layer_objects:
                child.select_set(True)

        # 设置激活对象为父物体
        bpy.context.view_layer.objects.active = parent_obj
        
        # 设定导出路径
        export_path = os.path.join(export_dir, f"{parent_obj.name}.fbx")
        
        # 执行 FBX 导出
        bpy.ops.export_scene.fbx(
            filepath=export_path,
            use_selection=True,
            apply_unit_scale=True,
            bake_space_transform=True,
            object_types={'MESH', 'EMPTY'},
            mesh_smooth_type='OFF',
            axis_up='Z',
            global_scale=10.0,
            
            path_mode='COPY',          # 复制贴图文件
            embed_textures=False,      # false:不嵌入贴图：会生成 .fbm 文件夹
        )

        count += 1
    return count

# 设置导出目录
export_dir = bpy.path.abspath("//fbx_exports/")
if not os.path.exists(export_dir):
    os.makedirs(export_dir)
    
scenes_skip_export = []

exported = 0
for scene in bpy.data.scenes:
    if scene.name in scenes_skip_export: 
        continue  # 跳过在跳过列表中的场景
    
    bpy.context.window.scene = scene  # 切换到目标场景
    exported += export_current_top_level_objects()

print(f"export {exported} objects")