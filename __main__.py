import bpy
from bpy.types import Operator
from bpy.props import FloatVectorProperty
from bpy_extras.object_utils import AddObjectHelper, object_data_add
from mathutils import Vector


class OBJECT_OT_oshafy(bpy.types.Operator, AddObjectHelper):
    bl_idname = "object.oshafy"
    bl_label = "Oshafy a plane"
    def execute(self, context):
        bpy.ops.object.duplicate_move(OBJECT_OT_duplicate={"linked":False, "mode":'TRANSLATION'}, TRANSFORM_OT_translate={"value":(0, 0, 0), "orient_type":'GLOBAL', "orient_matrix":((1, 0, 0), (0, 1, 0), (0, 0, 1)), "orient_matrix_type":'GLOBAL', "constraint_axis":(False, False, False), "mirror":False, "use_proportional_edit":False, "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "use_proportional_connected":False, "use_proportional_projected":False, "snap":False, "snap_elements":{'GRID'}, "use_snap_project":False, "snap_target":'CLOSEST', "use_snap_self":True, "use_snap_edit":True, "use_snap_nonedit":True, "use_snap_selectable":False, "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "cursor_transform":False, "texture_space":False, "remove_on_cancel":False, "use_duplicated_keyframes":False, "view2d_edge_pan":False, "release_confirm":False, "use_accurate":False, "use_automerge_and_split":False})
        bpy.ops.object.editmode_toggle()
        bpy.ops.mesh.select_all(action='SELECT')
        bpy.ops.mesh.dissolve_limited()
        bpy.ops.object.editmode_toggle()
        bpy.ops.object.modifier_add(type='SCREW')
        
        bpy.context.object.modifiers["Screw"].angle = 0
        bpy.context.object.modifiers["Screw"].screw_offset = 1.5
        bpy.ops.object.modifier_add(type='WIREFRAME')
        bpy.context.object.modifiers["Wireframe"].thickness = 0.1
        bpy.context.object.modifiers["Screw"].steps = 15
        bpy.context.object.modifiers["Screw"].steps = 8
        bpy.context.object.modifiers["Screw"].render_steps = 8
        bpy.context.object.modifiers["Wireframe"].use_boundary = True
        bpy.context.object.modifiers["Wireframe"].offset = -4
        bpy.context.object.modifiers["Wireframe"].use_even_offset = False 
        return{"FINISHED"}
    
