import os
import json
import pprint
import bpy


# ------------------------------------------------------------------------
#    Operators
# ------------------------------------------------------------------------

class RenderManagerImg(bpy.types.Operator):
    """Render Manager::Images"""
    bl_idname = "render.manage_images"
    bl_label = "Render Manager::Images"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.scene is not None

    def execute(self, context):
        scene = context.scene
        render_manager = scene.render_manager
        print("start rendering cameras in collection:", render_manager.collection)
        for cam in [obj for obj in bpy.data.collections[render_manager.collection].all_objects if obj.type == 'CAMERA']:
            scene.camera = cam
            # scene.render.image_settings.engine = 'BLENDER_EEVEE'
            # scene.render.image_settings.file_format = 'JPEG'
            # scene.render.image_settings.compression = 96
            scene.render.filepath = os.path.join(render_manager.path_dir, cam.name)
            bpy.ops.render.render(write_still=True)
            scene.render.filepath = render_manager.path_dir

        return {'FINISHED'}


class RenderManagerAnim(bpy.types.Operator):
    """Render Manager::Animations"""
    bl_idname = "render.manage_animations"
    bl_label = "Render Manager::Animations"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.scene is not None

    def execute(self, context):
        scene = context.scene
        render_manager = scene.render_manager
        print("start rendering cameras in collection:", render_manager.collection)
        for cam in [obj for obj in bpy.data.collections[render_manager.collection].all_objects if obj.type == 'CAMERA']:
            scene.camera = cam
            # scene.render.image_settings.engine = 'BLENDER_EEVEE'
            # scene.render.image_settings.file_format = 'FFMPEG'
            # scene.render.ffmpeg.format = 'MPEG4'
            # scene.render.ffmpeg.codec = 'H264'

            scene.render.filepath = os.path.join(render_manager.path_dir, cam.name)
            bpy.ops.render.render(animation=True, write_still=False)
            scene.render.filepath = render_manager.path_dir

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
        print("load configuration from file and set values to scene")
        scene = context.scene
        with open(scene.render_manager.load_render_settings, 'r', encoding='utf-8') as f:
            pl = json.load(f)
            pprint.pprint(pl)
            for section, plist in pl.items():
                # print(section)
                if section == 'render':
                    print('loading render params...')
                    for p, val in plist.items():
                        # print(p, val)
                        setattr(scene.render, p, val)
                elif section == 'image_settings':
                    print('loading image_settings...')
                    for p, val in plist.items():
                        # print(p, val)
                        setattr(scene.render.image_settings, p, val)
                elif section == 'ffmpeg':
                    print('loading ffmpeg...')
                    for p, val in plist.items():
                        # print(p, val)
                        setattr(scene.render.ffmpeg, p, val)
                elif section == 'frames':
                    print('loading frames...')
                    for p, val in plist.items():
                        # print(p, val)
                        setattr(scene, p, val)
        print('loading completed')
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
        print('-> save render settings to file:', scene.render_manager.save_render_settings)

        # get properties list
        # p = {sett: getattr(scene.render, sett) for sett in dir(scene.render)}
        pl = {}
        # container for render settings
        pl['render'] = {}
        print('reading render settings...')
        for p in scene.render.bl_rna.properties:
            if p.identifier in {'rna_type', 'stamp_background', 'stamp_foreground'}:
                continue
            if p.is_readonly:
                continue
            pl['render'][p.identifier] = getattr(scene.render, p.identifier)
        # container for image settings specific to still images rendering
        pl['image_settings'] = {}
        print('reading image settings...')
        for p in scene.render.image_settings.bl_rna.properties:
            if p.is_readonly:
                continue
            # print(p)
            pl['image_settings'][p.identifier] = getattr(scene.render.image_settings, p.identifier)
        # container for ffmpeg settings specific to animation rendering
        pl['ffmpeg'] = {}
        print('reading ffmpeg settings...')
        for p in scene.render.ffmpeg.bl_rna.properties:
            if p.is_readonly:
                continue
            # print(p)
            pl['ffmpeg'][p.identifier] = getattr(scene.render.ffmpeg, p.identifier)
        # container for frames settinga specific to animation rendering
        pl['frames'] = {}
        print('reading animation frames settings...')
        pl['frames']['frame_start'] = getattr(scene, 'frame_start')
        pl['frames']['frame_end'] = getattr(scene, 'frame_end')
        pl['frames']['frame_step'] = getattr(scene, 'frame_step')

        # pprint.pprint(pl)

        with open(scene.render_manager.save_render_settings, 'w', encoding='utf-8') as f:
            json.dump(pl, f, ensure_ascii=False, indent=4)

        print('saving completed')
        return {'FINISHED'}


classes = (
    RenderManagerImg,
    RenderManagerAnim,
    LoadRenderSettings,
    SaveRenderSettings,
)
