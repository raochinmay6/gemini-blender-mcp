import bpy

cam = bpy.data.cameras.new("Camera")
cam_obj = bpy.data.objects.new("Camera", cam)
bpy.context.collection.objects.link(cam_obj)
cam_obj.location = (0, -6, 1.6)
cam_obj.rotation_euler = (1.57, 0, 0)
bpy.context.scene.camera = cam_obj
