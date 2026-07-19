bl_info = {
    "name": "PS2 Character Generator",
    "author": "MJWilde93",
    "version": (0, 1, 0),
    "blender": (4, 0, 0),
    "location": "View3D > Sidebar > PS2 Character",
    "description": "Procedural PS2-style character generator",
    "category": "Add Mesh",
}


import bpy

from . import properties
from . import operators
from . import ui


classes = (
    properties.PS2CharacterProperties,
    operators.PS2_OT_GenerateCharacter,
    ui.PS2_PT_MainPanel,
)


def register():
    for cls in classes:
        bpy.utils.register_class(cls)

    bpy.types.Scene.ps2_character = bpy.props.PointerProperty(
        type=properties.PS2CharacterProperties
    )


def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)

    del bpy.types.Scene.ps2_character


if __name__ == "__main__":
    register()
