# local import
from . import (
    properties,
    operators,
    panels,
)

# blender related import
import bpy
from bpy.props import PointerProperty


bl_info = {
    "name": "Render Collection Cameras",
    "author": "joaulo",
    "version": (1, 0, 0),
    "blender": (2, 80, 0),
    "location": "Render output panel",
    "description": "save/load render output settings and start render still images or animations for all the cameras in the selected collection",
    # "warning": "",  # used for warning icon and text in addons panel
    "wiki_url": "",
    # "tracker_url": "",
    "category": "Render",
}


# ------------------------------------------------------------------------
#    In-Panel Menus
# ------------------------------------------------------------------------

# class OBJECT_MT_CustomMenu(Menu):
#    bl_label = "Custom Render"
#    bl_idname = "OBJECT_MT_custom_menu"

#    def draw(self, context):
#        layout = self.layout

# Built-in operators
#        layout.operator("object.select_all", text="Select/Deselect All").action = 'TOGGLE'
#        layout.operator("object.select_all", text="Inverse").action = 'INVERT'
#        layout.operator("object.select_random", text="Random")


classes = properties.classes + operators.classes + panels.classes


# ------------------------------------------------------------------------
#    Registration
# ------------------------------------------------------------------------


# def menu_func(self, context):
#     self.layout.operator(RenderCollectionCamerasImg.bl_idname)
#     self.layout.operator(RenderCollectionCamerasAnim.bl_idname)


def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    bpy.types.Scene.render_collection_cameras = PointerProperty(
        type=properties.RenderCollectionCamerasProperties)
#    bpy.types.TOPBAR_MT_render.append(menu_func)


def unregister():
    #    bpy.types.TOPBAR_MT_render.remove(menu_func)
    del bpy.types.Scene.render_collection_cameras
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)


if __name__ == "__main__":
    register()
