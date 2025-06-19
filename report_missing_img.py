# report missing image source
import bpy
import os

missing = []

print("🔍 Checking for missing textures...")

for image in bpy.data.images:
    if image.source != 'FILE':
        continue

    path = bpy.path.abspath(image.filepath)
    if not os.path.exists(path):
        print(f"Missing: {image.name} → {path}")
        missing.append((image.name, path))

if not missing:
    print("✅ All textures are found.")
else:
    print(f"⚠️ Total missing: {len(missing)}")
