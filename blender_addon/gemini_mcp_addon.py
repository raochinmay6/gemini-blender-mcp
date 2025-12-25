bl_info = {
    "name": "Gemini MCP Bridge",
    "blender": (3, 0, 0),
    "category": "System",
}

import bpy
import socket
import threading

HOST = "127.0.0.1"
PORT = 5555

def execute_code(code):
    try:
        exec(code, {"bpy": bpy})
    except Exception as e:
        print("Gemini MCP Error:", e)

def server():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen(1)
    while True:
        conn, _ = s.accept()
        data = conn.recv(65536).decode("utf-8")
        execute_code(data)
        conn.close()

class GEMINI_OT_start(bpy.types.Operator):
    bl_idname = "wm.gemini_mcp_start"
    bl_label = "Start Gemini MCP"

    def execute(self, context):
        threading.Thread(target=server, daemon=True).start()
        self.report({'INFO'}, "Gemini MCP running")
        return {'FINISHED'}

def register():
    bpy.utils.register_class(GEMINI_OT_start)

def unregister():
    bpy.utils.unregister_class(GEMINI_OT_start)
