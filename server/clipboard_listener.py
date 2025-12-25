import pyperclip
import time
from gemini_mcp_server import send_to_blender

print("Gemini MCP Clipboard Listener running")

last = ""
while True:
    text = pyperclip.paste()
    if text != last and text.strip().startswith("import bpy"):
        send_to_blender(text)
        print("✔ Sent to Blender")
        last = text
    time.sleep(0.8)
