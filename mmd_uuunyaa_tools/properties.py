# -*- coding: utf-8 -*-

import os
import glob

import bpy
from mmd_uuunyaa_tools import material_tuner


def load_previews():
    global previews
    previews = bpy.utils.previews.new()
    for path in glob.glob(os.path.join(os.path.dirname(__file__), 'thumbnails', '*.png')):
        previews.load(os.path.basename(path), path, 'IMAGE')

load_previews()

def update_material_thumbnails(property, context):
    bpy.ops.mmd_uuunyaa_tools.tune_material(material=property.thumbnails)

class MaterialPropertyGroup(bpy.types.PropertyGroup):
    thumbnails: bpy.props.EnumProperty(
        items=[(id, t.tuner.get_material_name(), '', previews[t.icon_filename].icon_id, i) for i, (id, t) in enumerate(material_tuner.TUNERS.items())],
        description='Choose the material you want to use',
        update=update_material_thumbnails,
    )

    @staticmethod
    def register():
        bpy.types.Material.mmd_uuunyaa_tools = bpy.props.PointerProperty(type=MaterialPropertyGroup)

    @staticmethod
    def unregister():
        del bpy.types.Material.mmd_uuunyaa_tools