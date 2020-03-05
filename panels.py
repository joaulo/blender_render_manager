import bpy


# ------------------------------------------------------------------------
#    Panel in Object Mode
# ------------------------------------------------------------------------

class RenderManagerPanel:
    bl_space_type = "PROPERTIES"
    bl_region_type = "WINDOW"  # UI
    bl_category = "RCC"
    bl_context = "output"
    bl_options = {'DEFAULT_CLOSED'}


class RM_PT_RenderManager(RenderManagerPanel, bpy.types.Panel):
    bl_idname = "RM_PT_RenderManager"
    bl_label = "Render Collection Cameras"

#    @classmethod
#    def poll(self,context):
#        return context.object is not None

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        render_manager = scene.render_manager

        layout.prop(render_manager, "path_dir")
#        layout.prop(render_manager, "start_frame")
#        layout.prop(render_manager, "end_frame")
        layout.prop_search(render_manager, "collection", bpy.data, "collections")
        layout.operator("render.manage_images")
        layout.operator("render.manage_animations")
        # layout.menu(OBJECT_MT_CustomMenu.bl_idname, text="Presets", icon="SCENE")
        layout.separator()


class RM_PT_LoadSettings(RenderManagerPanel, bpy.types.Panel):
    bl_parent_id = "RM_PT_RenderManager"
    bl_label = "Load Settings"

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        render_manager = scene.render_manager

        layout.prop(render_manager, "load_render_settings")
        layout.operator("load.render_settings")


class RM_PT_SaveSettings(RenderManagerPanel, bpy.types.Panel):
    bl_parent_id = "RM_PT_RenderManager"
    bl_label = "Save Settings"

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        render_manager = scene.render_manager

        layout.prop(render_manager, "save_render_settings")
        layout.operator("save.render_settings")


classes = (
    RM_PT_RenderManager,
    RM_PT_LoadSettings,
    RM_PT_SaveSettings,
)
