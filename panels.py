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


class JSWK_PT_RenderManager(RenderManagerPanel, bpy.types.Panel):
    bl_idname = "JSWK_PT_RenderManager"
    bl_label = "Render Manager"

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
        layout.operator("jswk.render_manager_images")
        layout.operator("jswk.render_manager_animations")
        # layout.menu(OBJECT_MT_CustomMenu.bl_idname, text="Presets", icon="SCENE")
        layout.separator()


class JSWK_PT_LoadSettings(RenderManagerPanel, bpy.types.Panel):
    bl_parent_id = "JSWK_PT_RenderManager"
    bl_label = "Load Settings"

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        render_manager = scene.render_manager

        layout.prop(render_manager, "load_render_settings")
        layout.operator("jswk.load_render_settings")


class JSWK_PT_SaveSettings(RenderManagerPanel, bpy.types.Panel):
    bl_parent_id = "JSWK_PT_RenderManager"
    bl_label = "Save Settings"

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        render_manager = scene.render_manager

        layout.prop(render_manager, "save_render_settings")
        layout.operator("jswk.save_render_settings")


classes = (
    JSWK_PT_RenderManager,
    JSWK_PT_LoadSettings,
    JSWK_PT_SaveSettings,
)
