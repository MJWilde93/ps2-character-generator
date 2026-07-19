import bpy
from bpy.types import PropertyGroup
from bpy.props import FloatProperty, IntProperty


class PS2CharacterProperties(PropertyGroup):

    head_size: FloatProperty(
        name="Head Size",
        default=1.2,
        min=0.5,
        max=2.0
    )

    triangle_budget: IntProperty(
        name="Triangle Budget",
        default=1800,
        min=500,
        max=10000
    )
