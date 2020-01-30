# ------------------------------------------------------------------------
#    Render Properties
# ------------------------------------------------------------------------
import bpy
from bpy.props import StringProperty


class RenderCollectionCamerasProperties(bpy.types.PropertyGroup):

    path_dir: StringProperty(
        name="Output Dir",
        description="Choose a directory:",
        default="",
        maxlen=1024,
        subtype='DIR_PATH'
    )

    collection: StringProperty(
        name="Collection",
        description="Choose a collection:",
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


classes = (RenderCollectionCamerasProperties,)
