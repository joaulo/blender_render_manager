import bpy


# ------------------------------------------------------------------------
#    Panel in Object Mode
# ------------------------------------------------------------------------

class RenderCollectionCamerasPanel:
    bl_space_type = "PROPERTIES"
    bl_region_type = "WINDOW"  # UI
    bl_category = "RCC"
    bl_context = "output"
    bl_options = {'DEFAULT_CLOSED'}


class RCC_PT_render_collection_cameras(RenderCollectionCamerasPanel, bpy.types.Panel):
    bl_idname = "RCC_PT_render_collection_cameras"
    bl_label = "Render Collection Cameras"

#    @classmethod
#    def poll(self,context):
#        return context.object is not None

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        rcc = scene.render_collection_cameras

        layout.prop(rcc, "path_dir")
#        layout.prop(rcc, "start_frame")
#        layout.prop(rcc, "end_frame")
        layout.prop_search(rcc, "collection", bpy.data, "collections")
        layout.operator("render.collection_cameras_images")
        layout.operator("render.collection_cameras_animations")
        # layout.menu(OBJECT_MT_CustomMenu.bl_idname, text="Presets", icon="SCENE")
        layout.separator()


class RCC_PT_rcc_load_settings(RenderCollectionCamerasPanel, bpy.types.Panel):
    bl_parent_id = "RCC_PT_render_collection_cameras"
    bl_label = "Load Settings"

    def draw(self, context):
        layout = self.layout
        layout.operator("load.render_settings")


class RCC_PT_rcc_save_settings(RenderCollectionCamerasPanel, bpy.types.Panel):
    bl_parent_id = "RCC_PT_render_collection_cameras"
    bl_label = "Save Settings"

    def draw(self, context):
        layout = self.layout
        layout.operator("save.render_settings")


classes = (
    RCC_PT_render_collection_cameras,
    RCC_PT_rcc_load_settings,
    RCC_PT_rcc_save_settings,
)
