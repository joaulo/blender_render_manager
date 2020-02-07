# ------------------------------------------------------------------------
#    Render Properties
# ------------------------------------------------------------------------
import bpy
from bpy.props import StringProperty


class RenderCollectionCamerasProperties(bpy.types.PropertyGroup):

    path_dir: StringProperty(
        name="Render output dir:",
        description="Choose a directory to save render files",
        default="",
        maxlen=1024,
        subtype='DIR_PATH'
    )

    collection: StringProperty(
        name="Select a collection:",
        description="Choose a collection with some cameras",
        default="",
    )

    # start_frame: IntProperty(
    #     name="Start Frame",
    #     description="Start Frame:",
    #     default=1,
    #     min=1
    # )

    # end_frame: IntProperty(
    #     name="End Frame",
    #     description="End Frame:",
    #     default=100,
    #     min=1
    # )

    save_render_settings: StringProperty(
        name="Save render settings to file:",
        description="Choose a file to save render settings",
        default="",
        maxlen=1024,
        subtype='FILE_PATH'
    )

    load_render_settings: StringProperty(
        name="Load render settings from file:",
        description="Choose a file to load render settings",
        default="",
        maxlen=1024,
        subtype='FILE_PATH'
    )


classes = (RenderCollectionCamerasProperties,)
