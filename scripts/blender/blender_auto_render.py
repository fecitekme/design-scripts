import bpy

# Set render settings
bpy.context.scene.render.engine = 'CYCLES'  # or 'EEVEE'
bpy.context.scene.render.image_settings.file_format = 'PNG'
bpy.context.scene.render.image_settings.color_mode = 'RGBA'  # For transparency

# Define output directory
output_dir = "file_path"

# List of target collections for rendering
target_collections = [str(i) for i in range(2, 21)]

# Iterate over each target collection
for collection_name in target_collections:
    collection = bpy.data.collections.get(collection_name)
    
    if collection:
        for obj in collection.objects:
            if obj.type == 'MESH':  # Assuming all your objects are meshes
                # Hide all objects in the scene except those in the "Collection"
                for other_obj in bpy.context.scene.objects:
                    # Check if the object belongs to the "Collection" collection
                    if "Collection" in [coll.name for coll in other_obj.users_collection]:
                        other_obj.hide_render = False
                    else:
                        other_obj.hide_render = True

                # Unhide the current object
                obj.hide_render = False

                # Set the output path
                bpy.context.scene.render.filepath = f"{output_dir}{obj.name}.png"

                # Render the image
                bpy.ops.render.render(write_still=True)

                # Re-hide the object after rendering
                obj.hide_render = True
