import bpy

DECIMATE_RATIO = 0.5  # 减面比例，比如 0.5 表示减半
GREAT_VERT_COUNT = 1000 # 对顶点数大于该数的网格减面
SKIP_OBJECTS = [] # 对列表物体名的物体跳过减面

for obj in bpy.data.objects:
    if obj.type == 'MESH':
        mesh = obj.data
        vert_count = len(mesh.vertices)

        if vert_count > GREAT_VERT_COUNT and obj.name not in SKIP_OBJECTS:
            # 检查是否已有 AutoDecimate
            if not any(mod.type == 'DECIMATE' and mod.name == 'AutoDecimate' for mod in obj.modifiers):
                decimate = obj.modifiers.new(name='AutoDecimate', type='DECIMATE')
                decimate.ratio = DECIMATE_RATIO
            else:
                print(f"  {obj.name} already has AutoDecimate modifier.")
                continue
            
            bpy.context.view_layer.objects.active = obj
            bpy.ops.object.modifier_apply(modifier='AutoDecimate')
            
            print(f"Object: {obj.name}, Vertices: {vert_count} -> Applying Decimate ({DECIMATE_RATIO}), Vertices After: {len(mesh.vertices)}")

bpy.ops.wm.save_mainfile()
