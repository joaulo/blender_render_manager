import bpy

# Frame Settings
bpy.context.scene.frame_start
bpy.context.scene.frame_end
bpy.context.scene.frame_step
# Render Settings
bpy.context.scene.render.resolution_x
bpy.context.scene.render.resolution_y
bpy.context.scene.render.resolution_percentage
bpy.context.scene.render.fps
bpy.context.scene.render.filepath
# Image Settings
bpy.context.scene.render.image_settings.file_format
bpy.context.scene.render.image_settings.quality
# Ffmpeg Settings
bpy.context.scene.render.ffmpeg.format
bpy.context.scene.render.ffmpeg.codec
bpy.context.scene.render.ffmpeg.constant_rate_factor
bpy.context.scene.render.ffmpeg.ffmpeg_preset
bpy.context.scene.render.ffmpeg.gopsize
