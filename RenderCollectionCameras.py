bl_info = {
    "name": "Render Collection Cameras",
    "description": "Render all the cameras in a selected collection",
    "author": "joaulo",
    "version": (1, 0, 0),
    "blender": (2, 80, 0),
    "location": "3D View > RCCT",
    "warning": "", # used for warning icon and text in addons panel
    "wiki_url": "",
    "tracker_url": "",
    "category": "Render",
}

import bpy
from bpy.props import (StringProperty,
                       IntProperty,
                       CollectionProperty,
                       PointerProperty,
                       )
from bpy.types import (Panel,
                       Operator,
                       Menu,
                       Scene,
                       PropertyGroup,
                       )
import os


# ------------------------------------------------------------------------
#    Render Properties
# ------------------------------------------------------------------------

class RenderCollectionCamerasProperties(PropertyGroup):

    path_dir: StringProperty(
                            name = "Directory",
                            description="Choose a directory:",
                            default="",
                            maxlen=1024,
                            subtype='DIR_PATH'
                            )
                            
    collection: StringProperty(
                            name = "Collection",
                            description="Choose a collection:",
                            default="",
                            )
    
    start_frame: IntProperty(
                            name="Start Frame",
                            description="Start Frame:",
                            default=1,
                            min=1
                            )
    
    end_frame: IntProperty(
                            name="End Frame",
                            description="End Frame:",
                            default=100,
                            min=1
                            )
    

# ------------------------------------------------------------------------
#    Operators
# ------------------------------------------------------------------------

class RenderCollectionCamerasImg(Operator):
    """Render Collection Cameras Images"""
    bl_idname = "render.collection_cameras_images"
    bl_label = "Render Collection Cameras Images"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        scene = context.scene
        rcct = scene.rcct
        print("start rendering cameras in collection:", rcct.collection)
        for cam in [obj for obj in bpy.data.collections[rcct.collection].all_objects if obj.type == 'CAMERA']:
            scene.camera = cam
            scene.render.filepath = os.path.join(rcct.path_dir, cam.name)
#            bpy.ops.anim.change_frame(rcct.start_frame)
#            bpy.ops.anim.end_frame_set()
#            bpy.ops.anim.change_frame(rcct.end_frame)
#            bpy.ops.anim.start_frame_set()
            bpy.ops.render.render(write_still=True)
            scene.render.filepath = rcct.path_dir

        return {'FINISHED'}


class RenderCollectionCamerasAnim(Operator):
    """Render Collection Cameras Animations"""
    bl_idname = "render.collection_cameras_animations"
    bl_label = "Render Collection Cameras Animations"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        scene = context.scene
        rcct = scene.rcct
        print("start rendering cameras in collection:", rcct.collection)
        for cam in [obj for obj in bpy.data.collections[rcct.collection].all_objects if obj.type == 'CAMERA']:
            scene.camera = cam
            scene.render.filepath = os.path.join(rcct.path_dir, cam.name)
#            bpy.ops.anim.change_frame(rcct.start_frame)
#            bpy.ops.anim.end_frame_set()
#            bpy.ops.anim.change_frame(rcct.end_frame)
#            bpy.ops.anim.start_frame_set()
            bpy.ops.render.render(animation=True, write_still=False)
            scene.render.filepath = rcct.path_dir

        return {'FINISHED'}


# ------------------------------------------------------------------------
#    In-Panel Menus
# ------------------------------------------------------------------------

#class OBJECT_MT_CustomMenu(Menu):
#    bl_label = "Custom Render"
#    bl_idname = "OBJECT_MT_custom_menu"

#    def draw(self, context):
#        layout = self.layout

        # Built-in operators
#        layout.operator("object.select_all", text="Select/Deselect All").action = 'TOGGLE'
#        layout.operator("object.select_all", text="Inverse").action = 'INVERT'
#        layout.operator("object.select_random", text="Random")


# ------------------------------------------------------------------------
#    Panel in Object Mode
# ------------------------------------------------------------------------

class RCCT_PT_Panel(Panel):
    bl_label = "Render Collection Cameras"
    bl_idname = "RCCT_PT_Panel"
    bl_space_type = "PROPERTIES"
    bl_region_type = "WINDOW" #UI
    bl_category = "RCCT"
    bl_context = "output"
    bl_options = {'DEFAULT_CLOSED'}


#    @classmethod
#    def poll(self,context):
#        return context.object is not None

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        rcct = scene.rcct

        layout.prop(rcct, "path_dir")
#        layout.prop(rcct, "start_frame") 
#        layout.prop(rcct, "end_frame")
        layout.prop_search(rcct, "collection", bpy.data, "collections")
        layout.operator("render.collection_cameras_images")
        layout.operator("render.collection_cameras_animations")
        #layout.menu(OBJECT_MT_CustomMenu.bl_idname, text="Presets", icon="SCENE")
        layout.separator()


# ------------------------------------------------------------------------
#    Registration
# ------------------------------------------------------------------------

classes = (
    RenderCollectionCamerasProperties,
    RenderCollectionCamerasImg,
    RenderCollectionCamerasAnim,
    #OBJECT_MT_CustomMenu,
    RCCT_PT_Panel
)

def menu_func(self, context):
    self.layout.operator(RenderCollectionCameras.bl_idname)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    Scene.rcct = PointerProperty(type=RenderCollectionCamerasProperties)
#    bpy.types.TOPBAR_MT_render.append(menu_func)

def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
    del Scene.rcct
#    bpy.types.TOPBAR_MT_render.remove(menu_func)


if __name__ == "__main__":
    register()
