'''
resturcture all shaders to Principled BSDF
i.e. Google tiles by default get mix shader that unable to export with fbx, so their materials'shaders to be modified before exporting
'''

import bpy

processed_objects = 0
skipped_objects = 0
processed_materials = set()

# 遍历所有对象
for obj in bpy.data.objects:
    if obj.type == 'MESH' and obj.material_slots:
        for slot in obj.material_slots:
            material = slot.material
            if material and material.use_nodes:
                # 跳过已处理的材质
                if material.name in processed_materials:
                    continue

                # 判断材质是否已经满足条件（TEX_IMAGE -> Base Color）
                already_valid = False
                for node in material.node_tree.nodes:
                    if node.type == 'BSDF_PRINCIPLED':
                        base_color_input = node.inputs['Base Color']
                        if base_color_input.is_linked:
                            from_node = base_color_input.links[0].from_node
                            if from_node.type == 'TEX_IMAGE':
                                already_valid = True
                                break

                if already_valid:
                    skipped_objects += 1
                    print(f"Skipped object: {obj.name}, material: {material.name} (already valid)")
                    continue

                # 创建新材质
                new_material = bpy.data.materials.new(name=f"New_{material.name}")
                new_material.use_nodes = True
                new_nodes = new_material.node_tree.nodes
                new_links = new_material.node_tree.links

                # 清空默认节点
                for node in new_nodes:
                    new_nodes.remove(node)

                # 创建新节点
                bsdf = new_nodes.new(type='ShaderNodeBsdfPrincipled')
                bsdf.location = (0, 0)
                output = new_nodes.new(type='ShaderNodeOutputMaterial')
                output.location = (300, 0)
                new_links.new(bsdf.outputs['BSDF'], output.inputs['Surface'])

                # 查找贴图
                for node in material.node_tree.nodes:
                    if node.type == 'TEX_IMAGE' and node.image:
                        tex = new_nodes.new('ShaderNodeTexImage')
                        tex.image = node.image
                        tex.location = (-300, 0)
                        new_links.new(tex.outputs['Color'], bsdf.inputs['Base Color'])
                        break

                slot.material = new_material
                processed_materials.add(material.name)
                processed_objects += 1
                print(f"Processed object: {obj.name}, material: {material.name} -> {new_material.name}")

print(f"\n✅ Done. Total processed objects: {processed_objects}, skipped: {skipped_objects}")
bpy.ops.wm.save_mainfile()
