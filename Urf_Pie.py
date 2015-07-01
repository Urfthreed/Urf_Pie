bl_info = {
    "name": "Urf_Pie",
    "author": "Urf",
    "version": (0, 2,),
    "blender": (2, 74, 1),
    "description": "Grease Pencil Animation Pie Menu",
    "warning": "",
    "wiki_url": "https://www.tumblr.com/blog/urf3d",
    "category": "User Interface",
}

import bpy
from bpy.types import Header, Menu, Panel

class Urf_pie(Menu):
    # label is displayed at the center of the pie menu.
    bl_label = "Urf's Pie"
    bl_idname="Urf_pie"

    @classmethod
    def poll(cls, context):
        return bool(context.gpencil_data and context.active_gpencil_layer)

    def draw(self, context):
        layout = self.layout

        pie = layout.menu_pie()
        # gpd = context.gpencil_data
        gpl = context.active_gpencil_layer
        
        # W - Stroke draw settings
        col = pie.column(align=True)
        col.label(text="Stroke")
        col.prop(gpl, "color", text="")
        col.prop(gpl, "alpha", text="", slider=True)
        
        #E - Frame Fwd
        col = pie.column()
        col.label("Frame Fwd x 2")
        row = col.row()
        row.operator("screen.frame_offset", icon="TRIA_RIGHT", text=" ").delta=2
        
        #S - Layer settings
        col = pie.column()
        col.prop(gpl, "line_width", slider=True)
        # col.prop(gpl, "use_volumetric_strokes")
        col.prop(gpl, "use_onion_skinning")
        
        #N - Active Layer
        # XXX: this should show an operator to change the active layer instead
        col = pie.column()
        col.label("Active Layer:      ")
        col.prop(gpl, "info", text="")
        # col.prop(gpd, "layers")
        row = col.row()
        row.prop(gpl, "lock")
        row.prop(gpl, "hide")
        
        #NW - Add/Remove Layers
        
        col = pie.column()
        col.label("Rem/Add/Dupl Layer")
        row = col.row()
        row.operator("gpencil.layer_remove", icon='ZOOMOUT', text=" ")
        row.operator("gpencil.layer_add", icon='ZOOMIN', text=" ")
        row.operator("gpencil.layer_duplicate", icon='COPY_ID', text=" ")
        
        #NE - Keyframes
        
        col = pie.column()
        col.label("Keyframes")
        row = col.row()
        row.operator("screen.keyframe_jump", text=" ", icon='PREV_KEYFRAME').next = False
        row.operator("screen.animation_play", text=" ", icon='PLAY')
        row.operator("screen.keyframe_jump", text=" ", icon='NEXT_KEYFRAME').next = True
        
        #SE - Fill draw settings
        col = pie.column(align=True)
        col.label(text="Fill")
        col.prop(gpl, "fill_color", text="")
        col.prop(gpl, "fill_alpha", text="", slider=True)
                
        #SW - Timeline
        col = pie.column()
        col.label("Timeline")
        row = col.row()
        row.prop(context.scene, "frame_current", text="Frame")
         
        
def register():
    bpy.utils.register_class(Urf_pie)
    
    wm = bpy.context.window_manager
    km = wm.keyconfigs.addon.keymaps.new(name="Grease Pencil")
    kmi = km.keymap_items.new("wm.call_menu_pie", "E", "PRESS", key_modifier="D").properties.name="Urf_pie"


def unregister():
    bpy.utils.unregister_class(Urf_pie)


if __name__ == "__main__":
    register()
