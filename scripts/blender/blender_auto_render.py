import bpy

# Set render settings
bpy.context.scene.render.engine = 'BLENDER_EEVEE_NEXT'  # Use 'CYCLES' if you prefer that render engine
bpy.context.scene.render.image_settings.file_format = 'PNG'
bpy.context.scene.render.image_settings.color_mode = 'RGBA'  # For transparency

# Define output directory
output_dir = "output_directory"

# List of target collections for rendering
target_collections = [str(i) for i in range(1, 5)]

# Iterate over each target collection
for collection_name in target_collections:
    collection = bpy.data.collections.get(collection_name)
    
    if collection:
        for obj in collection.objects:
            if obj.type == 'MESH':  # Render only mesh objects
                # Hide all objects in the scene except those in the "Collection"
                for other_obj in bpy.context.scene.objects:
                    if "Collection" in [coll.name for coll in other_obj.users_collection]:
                        other_obj.hide_render = False  # Keep lights, etc., visible
                    else:
                        other_obj.hide_render = True   # Hide all other objects

                # Unhide the current object to be rendered
                obj.hide_render = False

                # Turn film transparency ON
                bpy.context.scene.render.film_transparent = True

                # Set the output file path
                bpy.context.scene.render.filepath = f"{output_dir}{obj.name}.png"

                # Render the image
                bpy.ops.render.render(write_still=True)

                # Turn film transparency OFF after rendering
                bpy.context.scene.render.film_transparent = False

                # Re-hide the object after rendering
                obj.hide_render = True