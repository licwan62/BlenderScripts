import os
import subprocess
from pathlib import Path

# Refer to your own blender executive path
BLENDER_PATH = Path(r"C:\Program Files\Blender Foundation\Blender 4.4\blender.exe")
# Refer to path where all project files to be processed
TARGET_DIR = Path(r"Hamilton Simulator/blenders")
# Python script's path for batch script to run at
SCRIPT_PATH = Path(r"C:\Users\hzwlc\OneDrive\ONENOTE\Blender\export_fbx.py")

for filename in os.listdir(TARGET_DIR):
    if filename.endswith(".blend"):
        filepath = TARGET_DIR / filename
        print(f"\n🔧 Processing: {filepath}")

        result = subprocess.run([
            BLENDER_PATH,
            filepath,
            "--background",
            "--python", 
            SCRIPT_PATH
        ], capture_output=True, text=True, encoding="utf-8")
        
        print(result.stdout)
        if result.stderr:
            print("⚠️ Error:", result.stderr)