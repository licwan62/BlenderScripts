## Workflow: From BLOSM Setup to Unity Export

   This guide outlines the workflow for importing BLOSM map tiles, baking assets, modeling building facades, and exporting them to Unity. The process includes texture management, shader conversion, and batch automation for large-scale Blender projects.

------

   ### 1. Set Up BLOSM (API for Generating Basic Map Tiles)

   1. Download BLOSM from the official GitHub repository: https://github.com/vvoovv/blosm
   2. Install and configure BLOSM in your Blender project
   3. Import map tiles into the scene

------

   ### 2. Bake and Convert Tiles for Proper Rendering

   To prepare tiles for efficient rendering and export:

   1. **Bake multiple textures into an atlas**
      - Improves performance and simplifies asset management
   2. **Convert shaders to Principled BSDF** (required for exporting)
      - Use the script [`mod_shaders_to_principledbsdf.py`](https://github.com/licwan62/BlenderScripts/blob/master/mod_shaders_to_principledbsdf.py)
   3. **(Optional)** Unpack image assets
      - Allows Blender to reference external image files (with reduced .blend file size)

------

   ### 3. Create Textures for Building Facades

   1. Capture reference images from Google Maps or Google Earth

   2. Edit and organize images into a texture atlas

      - Correct **perspective distortion** to ensure realism in UV mapping

      - A single building may require multiple textures

------

   ### 4. Model Building Facades in Blender

   1. Create materials using the prepared textures
   2. Model the facades and ensure proper UV unwrapping for each surface

------

   ### 5. Clean Up Unnecessary Meshes

   Remove outliers and unwanted meshes to optimize the scene

------

   ### 6. Export to Unity via FBX

   1. Export models as FBX files
   2. **(Optional)** Automate batch FBX export using [`export_fbx.py`](https://github.com/licwan62/BlenderScripts/blob/master/export_fbx.py)
      - Ideal for exporting all top-level objects in a scene

------

   ### 7. (Optional) Run Scripts Across Multiple Blender Projects

   To save time when managing numerous `.blend` files (e.g., applying a shader fix or exporting FBX):

   1. Use the batch automation script [`batch.py`](https://github.com/licwan62/BlenderScripts/blob/master/batch.py)
   2. Before running the script, configure:
      - Path to the Blender executable
      - Directory containing all Blender project files
      - Target script path to be executed for each project