'''
clear materials in every slot for selected object
i.e. pre-processing for baking Google tiles in order to get the tile mapped with single texture instead of enormous materials and textures
'''
import bpy

obj = bpy.context

for i in range(0,len(obj.object.material_slots)):
    obj.object.active_material_index = 1
    bpy.ops.object.material_slot_remove()
    
bpy.ops.object.mode_set(mode = 'EDIT')
bpy.ops.mesh.select_all(action = 'SELECT')
bpy.ops.object.material_slot_assign()
bpy.ops.object.mode_set(mode = 'OBJECT')
