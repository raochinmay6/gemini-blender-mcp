import bpy

for obj in bpy.data.objects:
    obj.name = obj.name.encode("ascii", "ignore").decode()
