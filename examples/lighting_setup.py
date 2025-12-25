import bpy

light = bpy.data.lights.new(name="KeyLight", type='AREA')
obj = bpy.data.objects.new(name="KeyLight", object_data=light)
bpy.context.collection.objects.link(obj)
obj.location = (4, -4, 5)