class OBJECT_OT_add_wiring_supports(bpy.types.Operator, AddObjectHelper):
    bl_idname = "object.add_wiring_supports"
    bl_label = "Generate wiring supports from a plane"
    def execute(self, context):
        bpy.ops.object.duplicate_move(OBJECT_OT_duplicate={"linked":False, "mode":'TRANSLATION'}, TRANSFORM_OT_translate={"value":(0, 0, 0), "orient_type":'GLOBAL', "orient_matrix":((1, 0, 0), (0, 1, 0), (0, 0, 1)), "orient_matrix_type":'GLOBAL', "constraint_axis":(False, False, False), "mirror":False, "use_proportional_edit":False, "proportional_edit_falloff":'SMOOTH', "proportional_size":6.11591, "use_proportional_connected":False, "use_proportional_projected":False, "snap":False, "snap_elements":{'GRID'}, "use_snap_project":False, "snap_target":'CLOSEST', "use_snap_self":True, "use_snap_edit":True, "use_snap_nonedit":True, "use_snap_selectable":False, "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "cursor_transform":False, "texture_space":False, "remove_on_cancel":False, "use_duplicated_keyframes":False, "view2d_edge_pan":False, "release_confirm":False, "use_accurate":False, "use_automerge_and_split":False})
        bpy.ops.object.editmode_toggle()
        bpy.ops.mesh.select_all(action='SELECT')
        bpy.ops.mesh.extrude_region_move(MESH_OT_extrude_region={"use_normal_flip":False, "use_dissolve_ortho_edges":False, "mirror":False}, TRANSFORM_OT_translate={"value":(0, 0, 14.7468), "orient_type":'GLOBAL', "orient_matrix":((1, 0, 0), (0, 1, 0), (0, 0, 1)), "orient_matrix_type":'GLOBAL', "constraint_axis":(False, False, True), "mirror":False, "use_proportional_edit":False, "proportional_edit_falloff":'SMOOTH', "proportional_size":6.11591, "use_proportional_connected":False, "use_proportional_projected":False, "snap":False, "snap_elements":{'GRID'}, "use_snap_project":False, "snap_target":'CLOSEST', "use_snap_self":True, "use_snap_edit":True, "use_snap_nonedit":True, "use_snap_selectable":False, "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "cursor_transform":False, "texture_space":False, "remove_on_cancel":False, "use_duplicated_keyframes":False, "view2d_edge_pan":False, "release_confirm":False, "use_accurate":False, "use_automerge_and_split":False})
        bpy.ops.mesh.delete(type='EDGE')
        bpy.ops.object.editmode_toggle()
        bpy.ops.object.modifier_add(type='SKIN')
        bpy.context.object.modifiers["Skin"].use_smooth_shade = True
        bpy.ops.object.modifier_add(type='WIREFRAME')
        bpy.context.object.modifiers["Wireframe"].thickness = 0.073
        bpy.ops.transform.translate(value=(-0, -0, -0.337619), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(False, False, True), mirror=False, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=6.11591, use_proportional_connected=False, use_proportional_projected=False, snap=False, snap_elements={'GRID'}, use_snap_project=False, snap_target='CLOSEST', use_snap_self=True, use_snap_edit=True, use_snap_nonedit=True, use_snap_selectable=False)
        return{"FINISHED"}
        
class OBJECT_OT_add_level_supports(bpy.types.Operator, AddObjectHelper):
    bl_idname = "object.add_level_supports"
    bl_label = "Generate downward level supports from a plane"
    def execute(self, context):
        bpy.ops.object.duplicate_move(OBJECT_OT_duplicate={"linked":False, "mode":'TRANSLATION'}, TRANSFORM_OT_translate={"value":(0, 0, 0), "orient_type":'GLOBAL', "orient_matrix":((1, 0, 0), (0, 1, 0), (0, 0, 1)), "orient_matrix_type":'GLOBAL', "constraint_axis":(False, False, False), "mirror":False, "use_proportional_edit":False, "proportional_edit_falloff":'SMOOTH', "proportional_size":6.11591, "use_proportional_connected":False, "use_proportional_projected":False, "snap":False, "snap_elements":{'GRID'}, "use_snap_project":False, "snap_target":'CLOSEST', "use_snap_self":True, "use_snap_edit":True, "use_snap_nonedit":True, "use_snap_selectable":False, "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "cursor_transform":False, "texture_space":False, "remove_on_cancel":False, "use_duplicated_keyframes":False, "view2d_edge_pan":False, "release_confirm":False, "use_accurate":False, "use_automerge_and_split":False})
        bpy.ops.object.editmode_toggle()
        bpy.ops.mesh.select_all(action='SELECT')
        bpy.ops.mesh.extrude_region_move(MESH_OT_extrude_region={"use_normal_flip":False, "use_dissolve_ortho_edges":False, "mirror":False}, TRANSFORM_OT_translate={"value":(0, 0, -24.7468), "orient_type":'GLOBAL', "orient_matrix":((1, 0, 0), (0, 1, 0), (0, 0, 1)), "orient_matrix_type":'GLOBAL', "constraint_axis":(False, False, True), "mirror":False, "use_proportional_edit":False, "proportional_edit_falloff":'SMOOTH', "proportional_size":6.11591, "use_proportional_connected":False, "use_proportional_projected":False, "snap":False, "snap_elements":{'GRID'}, "use_snap_project":False, "snap_target":'CLOSEST', "use_snap_self":True, "use_snap_edit":True, "use_snap_nonedit":True, "use_snap_selectable":False, "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "cursor_transform":False, "texture_space":False, "remove_on_cancel":False, "use_duplicated_keyframes":False, "view2d_edge_pan":False, "release_confirm":False, "use_accurate":False, "use_automerge_and_split":False})
        bpy.ops.mesh.delete(type='EDGE')
        bpy.ops.object.editmode_toggle()
        bpy.ops.object.modifier_add(type='SKIN')
        bpy.context.object.modifiers["Skin"].use_smooth_shade = True
        bpy.ops.object.modifier_add(type='WIREFRAME')
        bpy.context.object.modifiers["Wireframe"].thickness = 0.073
        bpy.ops.transform.translate(value=(-0, -0, -0.337619), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(False, False, True), mirror=False, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=6.11591, use_proportional_connected=False, use_proportional_projected=False, snap=False, snap_elements={'GRID'}, use_snap_project=False, snap_target='CLOSEST', use_snap_self=True, use_snap_edit=True, use_snap_nonedit=True, use_snap_selectable=False)    
        return{"FINISHED"}
    
class OBJECT_OT_make_ceiling(bpy.types.Operator):
    
    bl_idname = "object.archino_make_ceiling"
    bl_label = "Make ceiling"
    bl_options = { 'REGISTER','UNDO' }
    
    
    def execute(self, context):
        scene = context.scene
        bpy.ops.object.duplicate_move(OBJECT_OT_duplicate={"linked":False, "mode":'TRANSLATION'}, TRANSFORM_OT_translate={"value":(0, 0, 2), "orient_type":'GLOBAL', "orient_matrix":((1, 0, 0), (0, 1, 0), (0, 0, 1)), "orient_matrix_type":'GLOBAL', "constraint_axis":(False, False, True), "mirror":False, "use_proportional_edit":False, "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "use_proportional_connected":False, "use_proportional_projected":False, "snap":True, "snap_elements":{'INCREMENT'}, "use_snap_project":False, "snap_target":'CLOSEST', "use_snap_self":True, "use_snap_edit":True, "use_snap_nonedit":True, "use_snap_selectable":False, "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "cursor_transform":False, "texture_space":False, "remove_on_cancel":False, "use_duplicated_keyframes":False, "view2d_edge_pan":False, "release_confirm":False, "use_accurate":False, "use_automerge_and_split":False})
        bpy.ops.object.modifier_remove(modifier="Screw")
        bpy.ops.object.modifier_remove(modifier="Bevel")
        bpy.ops.object.modifier_remove(modifier="Solidify")
        bpy.ops.object.modifier_remove(modifier="WeighedNormal")
        bpy.ops.object.modifier_remove(modifier="UVProject")
        bpy.ops.object.editmode_toggle()
        bpy.ops.mesh.select_all(action='SELECT')
        bpy.ops.mesh.edge_face_add()
        bpy.ops.mesh.quads_convert_to_tris(quad_method='BEAUTY', ngon_method='BEAUTY')
        bpy.ops.mesh.quads_convert_to_tris(quad_method='LONGEST_DIAGONAL', ngon_method='CLIP')
        bpy.ops.object.editmode_toggle()
        bpy.ops.transform.translate(value=(-0, -0, 0.1), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(False, False, True), mirror=False, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False, snap=True, snap_elements={'INCREMENT'}, use_snap_project=False, snap_target='CLOSEST', use_snap_self=True, use_snap_edit=True, use_snap_nonedit=True, use_snap_selectable=False)
        bpy.ops.object.modifier_add(type='SOLIDIFY')
        bpy.context.object.modifiers["Solidify"].thickness = -0.03
        return{"FINISHED"}

class OBJECT_OT_3planar_dynamic(bpy.types.Operator):
    bl_idname = "object.create_3planar_architect"
    bl_label = "Create tri-planar projection"
    bl_options = { 'REGISTER','UNDO' }
    
    
    def execute(self, context):
        scene = context.scene
        act = bpy.context.active_object
        bpy.ops.object.modifier_add(type='UV_PROJECT')
        context.object.modifiers["UVProject"].projector_count = 6        
        ogcontext = context.object.name
        
        def makeprojectors(): #recorded from manual action by info console!
            bpy.ops.object.empty_add(type='SINGLE_ARROW', align='WORLD', location=(1.63202, 0.0866237, 1), scale=(1, 1, 1))
            bpy.context.object.name = ogcontext + "_uvp1"
            bpy.ops.object.empty_add(type='SINGLE_ARROW', align='WORLD', location=(1.63202, 0.0866237, 1), scale=(1, 1, 1))
            bpy.ops.transform.rotate(value=1.5708, orient_axis='X', orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(True, False, False), mirror=False, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False, snap=False, snap_elements={'INCREMENT'}, use_snap_project=False, snap_target='CLOSEST', use_snap_self=True, use_snap_edit=True, use_snap_nonedit=True, use_snap_selectable=False)
            bpy.context.object.name = ogcontext + "_uvp2"
            bpy.ops.object.empty_add(type='SINGLE_ARROW', align='WORLD', location=(1.63202, 0.0866237, 1), scale=(1, 1, 1))
            bpy.ops.transform.rotate(value=1.5708, orient_axis='X', orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(True, False, False), mirror=False, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False, snap=False, snap_elements={'INCREMENT'}, use_snap_project=False, snap_target='CLOSEST', use_snap_self=True, use_snap_edit=True, use_snap_nonedit=True, use_snap_selectable=False)
            bpy.ops.transform.rotate(value=1.5708, orient_axis='Z', orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(False, False, True), mirror=False, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False, snap=False, snap_elements={'INCREMENT'}, use_snap_project=False, snap_target='CLOSEST', use_snap_self=True, use_snap_edit=True, use_snap_nonedit=True, use_snap_selectable=False)
            bpy.context.object.name = ogcontext + "_uvp3"
            bpy.ops.object.empty_add(type='SINGLE_ARROW', align='WORLD', location=(1.63202, 0.0866237, 1), scale=(1, 1, 1))
            bpy.ops.transform.rotate(value=1.5708, orient_axis='Z', orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(False, False, True), mirror=False, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False, snap=False, snap_elements={'INCREMENT'}, use_snap_project=False, snap_target='CLOSEST', use_snap_self=True, use_snap_edit=True, use_snap_nonedit=True, use_snap_selectable=False)
            bpy.ops.transform.rotate(value=-1.5708, orient_axis='Y', orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(False, True, False), mirror=False, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False, snap=False, snap_elements={'INCREMENT'}, use_snap_project=False, snap_target='CLOSEST', use_snap_self=True, use_snap_edit=True, use_snap_nonedit=True, use_snap_selectable=False)
            bpy.context.object.name = ogcontext + "_uvp4"
            bpy.ops.object.empty_add(type='SINGLE_ARROW', align='WORLD', location=(1.63202, 0.0866237, 1), scale=(1, 1, 1))
            bpy.ops.transform.rotate(value=-1.5708, orient_axis='X', orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(True, False, False), mirror=False, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False, snap=False, snap_elements={'INCREMENT'}, use_snap_project=False, snap_target='CLOSEST', use_snap_self=True, use_snap_edit=True, use_snap_nonedit=True, use_snap_selectable=False)
            bpy.context.object.name = ogcontext + "_uvp5"
            bpy.ops.object.empty_add(type='SINGLE_ARROW', align='WORLD', location=(1.63202, 0.0866237, 1), scale=(1, 1, 1))
            bpy.ops.transform.rotate(value=3.14159, orient_axis='X', orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(True, False, False), mirror=False, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False, snap=False, snap_elements={'INCREMENT'}, use_snap_project=False, snap_target='CLOSEST', use_snap_self=True, use_snap_edit=True, use_snap_nonedit=True, use_snap_selectable=False)
            bpy.context.object.name = ogcontext + "_uvp6"
            #bpy.ops.outliner.item_activate(extend_range=True, deselect_all=True)
            return {"PROJECTORS ADDED"}
        
        def add_3planar_stack():    
            makeprojectors()
            
            bpy.ops.object.select_all(action='DESELECT')
            bpy.data.objects[ogcontext].select_set(True)
            bpy.context.view_layer.objects.active = bpy.data.objects[ogcontext]
            
            # to select the only the object in the 3D viewport
            
            ind = 0
            for p in context.object.modifiers["UVProject"].projectors:
                ind += 1
                p.object = bpy.data.objects[ogcontext + "_uvp" + str(ind)]
                
        add_3planar_stack()
        
        return {"FINISHED"}
    
                    
class OBJECT_PT_ainorchitect_panel(bpy.types.Panel):
    bl_label = "Archino"
    bl_idname = "OBJECT_PT_matek"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Ainorchitect'
    
    def draw(self, context):
        layout = self.layout
        layout.operator("object.create_3planar_architect")
        layout.operator("object.create_aino_floorplan")
        layout.operator("object.archino_make_ceiling")
        layout.operator("object.oshafy")
        layout.operator("object.add_wiring_supports")
        layout.operator("object.add_level_supports")

class OBJECT_OT_aino_floorplanner(bpy.types.Operator, AddObjectHelper):
    bl_idname = "mesh.create_aino_floorplan"
    bl_label = "Create aino floorplan"
    bl_options = { 'REGISTER','UNDO' }
     
    scale: FloatVectorProperty(
        name="scale",
        default=(1.0, 1.0, 1.0),
        subtype='TRANSLATION',
        description="scaling",
    )
    
    def execute(self, context):
        def make_floorplan(self, context):
            scale_x = self.scale.x * 1
            scale_y = self.scale.y * 1
            verts = [
                Vector((1 * scale_x, 1 * scale_y, 0)),
                Vector((1 * scale_x, 1 * scale_y, 0)),
                #Vector((1 * scale_x, -1 * scale_y, 0)),
                #Vector((-1 * scale_x, -1 * scale_y, 0)),
            ]

            edges = [[0,1]]
            faces = []

            mesh = bpy.data.meshes.new(name="Floorplan")
            mesh.from_pydata(verts, edges, faces)
            # useful for development when the mesh may be invalid.
            mesh.validate(verbose=True)
            object_data_add(context, mesh, operator=self)
            
            bpy.ops.object.modifier_add(type='SCREW')
            bpy.context.object.modifiers["Screw"].angle = 0
            bpy.context.object.modifiers["Screw"].screw_offset = 2.5
            bpy.context.object.modifiers["Screw"].steps = 1
            bpy.context.object.modifiers["Screw"].render_steps = 1
            bpy.ops.object.modifier_add(type='SOLIDIFY')
            bpy.context.object.modifiers["Solidify"].use_even_offset = True
            bpy.context.object.modifiers["Solidify"].thickness = 0.38
            bpy.ops.object.modifier_add(type='WEIGHTED_NORMAL')
            bpy.ops.object.modifier_add(type='BEVEL')
            bpy.context.object.modifiers["Bevel"].offset_type = 'PERCENT'
            bpy.context.object.modifiers["Bevel"].width_pct = 0.1
            bpy.context.object.modifiers["Bevel"].segments = 2
            bpy.context.object.modifiers["Bevel"].width_pct = 1.7
            bpy.context.object.modifiers["WeightedNormal"].weight = 100
            bpy.context.object.modifiers["WeightedNormal"].keep_sharp = True
            bpy.context.object.modifiers["WeightedNormal"].use_face_influence = True
            bpy.context.object.modifiers["WeightedNormal"].thresh = 1.96
            bpy.context.object.modifiers["Solidify"].solidify_mode = 'NON_MANIFOLD'
            bpy.ops.object.modifier_add(type='BOOLEAN')
            bpy.context.object.modifiers["Boolean"].operand_type = 'COLLECTION'

            #bpy.context.object.scale[2] = 5
            OBJECT_OT_3planar_dynamic.execute(self, context)
            

            #gnmod = bpy.context.object.modifiers.new("ArchinoNodes", "NODES")
            #g = bpy.ops.node.new_geometry_node_group_assign()
            #bpy.ops.node.name = "ArchinoNodes"
            
            #bpy.ops.mesh.select_mode(use_extend=False, use_expand=False, type='VERT')

        
        #----Moving the view to ortho top and edit mode----------
        area_type = 'VIEW_3D'
        areas  = [area for area in bpy.context.window.screen.areas if area.type == area_type]
        
        override = {
            'window': bpy.context.window,
            'screen': bpy.context.window.screen,
            'area': areas[0],
            'region': [region for region in areas[0].regions if region.type == 'WINDOW'][0],
        }

        bpy.ops.view3d.view_axis( type='TOP', align_active=True)
        make_floorplan(self, context)
        bpy.ops.object.editmode_toggle()
        bpy.context.space_data.shading.type = 'WIREFRAME'
        bpy.ops.wm.tool_set_by_id(name="builtin.extrude_region")
        #----------------------------------------------------------
        return {'FINISHED'}

    
    
# Registration of architect object stuff    

def add_object_ainoarc_button(self, context):
    self.layout.operator(
        OBJECT_OT_aino_floorplanner.bl_idname,
        text="Add Aino Architect",
        icon='UGLYPACKAGE')


def register():
    bpy.utils.register_class(OBJECT_OT_3planar_dynamic)
    bpy.utils.register_class(OBJECT_OT_aino_floorplanner)
    bpy.utils.register_class(OBJECT_OT_add_wiring_supports)
    bpy.utils.register_class(OBJECT_OT_make_ceiling)
    bpy.utils.register_class(OBJECT_PT_ainorchitect_panel)
    bpy.utils.register_class(OBJECT_OT_oshafy)
    bpy.utils.register_class(OBJECT_OT_add_level_supports)
    #bpy.utils.register_class(OBJECT_OT_add_object_ainoarc)
    bpy.types.VIEW3D_MT_mesh_add.append(add_object_ainoarc_button)

def unregister():
    bpy.utils.unregister_class(OBJECT_OT_3planar_dynamic)
    bpy.utils.unregister_class(OBJECT_OT_add_wiring_supports)
    bpy.utils.unregister_class(OBJECT_OT_aino_floorplanner)
    bpy.utils.unregister_class(OBJECT_PT_ainorchitect_panel)
    bpy.utils.unregister_class(OBJECT_OT_make_ceiling)
    bpy.utils.unregister_class(OBJECT_OT_oshafy)
    bpy.utils.unregister_class(OBJECT_OT_add_level_supports)
    #bpy.utils.unregister_class(OBJECT_OT_add_object_ainoarc)
    bpy.types.VIEW3D_MT_mesh_add.remove(add_object_ainoarc_button)
if __name__ == "__main__":
    register()
        