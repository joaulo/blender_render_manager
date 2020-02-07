import os
import json
import pprint
import bpy


# ------------------------------------------------------------------------
#    Operators
# ------------------------------------------------------------------------

class RenderCollectionCamerasImg(bpy.types.Operator):
    """Render Collection Cameras Images"""
    bl_idname = "render.collection_cameras_images"
    bl_label = "Render Collection Cameras Images"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.scene is not None

    def execute(self, context):
        scene = context.scene
        rcc = scene.render_collection_cameras
        print("start rendering cameras in collection:", rcc.collection)
        for cam in [obj for obj in bpy.data.collections[rcc.collection].all_objects if obj.type == 'CAMERA']:
            # scene.camera = cam
            # scene.render.image_settings.engine = 'BLENDER_EEVEE'
            scene.render.image_settings.file_format = 'JPEG'
            # scene.render.image_settings.compression = 96
            scene.render.filepath = os.path.join(rcc.path_dir, cam.name)
            bpy.ops.render.render(write_still=True)
            scene.render.filepath = rcc.path_dir

        return {'FINISHED'}


class RenderCollectionCamerasAnim(bpy.types.Operator):
    """Render Collection Cameras Animations"""
    bl_idname = "render.collection_cameras_animations"
    bl_label = "Render Collection Cameras Animations"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.scene is not None

    def execute(self, context):
        scene = context.scene
        rcc = scene.render_collection_cameras
        print("start rendering cameras in collection:", rcc.collection)
        for cam in [obj for obj in bpy.data.collections[rcc.collection].all_objects if obj.type == 'CAMERA']:
            # scene.camera = cam
            # scene.render.image_settings.engine = 'BLENDER_EEVEE'
            scene.render.image_settings.file_format = 'FFMPEG'
            scene.render.ffmpeg.format = 'MPEG4'
            scene.render.ffmpeg.codec = 'MPEG4'

            scene.render.filepath = os.path.join(rcc.path_dir, cam.name)
            bpy.ops.render.render(animation=True, write_still=False)
            scene.render.filepath = rcc.path_dir

        return {'FINISHED'}


class LoadRenderSettings(bpy.types.Operator):
    """Load render settings previously saved to configuration file"""
    bl_idname = "load.render_settings"
    bl_label = "Load Render Settings"
    bl_options = {'REGISTER'}

    @classmethod
    def poll(cls, context):
        return context.scene is not None

    def execute(self, context):
        print("TODO: load configuration from file and set values to scene")
        scene = context.scene
        with open(scene.render_collection_cameras.load_render_settings, 'r', encoding='utf-8') as f:
            pl = json.load(f)
            pprint.pprint(pl)
            for p, val in pl.items():
                print(p, val)
                setattr(scene.render, p, val)

        return {'FINISHED'}


class SaveRenderSettings(bpy.types.Operator):
    """Save render output settings to configuration file"""
    bl_idname = "save.render_settings"
    bl_label = "Save Render Settings"
    bl_options = {'REGISTER'}

    @classmethod
    def poll(cls, context):
        return context.scene is not None

    def execute(self, context):
        scene = context.scene

        # get properties list
        # p = {sett: getattr(scene.render, sett) for sett in dir(scene.render)}
        pl = {}
        for p in scene.render.bl_rna.properties:
            if p.identifier in {'rna_type', 'stamp_background', 'stamp_foreground'}:
                continue
            if p.is_readonly:
                continue
            print(p)
            pl[p.identifier] = getattr(scene.render, p.identifier)

        pprint.pprint(pl)

        with open(scene.render_collection_cameras.save_render_settings, 'w', encoding='utf-8') as f:
            json.dump(pl, f, ensure_ascii=False, indent=4)

        return {'FINISHED'}


classes = (
    RenderCollectionCamerasImg,
    RenderCollectionCamerasAnim,
    LoadRenderSettings,
    SaveRenderSettings,
)
