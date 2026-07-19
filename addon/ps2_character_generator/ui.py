import bpy
from bpy.types import Panel


class PS2_PT_MainPanel(Panel):

    bl_label = "PS2 Character Generator"
    bl_idname = "PS2_PT_MainPanel"

    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "PS2 Character"

    def draw(self, context):

        layout = self.layout

        props = context.scene.ps2_character

        layout.prop(
            props,
            "head_size"
        )

        layout.prop(
            props,
            "triangle_budget"
        )

        layout.operator(
            "ps2.generate_character"
        )
